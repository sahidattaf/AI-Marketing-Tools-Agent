# AI Marketing Tools - Deployment & Hosting Guide

This directory contains all the necessary configuration files, scripts, and documentation for deploying the AI Marketing Tools platform to production environments.

## Directory Structure

```
deployment/
├── docker/                    # Docker configuration files
│   ├── Dockerfile.backend     # Backend Flask application
│   ├── Dockerfile.frontend    # Frontend React application
│   ├── Dockerfile.mobile      # Mobile Expo application
│   └── docker-compose.yml     # Multi-service orchestration
├── nginx/                     # Nginx reverse proxy configuration
│   └── nginx.conf             # Production nginx configuration
├── scripts/                   # Deployment and maintenance scripts
│   ├── deploy.sh              # Main deployment script
│   ├── backup.sh              # Automated backup script
│   └── maintenance.sh         # Maintenance utilities
├── config/                    # Configuration templates
│   ├── production.env         # Production environment template
│   ├── monitoring.json        # Monitoring configuration
│   └── ssl.conf               # SSL configuration
├── ssl/                       # SSL certificates directory
└── README.md                  # This file
```

## Quick Start

### Prerequisites

Before deploying, ensure you have:

- **Docker** (version 20.10+)
- **Docker Compose** (version 2.0+)
- **Linux server** (Ubuntu 20.04+ recommended)
- **Domain name** pointed to your server
- **SSL certificates** (Let's Encrypt recommended)
- **Minimum 4GB RAM** and **20GB disk space**

### 1. Clone and Prepare

```bash
# Clone the repository
git clone <repository-url> ai-marketing-tools
cd ai-marketing-tools

# Make deployment script executable
chmod +x deployment/scripts/deploy.sh

# Copy environment template
cp deployment/config/production.env .env
```

### 2. Configure Environment

Edit the `.env` file with your production values:

```bash
nano .env
```

**Critical settings to update:**
- Database passwords
- API keys and secrets
- Email configuration
- Domain names
- SSL certificate paths

### 3. Deploy

Run the automated deployment script:

```bash
# Standard production deployment
./deployment/scripts/deploy.sh

# Development deployment
./deployment/scripts/deploy.sh --dev

# Skip backup (first deployment)
./deployment/scripts/deploy.sh --skip-backup
```

### 4. Verify Deployment

After deployment, verify all services are running:

```bash
# Check service status
docker-compose -f deployment/docker/docker-compose.yml ps

# Check logs
docker-compose -f deployment/docker/docker-compose.yml logs

# Test endpoints
curl http://localhost/api/health
curl http://localhost/
```

## Architecture Overview

### Service Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx Proxy   │    │   Frontend      │    │   Mobile App    │
│   (Port 80/443) │    │   (React)       │    │   (Expo)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Backend API   │    │   Database      │    │   Redis Cache   │
│   (Flask)       │    │   (PostgreSQL)  │    │   (Redis)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌─────────────────────────────────────────────────┐
         │              Monitoring System                  │
         │         (Analytics & Health Checks)            │
         └─────────────────────────────────────────────────┘
```

### Network Configuration

- **Frontend**: Served via Nginx on ports 80/443
- **Backend API**: Internal communication on port 5000
- **Mobile App**: Accessible via `/mobile/` path
- **Database**: Internal PostgreSQL on port 5432
- **Cache**: Internal Redis on port 6379
- **Monitoring**: Dashboard on `/monitoring/` path

## Configuration Details

### Environment Variables

#### Core Application Settings
```bash
NODE_ENV=production
FLASK_ENV=production
DEBUG=false
```

#### Database Configuration
```bash
DB_HOST=database
DB_PORT=5432
DB_NAME=ai_marketing
DB_USER=marketing_user
DB_PASSWORD=your_secure_password
```

#### Security Settings
```bash
JWT_SECRET=your_jwt_secret
API_KEY=your_api_key
SECRET_KEY=your_secret_key
BCRYPT_LOG_ROUNDS=12
```

#### Email Configuration
```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=noreply@ai-marketing-tools.com
SMTP_PASSWORD=your_email_password
```

### SSL Configuration

#### Using Let's Encrypt (Recommended)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificates
sudo certbot --nginx -d ai-marketing-tools.com -d www.ai-marketing-tools.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

#### Using Custom Certificates

Place your certificates in the `ssl/` directory:
- `fullchain.pem` - Full certificate chain
- `privkey.pem` - Private key

### Database Setup

#### PostgreSQL Configuration

The deployment uses PostgreSQL as the primary database:

```sql
-- Database initialization
CREATE DATABASE ai_marketing;
CREATE USER marketing_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE ai_marketing TO marketing_user;
```

#### Database Migrations

```bash
# Run migrations
docker exec ai-marketing-backend flask db upgrade

# Create new migration
docker exec ai-marketing-backend flask db migrate -m "Description"
```

### Monitoring Setup

#### Health Checks

All services include health checks:
- **Backend**: `GET /api/health`
- **Frontend**: `GET /health`
- **Database**: PostgreSQL connection test
- **Redis**: Redis ping test

#### Monitoring Dashboard

Access the monitoring dashboard at:
- **URL**: `https://your-domain.com/monitoring/`
- **Authentication**: Basic auth (configure in nginx)

#### Log Management

Logs are stored in:
- **Application logs**: `/var/log/ai-marketing-tools/`
- **Nginx logs**: `/var/log/nginx/`
- **Docker logs**: `docker-compose logs`

## Deployment Strategies

### Blue-Green Deployment

For zero-downtime deployments:

```bash
# Deploy to staging environment
./deployment/scripts/deploy.sh --env=staging

# Test staging environment
./deployment/scripts/test.sh --env=staging

# Switch to production
./deployment/scripts/switch.sh --from=staging --to=production
```

### Rolling Updates

For gradual updates:

```bash
# Update backend only
docker-compose -f deployment/docker/docker-compose.yml up -d --no-deps backend

# Update frontend only
docker-compose -f deployment/docker/docker-compose.yml up -d --no-deps frontend
```

### Rollback Procedure

If deployment fails:

```bash
# Quick rollback to previous version
docker-compose -f deployment/docker/docker-compose.yml down
docker-compose -f deployment/docker/docker-compose.yml up -d

# Restore from backup
./deployment/scripts/restore.sh --backup=backup-20250127-120000
```

## Scaling Configuration

### Horizontal Scaling

#### Load Balancer Setup

```nginx
upstream backend_servers {
    least_conn;
    server backend-1:5000 max_fails=3 fail_timeout=30s;
    server backend-2:5000 max_fails=3 fail_timeout=30s;
    server backend-3:5000 max_fails=3 fail_timeout=30s;
}
```

#### Database Scaling

```yaml
# Read replicas
database_replica:
  image: postgres:15-alpine
  environment:
    POSTGRES_MASTER_SERVICE: database
    POSTGRES_REPLICA_USER: replica_user
    POSTGRES_REPLICA_PASSWORD: replica_password
```

### Vertical Scaling

#### Resource Limits

```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
        reservations:
          cpus: '1.0'
          memory: 2G
```

## Security Configuration

### Firewall Setup

```bash
# UFW configuration
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable
```

### Security Headers

Nginx includes security headers:
- `X-Frame-Options: SAMEORIGIN`
- `X-Content-Type-Options: nosniff`
- `X-XSS-Protection: 1; mode=block`
- `Strict-Transport-Security: max-age=63072000`
- `Content-Security-Policy: ...`

### Database Security

```sql
-- Restrict database access
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO marketing_user;
GRANT CREATE ON SCHEMA public TO marketing_user;
```

## Backup and Recovery

### Automated Backups

Backups run daily at 2 AM:

```bash
# Manual backup
./deployment/scripts/backup.sh

# Restore from backup
./deployment/scripts/restore.sh --backup=backup-20250127-020000
```

### Backup Components

- **Database**: PostgreSQL dump
- **Application data**: User uploads, logs
- **Configuration**: Environment files, certificates

### Backup Storage

- **Local**: `/backup/ai-marketing-tools/`
- **Remote**: AWS S3 (configurable)
- **Retention**: 30 days (configurable)

## Performance Optimization

### Caching Strategy

#### Redis Caching

```python
# Application-level caching
@cache.memoize(timeout=300)
def get_user_analytics(user_id):
    return analytics_service.get_user_data(user_id)
```

#### Nginx Caching

```nginx
# Static asset caching
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### Database Optimization

```sql
-- Index optimization
CREATE INDEX idx_user_created_at ON users(created_at);
CREATE INDEX idx_analytics_timestamp ON analytics(timestamp);

-- Query optimization
EXPLAIN ANALYZE SELECT * FROM users WHERE created_at > NOW() - INTERVAL '30 days';
```

### CDN Integration

```bash
# CloudFlare configuration
CLOUDFLARE_ZONE_ID=your_zone_id
CLOUDFLARE_API_TOKEN=your_api_token

# Purge cache after deployment
curl -X POST "https://api.cloudflare.com/client/v4/zones/$CLOUDFLARE_ZONE_ID/purge_cache" \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
```

## Troubleshooting

### Common Issues

#### Service Won't Start

```bash
# Check logs
docker-compose -f deployment/docker/docker-compose.yml logs service_name

# Check resource usage
docker stats

# Check disk space
df -h
```

#### Database Connection Issues

```bash
# Test database connection
docker exec ai-marketing-db pg_isready -U marketing_user -d ai_marketing

# Check database logs
docker-compose -f deployment/docker/docker-compose.yml logs database
```

#### SSL Certificate Issues

```bash
# Check certificate validity
openssl x509 -in ssl/fullchain.pem -text -noout

# Test SSL configuration
curl -I https://your-domain.com
```

### Performance Issues

#### High CPU Usage

```bash
# Check process usage
docker exec ai-marketing-backend top

# Scale up resources
docker-compose -f deployment/docker/docker-compose.yml up -d --scale backend=3
```

#### Memory Leaks

```bash
# Monitor memory usage
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Restart services
docker-compose -f deployment/docker/docker-compose.yml restart backend
```

### Log Analysis

#### Application Logs

```bash
# Real-time logs
docker-compose -f deployment/docker/docker-compose.yml logs -f backend

# Error logs only
docker-compose -f deployment/docker/docker-compose.yml logs backend | grep ERROR
```

#### Access Logs

```bash
# Nginx access logs
tail -f /var/log/nginx/access.log

# Top IP addresses
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10
```

## Maintenance

### Regular Maintenance Tasks

#### Daily
- Monitor service health
- Check disk space
- Review error logs
- Verify backups

#### Weekly
- Update security patches
- Analyze performance metrics
- Clean up old logs
- Test backup restoration

#### Monthly
- Update dependencies
- Review security configuration
- Optimize database
- Update documentation

### Maintenance Mode

```bash
# Enable maintenance mode
echo "MAINTENANCE_MODE=true" >> .env
docker-compose -f deployment/docker/docker-compose.yml restart

# Disable maintenance mode
sed -i 's/MAINTENANCE_MODE=true/MAINTENANCE_MODE=false/' .env
docker-compose -f deployment/docker/docker-compose.yml restart
```

## Support and Documentation

### Getting Help

- **Documentation**: Check component README files
- **Logs**: Review application and system logs
- **Monitoring**: Use the monitoring dashboard
- **Community**: Check GitHub issues and discussions

### Useful Commands

```bash
# Service management
docker-compose -f deployment/docker/docker-compose.yml ps
docker-compose -f deployment/docker/docker-compose.yml restart
docker-compose -f deployment/docker/docker-compose.yml down
docker-compose -f deployment/docker/docker-compose.yml up -d

# Database management
docker exec -it ai-marketing-db psql -U marketing_user -d ai_marketing
docker exec ai-marketing-backend flask db upgrade

# Log management
docker-compose -f deployment/docker/docker-compose.yml logs -f
tail -f /var/log/ai-marketing-tools/application.log

# Backup and restore
./deployment/scripts/backup.sh
./deployment/scripts/restore.sh --backup=backup-name
```

---

*Deployment Guide v1.0*  
*Last Updated: January 27, 2025*  
*Next Review: April 27, 2025*

