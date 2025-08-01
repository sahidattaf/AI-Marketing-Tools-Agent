# AI Marketing Tools - Analytics & Monitoring System

This directory contains the complete analytics and monitoring infrastructure for the AI Marketing Tools platform, providing real-time insights, performance tracking, and automated alerting.

## Directory Structure

```
analytics-monitoring/
├── dashboards/                    # Interactive analytics dashboards
│   ├── analytics_dashboard.py     # Main analytics dashboard generator
│   ├── overview_dashboard.html    # Platform overview dashboard
│   ├── chatbot_dashboard.html     # Chatbot analytics dashboard
│   └── revenue_dashboard.html     # Revenue and business metrics
├── scripts/                       # Monitoring and analysis scripts
│   ├── monitoring_system.py       # Real-time monitoring system
│   └── performance_analyzer.py    # Advanced performance analysis
├── reports/                       # Generated reports and analysis
│   ├── executive_summary.json     # Executive summary report
│   ├── monitoring_report.json     # Monitoring status report
│   ├── performance_analysis_report.json  # Performance analysis
│   └── performance_analysis.png   # Performance visualization
├── config/                        # Configuration files
│   └── monitoring_config.json     # Monitoring system configuration
├── logs/                          # System logs
│   └── monitoring.log             # Monitoring system logs
├── monitoring.db                  # SQLite database for metrics
└── README.md                      # This file
```

## Features

### 📊 Analytics Dashboards

#### Overview Dashboard
- **Key Metrics**: Total users, daily active users, conversion rates
- **Traffic Analysis**: Sources, language distribution, top pages
- **User Engagement**: Session duration, bounce rate, page views
- **Performance Indicators**: Real-time system health metrics

#### Chatbot Analytics
- **Conversation Metrics**: Volume, satisfaction scores, resolution rates
- **Topic Analysis**: Popular topics, language usage patterns
- **Performance Tracking**: Response times, hourly distribution
- **User Satisfaction**: Ratings and feedback analysis

#### Revenue Dashboard
- **Financial Metrics**: MRR, ARR, churn rate, ARPU
- **Plan Distribution**: Subscription tier analysis
- **Billing Preferences**: Monthly vs yearly subscriptions
- **Revenue Trends**: Historical performance and projections

### 🔍 Monitoring System

#### Real-Time Monitoring
- **Service Health**: Backend API, web app, mobile app availability
- **Performance Tracking**: Response times, error rates, uptime
- **System Resources**: CPU, memory, disk usage monitoring
- **Database Health**: Connectivity and performance metrics

#### Alerting System
- **Threshold-Based Alerts**: Configurable performance thresholds
- **Email Notifications**: Automated alert delivery (configurable)
- **Alert Escalation**: Priority-based notification rules
- **Alert Tracking**: Historical alert logs and resolution tracking

#### Performance Analysis
- **Response Time Analysis**: Trends, anomalies, service comparisons
- **Availability Analysis**: Uptime calculations, downtime incidents
- **Resource Usage**: System performance patterns and optimization
- **Optimization Recommendations**: Automated performance suggestions

## Configuration

### Monitoring Configuration (`config/monitoring_config.json`)

```json
{
  "api_base_url": "http://localhost:5000",
  "web_app_url": "http://localhost:5173",
  "mobile_app_url": "http://localhost:19006",
  "check_interval": 60,
  "alert_thresholds": {
    "response_time_ms": 5000,
    "error_rate_percent": 5.0,
    "cpu_usage_percent": 80.0,
    "memory_usage_percent": 85.0,
    "disk_usage_percent": 90.0,
    "uptime_percent": 99.0
  },
  "email_alerts": {
    "enabled": false,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "alerts@ai-marketing-tools.com",
    "recipients": ["admin@ai-marketing-tools.com"]
  }
}
```

### Alert Thresholds
- **Response Time**: 5000ms (5 seconds)
- **Error Rate**: 5.0%
- **CPU Usage**: 80.0%
- **Memory Usage**: 85.0%
- **Disk Usage**: 90.0%
- **Uptime Target**: 99.0%

## Usage

### Running Analytics Dashboards

```bash
# Generate all analytics dashboards
cd analytics-monitoring/dashboards
python3 analytics_dashboard.py

# View dashboards in browser
# Open the generated HTML files in your web browser
```

### Starting Monitoring System

```bash
# Run monitoring system
cd analytics-monitoring/scripts
python3 monitoring_system.py

# Run in background (continuous monitoring)
nohup python3 monitoring_system.py &
```

### Performance Analysis

```bash
# Run performance analysis
cd analytics-monitoring/scripts
python3 performance_analyzer.py

# Analyze specific time period (hours)
python3 -c "
from performance_analyzer import PerformanceAnalyzer
analyzer = PerformanceAnalyzer()
report = analyzer.run_full_analysis(hours=24)  # Last 24 hours
"
```

## Key Metrics Tracked

### Business Metrics
- **User Acquisition**: Total users, daily/monthly active users
- **Conversion Metrics**: Free-to-paid conversion rates, trial conversions
- **Revenue Metrics**: MRR, ARR, ARPU, churn rate
- **Engagement Metrics**: Session duration, page views, feature usage

### Technical Metrics
- **Performance**: Response times, page load times, API latency
- **Reliability**: Uptime, error rates, incident frequency
- **Scalability**: Resource usage, concurrent users, throughput
- **Quality**: User satisfaction, bug reports, feature adoption

### Chatbot Metrics
- **Usage**: Conversation volume, message frequency
- **Performance**: Response times, resolution rates
- **Quality**: User satisfaction scores, topic coverage
- **Efficiency**: Automation rate, escalation frequency

## Database Schema

### Monitoring Logs Table
```sql
CREATE TABLE monitoring_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    service_name TEXT NOT NULL,
    status TEXT NOT NULL,
    response_time_ms INTEGER,
    error_message TEXT,
    metrics TEXT
);
```

### Alerts Table
```sql
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    alert_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    message TEXT NOT NULL,
    resolved BOOLEAN DEFAULT FALSE,
    resolved_at DATETIME
);
```

### System Metrics Table
```sql
CREATE TABLE system_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    cpu_usage REAL,
    memory_usage REAL,
    disk_usage REAL,
    network_io TEXT,
    active_connections INTEGER
);
```

## API Endpoints Monitored

### Backend API Endpoints
- `GET /api/health` - Service health check
- `GET /api/chat/analytics` - Chatbot analytics
- `GET /api/plans` - Pricing plans
- `GET /api/dashboard/overview` - Dashboard data
- `GET /api/analytics/revenue` - Revenue analytics

### Application Endpoints
- **Web App**: `http://localhost:5173/`
- **Mobile App**: `http://localhost:19006/`
- **Backend API**: `http://localhost:5000/`

## Alerting Rules

### Critical Alerts (Immediate Notification)
- Service downtime or errors
- Response time > 5 seconds
- Disk usage > 90%
- System uptime < 99%

### Warning Alerts (Escalated if Persistent)
- High CPU usage (> 80%)
- High memory usage (> 85%)
- Response time > 2 seconds
- Error rate > 1%

### Information Alerts (Logged Only)
- Performance degradation trends
- Resource usage patterns
- User behavior anomalies

## Troubleshooting

### Common Issues

#### Monitoring System Not Starting
```bash
# Check dependencies
pip3 install psutil requests pandas matplotlib seaborn plotly

# Check database permissions
ls -la analytics-monitoring/monitoring.db

# Check log files
tail -f analytics-monitoring/logs/monitoring.log
```

#### Dashboard Generation Errors
```bash
# Verify Python packages
pip3 install plotly pandas numpy matplotlib seaborn

# Check data availability
sqlite3 analytics-monitoring/monitoring.db "SELECT COUNT(*) FROM monitoring_logs;"
```

#### High Resource Usage Alerts
```bash
# Check system resources
top
df -h
free -m

# Review application logs
tail -f analytics-monitoring/logs/monitoring.log
```

## Performance Optimization

### Database Optimization
- Regular cleanup of old monitoring data
- Index optimization for query performance
- Database vacuum operations

### Monitoring Efficiency
- Adjustable check intervals based on criticality
- Intelligent alerting to reduce noise
- Batch processing for large datasets

### Dashboard Performance
- Cached data for faster loading
- Optimized queries for large datasets
- Progressive loading for complex visualizations

## Security Considerations

### Data Protection
- Sensitive data encryption in database
- Secure API endpoint monitoring
- Access control for monitoring dashboards

### Alert Security
- Secure email configuration for alerts
- Rate limiting for alert notifications
- Audit trail for monitoring access

## Maintenance

### Regular Tasks
- **Daily**: Review monitoring alerts and system health
- **Weekly**: Analyze performance trends and optimization opportunities
- **Monthly**: Update monitoring thresholds and alert rules
- **Quarterly**: Review and optimize monitoring infrastructure

### Data Retention
- **Monitoring Logs**: 30 days
- **System Metrics**: 90 days
- **Alert History**: 1 year
- **Performance Reports**: Permanent

## Integration

### External Services
- **Email Alerts**: SMTP integration for notifications
- **Slack/Teams**: Webhook integration for team alerts
- **PagerDuty**: Incident management integration
- **Grafana**: Advanced visualization integration

### API Integration
- RESTful API for external monitoring tools
- Webhook support for real-time notifications
- Export capabilities for external analysis

## Support

For questions or issues with the analytics and monitoring system:

- **Documentation**: This README and inline code comments
- **Logs**: Check `analytics-monitoring/logs/monitoring.log`
- **Database**: Query `analytics-monitoring/monitoring.db` for historical data
- **Configuration**: Review `config/monitoring_config.json`

---

*Analytics & Monitoring System v1.0*  
*Last Updated: January 27, 2025*  
*Next Review: April 27, 2025*

