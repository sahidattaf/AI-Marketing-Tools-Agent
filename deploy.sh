#!/bin/bash

# AI Marketing Tools - Production Deployment Script
# This script handles the complete deployment process for the AI Marketing Tools platform

set -e  # Exit on any error

# Configuration
PROJECT_NAME="ai-marketing-tools"
DOCKER_COMPOSE_FILE="docker/docker-compose.yml"
BACKUP_DIR="/backup/ai-marketing-tools"
LOG_FILE="/var/log/ai-marketing-deploy.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
    exit 1
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        error "This script should not be run as root for security reasons"
    fi
}

# Check prerequisites
check_prerequisites() {
    log "Checking prerequisites..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        error "Docker is not installed. Please install Docker first."
    fi
    
    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        error "Docker Compose is not installed. Please install Docker Compose first."
    fi
    
    # Check if user is in docker group
    if ! groups $USER | grep &>/dev/null '\bdocker\b'; then
        error "User $USER is not in the docker group. Please add user to docker group and re-login."
    fi
    
    # Check available disk space (minimum 5GB)
    available_space=$(df / | awk 'NR==2 {print $4}')
    if [[ $available_space -lt 5242880 ]]; then  # 5GB in KB
        warning "Less than 5GB disk space available. Deployment may fail."
    fi
    
    log "Prerequisites check completed successfully"
}

# Create necessary directories
create_directories() {
    log "Creating necessary directories..."
    
    sudo mkdir -p "$BACKUP_DIR"
    sudo mkdir -p /var/log/ai-marketing-tools
    sudo mkdir -p /etc/ai-marketing-tools
    
    # Set proper permissions
    sudo chown -R $USER:$USER "$BACKUP_DIR"
    sudo chown -R $USER:$USER /var/log/ai-marketing-tools
    
    log "Directories created successfully"
}

# Backup existing deployment
backup_existing() {
    log "Creating backup of existing deployment..."
    
    if [[ -d "/opt/ai-marketing-tools" ]]; then
        backup_name="backup-$(date +%Y%m%d-%H%M%S)"
        sudo cp -r /opt/ai-marketing-tools "$BACKUP_DIR/$backup_name"
        log "Backup created: $BACKUP_DIR/$backup_name"
    else
        info "No existing deployment found, skipping backup"
    fi
}

# Setup environment variables
setup_environment() {
    log "Setting up environment variables..."
    
    # Create .env file if it doesn't exist
    if [[ ! -f ".env" ]]; then
        cat > .env << EOF
# AI Marketing Tools Environment Configuration
NODE_ENV=production
FLASK_ENV=production

# Database Configuration
DB_PASSWORD=$(openssl rand -base64 32)
DATABASE_URL=postgresql://marketing_user:\${DB_PASSWORD}@database:5432/ai_marketing

# API Configuration
API_KEY=$(openssl rand -base64 32)
JWT_SECRET=$(openssl rand -base64 32)

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=noreply@ai-marketing-tools.com
SMTP_PASSWORD=your_smtp_password_here

# Alert Configuration
ALERT_EMAIL=admin@ai-marketing-tools.com

# SSL Configuration
SSL_CERT_PATH=/etc/nginx/ssl/fullchain.pem
SSL_KEY_PATH=/etc/nginx/ssl/privkey.pem

# Monitoring Configuration
MONITORING_INTERVAL=60
ENABLE_ALERTS=true

# Backup Configuration
BACKUP_RETENTION_DAYS=30
BACKUP_SCHEDULE="0 2 * * *"
EOF
        log "Environment file created. Please update the configuration values."
        warning "Please edit .env file with your actual configuration values before continuing."
        read -p "Press Enter to continue after updating .env file..."
    fi
    
    # Load environment variables
    source .env
    
    log "Environment variables loaded"
}

# Generate SSL certificates (self-signed for development)
generate_ssl_certificates() {
    log "Generating SSL certificates..."
    
    SSL_DIR="ssl"
    mkdir -p "$SSL_DIR"
    
    if [[ ! -f "$SSL_DIR/privkey.pem" ]] || [[ ! -f "$SSL_DIR/fullchain.pem" ]]; then
        # Generate self-signed certificate for development
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout "$SSL_DIR/privkey.pem" \
            -out "$SSL_DIR/fullchain.pem" \
            -subj "/C=CW/ST=Curacao/L=Willemstad/O=AI Marketing Tools/CN=ai-marketing-tools.com"
        
        log "Self-signed SSL certificates generated"
        warning "For production, replace with valid SSL certificates from a trusted CA"
    else
        log "SSL certificates already exist"
    fi
}

# Build Docker images
build_images() {
    log "Building Docker images..."
    
    # Build backend image
    info "Building backend image..."
    docker build -f deployment/docker/Dockerfile.backend -t ai-marketing-backend:latest ai-marketing-backend/
    
    # Build frontend image
    info "Building frontend image..."
    docker build -f deployment/docker/Dockerfile.frontend -t ai-marketing-frontend:latest ai-marketing-web/
    
    # Build mobile image (if exists)
    if [[ -d "ai-marketing-mobile" ]]; then
        info "Building mobile image..."
        docker build -f deployment/docker/Dockerfile.mobile -t ai-marketing-mobile:latest ai-marketing-mobile/
    fi
    
    log "Docker images built successfully"
}

# Deploy services
deploy_services() {
    log "Deploying services..."
    
    # Stop existing services
    info "Stopping existing services..."
    docker-compose -f "$DOCKER_COMPOSE_FILE" down --remove-orphans || true
    
    # Start services
    info "Starting services..."
    docker-compose -f "$DOCKER_COMPOSE_FILE" up -d
    
    # Wait for services to be healthy
    info "Waiting for services to be healthy..."
    sleep 30
    
    # Check service health
    check_service_health
    
    log "Services deployed successfully"
}

# Check service health
check_service_health() {
    log "Checking service health..."
    
    services=("backend" "frontend" "database" "redis")
    
    for service in "${services[@]}"; do
        info "Checking $service health..."
        
        # Wait up to 60 seconds for service to be healthy
        timeout=60
        while [[ $timeout -gt 0 ]]; do
            if docker-compose -f "$DOCKER_COMPOSE_FILE" ps "$service" | grep -q "healthy\|Up"; then
                log "$service is healthy"
                break
            fi
            
            sleep 5
            ((timeout-=5))
        done
        
        if [[ $timeout -eq 0 ]]; then
            error "$service failed to become healthy"
        fi
    done
    
    log "All services are healthy"
}

# Setup monitoring
setup_monitoring() {
    log "Setting up monitoring..."
    
    # Create monitoring configuration
    cat > config/monitoring.json << EOF
{
    "services": [
        {
            "name": "backend",
            "url": "http://localhost:5000/api/health",
            "interval": 30
        },
        {
            "name": "frontend",
            "url": "http://localhost/health",
            "interval": 30
        }
    ],
    "alerts": {
        "email": "$ALERT_EMAIL",
        "webhook": null
    },
    "retention": {
        "logs": 30,
        "metrics": 90
    }
}
EOF
    
    # Start monitoring service
    docker-compose -f "$DOCKER_COMPOSE_FILE" up -d monitoring
    
    log "Monitoring setup completed"
}

# Setup backup cron job
setup_backup() {
    log "Setting up automated backups..."
    
    # Create backup script
    cat > scripts/backup.sh << 'EOF'
#!/bin/bash
# Automated backup script for AI Marketing Tools

BACKUP_DIR="/backup/ai-marketing-tools"
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_NAME="backup-$DATE"

# Create backup directory
mkdir -p "$BACKUP_DIR/$BACKUP_NAME"

# Backup database
docker exec ai-marketing-db pg_dump -U marketing_user ai_marketing > "$BACKUP_DIR/$BACKUP_NAME/database.sql"

# Backup application data
docker cp ai-marketing-backend:/app/data "$BACKUP_DIR/$BACKUP_NAME/"

# Backup logs
docker cp ai-marketing-backend:/app/logs "$BACKUP_DIR/$BACKUP_NAME/"

# Compress backup
tar -czf "$BACKUP_DIR/$BACKUP_NAME.tar.gz" -C "$BACKUP_DIR" "$BACKUP_NAME"
rm -rf "$BACKUP_DIR/$BACKUP_NAME"

# Clean old backups (keep last 30 days)
find "$BACKUP_DIR" -name "backup-*.tar.gz" -mtime +30 -delete

echo "Backup completed: $BACKUP_NAME.tar.gz"
EOF
    
    chmod +x scripts/backup.sh
    
    # Add to crontab
    (crontab -l 2>/dev/null; echo "$BACKUP_SCHEDULE /opt/ai-marketing-tools/scripts/backup.sh >> /var/log/ai-marketing-backup.log 2>&1") | crontab -
    
    log "Automated backup setup completed"
}

# Setup log rotation
setup_log_rotation() {
    log "Setting up log rotation..."
    
    sudo tee /etc/logrotate.d/ai-marketing-tools > /dev/null << EOF
/var/log/ai-marketing-tools/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 $USER $USER
    postrotate
        docker-compose -f /opt/ai-marketing-tools/$DOCKER_COMPOSE_FILE restart > /dev/null 2>&1 || true
    endscript
}
EOF
    
    log "Log rotation setup completed"
}

# Post-deployment verification
post_deployment_verification() {
    log "Running post-deployment verification..."
    
    # Test API endpoints
    info "Testing API endpoints..."
    
    # Wait for services to fully start
    sleep 10
    
    # Test health endpoint
    if curl -f http://localhost:5000/api/health > /dev/null 2>&1; then
        log "Backend API health check passed"
    else
        error "Backend API health check failed"
    fi
    
    # Test frontend
    if curl -f http://localhost/ > /dev/null 2>&1; then
        log "Frontend health check passed"
    else
        error "Frontend health check failed"
    fi
    
    # Test database connection
    if docker exec ai-marketing-db pg_isready -U marketing_user -d ai_marketing > /dev/null 2>&1; then
        log "Database connection check passed"
    else
        error "Database connection check failed"
    fi
    
    log "Post-deployment verification completed successfully"
}

# Display deployment summary
display_summary() {
    log "Deployment completed successfully!"
    
    echo ""
    echo "=== AI Marketing Tools Deployment Summary ==="
    echo ""
    echo "🌐 Web Application: http://localhost/"
    echo "📱 Mobile Application: http://localhost/mobile/"
    echo "🔧 API Endpoints: http://localhost:5000/api/"
    echo "📊 Monitoring Dashboard: http://localhost/monitoring/"
    echo ""
    echo "🔐 SSL Certificates: $SSL_DIR/"
    echo "💾 Backups: $BACKUP_DIR/"
    echo "📋 Logs: /var/log/ai-marketing-tools/"
    echo ""
    echo "📖 Documentation: See README.md files in each component"
    echo ""
    echo "⚠️  Important Notes:"
    echo "   - Update SSL certificates for production use"
    echo "   - Configure email settings in .env file"
    echo "   - Review security settings before public deployment"
    echo "   - Monitor logs for any issues"
    echo ""
    echo "🎉 Deployment completed at $(date)"
}

# Cleanup function
cleanup() {
    log "Cleaning up temporary files..."
    # Add any cleanup tasks here
}

# Main deployment function
main() {
    log "Starting AI Marketing Tools deployment..."
    
    # Trap cleanup on exit
    trap cleanup EXIT
    
    # Run deployment steps
    check_root
    check_prerequisites
    create_directories
    backup_existing
    setup_environment
    generate_ssl_certificates
    build_images
    deploy_services
    setup_monitoring
    setup_backup
    setup_log_rotation
    post_deployment_verification
    display_summary
    
    log "Deployment process completed successfully!"
}

# Script usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  -v, --verbose  Enable verbose output"
    echo "  --skip-backup  Skip backup of existing deployment"
    echo "  --dev          Deploy in development mode"
    echo ""
    echo "Examples:"
    echo "  $0                 # Standard production deployment"
    echo "  $0 --dev           # Development deployment"
    echo "  $0 --skip-backup   # Skip backup step"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -v|--verbose)
            set -x
            shift
            ;;
        --skip-backup)
            SKIP_BACKUP=true
            shift
            ;;
        --dev)
            DEV_MODE=true
            shift
            ;;
        *)
            error "Unknown option: $1"
            ;;
    esac
done

# Run main function
main "$@"

