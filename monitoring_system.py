#!/usr/bin/env python3
"""
AI Marketing Tools - Monitoring System
Real-time monitoring for platform health, performance, and alerts.
"""

import time
import requests
import psutil
import json
import logging
import smtplib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import sqlite3
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/logs/monitoring.log'),
        logging.StreamHandler()
    ]
)

class AIMarketingMonitoringSystem:
    """Comprehensive monitoring system for AI Marketing Tools platform"""
    
    def __init__(self, config_path: str = None):
        self.config = self.load_config(config_path)
        self.db_path = '/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/monitoring.db'
        self.init_database()
        self.alerts_sent = {}  # Track sent alerts to avoid spam
        
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load monitoring configuration"""
        default_config = {
            'api_base_url': 'http://localhost:5000',
            'web_app_url': 'http://localhost:5173',
            'mobile_app_url': 'http://localhost:19006',
            'check_interval': 60,  # seconds
            'alert_thresholds': {
                'response_time_ms': 5000,
                'error_rate_percent': 5.0,
                'cpu_usage_percent': 80.0,
                'memory_usage_percent': 85.0,
                'disk_usage_percent': 90.0,
                'uptime_percent': 99.0
            },
            'email_alerts': {
                'enabled': False,
                'smtp_server': 'smtp.gmail.com',
                'smtp_port': 587,
                'sender_email': 'alerts@ai-marketing-tools.com',
                'sender_password': 'your_password',
                'recipients': ['admin@ai-marketing-tools.com']
            },
            'services_to_monitor': [
                'backend_api',
                'web_app',
                'mobile_app',
                'database',
                'system_resources'
            ]
        }
        
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        
        return default_config
    
    def init_database(self):
        """Initialize SQLite database for monitoring data"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create monitoring_logs table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS monitoring_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    service_name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    response_time_ms INTEGER,
                    error_message TEXT,
                    metrics TEXT
                )
            ''')
            
            # Create alerts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    alert_type TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    message TEXT NOT NULL,
                    resolved BOOLEAN DEFAULT FALSE,
                    resolved_at DATETIME
                )
            ''')
            
            # Create system_metrics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS system_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    cpu_usage REAL,
                    memory_usage REAL,
                    disk_usage REAL,
                    network_io TEXT,
                    active_connections INTEGER
                )
            ''')
            
            conn.commit()
    
    def check_backend_api(self) -> Dict[str, Any]:
        """Monitor backend API health and performance"""
        service_name = 'backend_api'
        start_time = time.time()
        
        try:
            # Check health endpoint
            response = requests.get(
                f"{self.config['api_base_url']}/api/health",
                timeout=10
            )
            
            response_time = int((time.time() - start_time) * 1000)
            
            if response.status_code == 200:
                health_data = response.json()
                
                # Check individual API endpoints
                endpoints_status = {}
                for endpoint in ['/api/chat/analytics', '/api/plans', '/api/dashboard/overview']:
                    try:
                        ep_response = requests.get(f"{self.config['api_base_url']}{endpoint}", timeout=5)
                        endpoints_status[endpoint] = {
                            'status': ep_response.status_code,
                            'response_time': int((time.time() - start_time) * 1000)
                        }
                    except Exception as e:
                        endpoints_status[endpoint] = {'status': 'error', 'error': str(e)}
                
                return {
                    'service': service_name,
                    'status': 'healthy',
                    'response_time_ms': response_time,
                    'health_data': health_data,
                    'endpoints_status': endpoints_status
                }
            else:
                return {
                    'service': service_name,
                    'status': 'unhealthy',
                    'response_time_ms': response_time,
                    'error': f"HTTP {response.status_code}"
                }
                
        except requests.exceptions.RequestException as e:
            return {
                'service': service_name,
                'status': 'error',
                'response_time_ms': int((time.time() - start_time) * 1000),
                'error': str(e)
            }
    
    def check_web_app(self) -> Dict[str, Any]:
        """Monitor web application availability"""
        service_name = 'web_app'
        start_time = time.time()
        
        try:
            response = requests.get(self.config['web_app_url'], timeout=10)
            response_time = int((time.time() - start_time) * 1000)
            
            if response.status_code == 200:
                return {
                    'service': service_name,
                    'status': 'healthy',
                    'response_time_ms': response_time,
                    'content_length': len(response.content)
                }
            else:
                return {
                    'service': service_name,
                    'status': 'unhealthy',
                    'response_time_ms': response_time,
                    'error': f"HTTP {response.status_code}"
                }
                
        except requests.exceptions.RequestException as e:
            return {
                'service': service_name,
                'status': 'error',
                'response_time_ms': int((time.time() - start_time) * 1000),
                'error': str(e)
            }
    
    def check_mobile_app(self) -> Dict[str, Any]:
        """Monitor mobile application availability"""
        service_name = 'mobile_app'
        start_time = time.time()
        
        try:
            response = requests.get(self.config['mobile_app_url'], timeout=10)
            response_time = int((time.time() - start_time) * 1000)
            
            if response.status_code == 200:
                return {
                    'service': service_name,
                    'status': 'healthy',
                    'response_time_ms': response_time,
                    'content_length': len(response.content)
                }
            else:
                return {
                    'service': service_name,
                    'status': 'unhealthy',
                    'response_time_ms': response_time,
                    'error': f"HTTP {response.status_code}"
                }
                
        except requests.exceptions.RequestException as e:
            return {
                'service': service_name,
                'status': 'error',
                'response_time_ms': int((time.time() - start_time) * 1000),
                'error': str(e)
            }
    
    def check_database(self) -> Dict[str, Any]:
        """Monitor database connectivity and performance"""
        service_name = 'database'
        start_time = time.time()
        
        try:
            with sqlite3.connect(self.db_path, timeout=5) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM monitoring_logs")
                log_count = cursor.fetchone()[0]
                
                response_time = int((time.time() - start_time) * 1000)
                
                return {
                    'service': service_name,
                    'status': 'healthy',
                    'response_time_ms': response_time,
                    'log_count': log_count,
                    'database_size_mb': os.path.getsize(self.db_path) / (1024 * 1024)
                }
                
        except Exception as e:
            return {
                'service': service_name,
                'status': 'error',
                'response_time_ms': int((time.time() - start_time) * 1000),
                'error': str(e)
            }
    
    def check_system_resources(self) -> Dict[str, Any]:
        """Monitor system resources (CPU, memory, disk)"""
        service_name = 'system_resources'
        
        try:
            # CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            
            # Disk usage
            disk = psutil.disk_usage('/')
            disk_usage = (disk.used / disk.total) * 100
            
            # Network I/O
            network = psutil.net_io_counters()
            
            # Active connections
            connections = len(psutil.net_connections())
            
            return {
                'service': service_name,
                'status': 'healthy',
                'cpu_usage': cpu_usage,
                'memory_usage': memory_usage,
                'disk_usage': disk_usage,
                'network_io': {
                    'bytes_sent': network.bytes_sent,
                    'bytes_recv': network.bytes_recv,
                    'packets_sent': network.packets_sent,
                    'packets_recv': network.packets_recv
                },
                'active_connections': connections
            }
            
        except Exception as e:
            return {
                'service': service_name,
                'status': 'error',
                'error': str(e)
            }
    
    def log_monitoring_result(self, result: Dict[str, Any]):
        """Log monitoring result to database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO monitoring_logs 
                    (service_name, status, response_time_ms, error_message, metrics)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    result['service'],
                    result['status'],
                    result.get('response_time_ms'),
                    result.get('error'),
                    json.dumps(result)
                ))
                
                conn.commit()
                
        except Exception as e:
            logging.error(f"Failed to log monitoring result: {e}")
    
    def log_system_metrics(self, metrics: Dict[str, Any]):
        """Log system metrics to database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO system_metrics 
                    (cpu_usage, memory_usage, disk_usage, network_io, active_connections)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    metrics.get('cpu_usage'),
                    metrics.get('memory_usage'),
                    metrics.get('disk_usage'),
                    json.dumps(metrics.get('network_io', {})),
                    metrics.get('active_connections')
                ))
                
                conn.commit()
                
        except Exception as e:
            logging.error(f"Failed to log system metrics: {e}")
    
    def check_alert_conditions(self, result: Dict[str, Any]):
        """Check if monitoring result triggers any alerts"""
        alerts = []
        thresholds = self.config['alert_thresholds']
        
        # Response time alert
        if result.get('response_time_ms', 0) > thresholds['response_time_ms']:
            alerts.append({
                'type': 'high_response_time',
                'severity': 'warning',
                'message': f"{result['service']} response time {result['response_time_ms']}ms exceeds threshold {thresholds['response_time_ms']}ms"
            })
        
        # Service down alert
        if result['status'] in ['error', 'unhealthy']:
            alerts.append({
                'type': 'service_down',
                'severity': 'critical',
                'message': f"{result['service']} is {result['status']}: {result.get('error', 'Unknown error')}"
            })
        
        # System resource alerts
        if result['service'] == 'system_resources':
            if result.get('cpu_usage', 0) > thresholds['cpu_usage_percent']:
                alerts.append({
                    'type': 'high_cpu_usage',
                    'severity': 'warning',
                    'message': f"CPU usage {result['cpu_usage']:.1f}% exceeds threshold {thresholds['cpu_usage_percent']}%"
                })
            
            if result.get('memory_usage', 0) > thresholds['memory_usage_percent']:
                alerts.append({
                    'type': 'high_memory_usage',
                    'severity': 'warning',
                    'message': f"Memory usage {result['memory_usage']:.1f}% exceeds threshold {thresholds['memory_usage_percent']}%"
                })
            
            if result.get('disk_usage', 0) > thresholds['disk_usage_percent']:
                alerts.append({
                    'type': 'high_disk_usage',
                    'severity': 'critical',
                    'message': f"Disk usage {result['disk_usage']:.1f}% exceeds threshold {thresholds['disk_usage_percent']}%"
                })
        
        return alerts
    
    def send_alert(self, alert: Dict[str, Any]):
        """Send alert notification"""
        # Log alert to database
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO alerts (alert_type, severity, message)
                    VALUES (?, ?, ?)
                ''', (alert['type'], alert['severity'], alert['message']))
                conn.commit()
        except Exception as e:
            logging.error(f"Failed to log alert: {e}")
        
        # Log alert
        logging.warning(f"ALERT [{alert['severity'].upper()}]: {alert['message']}")
        
        # Send email alert if configured
        if self.config['email_alerts']['enabled']:
            self.send_email_alert(alert)
        
        # Track sent alerts to avoid spam
        alert_key = f"{alert['type']}_{alert['message']}"
        self.alerts_sent[alert_key] = datetime.now()
    
    def send_email_alert(self, alert: Dict[str, Any]):
        """Send email alert notification"""
        try:
            email_config = self.config['email_alerts']
            
            msg = MIMEMultipart()
            msg['From'] = email_config['sender_email']
            msg['To'] = ', '.join(email_config['recipients'])
            msg['Subject'] = f"AI Marketing Tools Alert - {alert['severity'].upper()}"
            
            body = f"""
            Alert Details:
            
            Type: {alert['type']}
            Severity: {alert['severity']}
            Message: {alert['message']}
            Timestamp: {datetime.now().isoformat()}
            
            Please investigate and resolve this issue.
            
            AI Marketing Tools Monitoring System
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
            server.starttls()
            server.login(email_config['sender_email'], email_config['sender_password'])
            
            text = msg.as_string()
            server.sendmail(email_config['sender_email'], email_config['recipients'], text)
            server.quit()
            
            logging.info(f"Email alert sent for {alert['type']}")
            
        except Exception as e:
            logging.error(f"Failed to send email alert: {e}")
    
    def run_monitoring_cycle(self):
        """Run one complete monitoring cycle"""
        logging.info("Starting monitoring cycle...")
        
        # Define monitoring functions
        monitoring_functions = {
            'backend_api': self.check_backend_api,
            'web_app': self.check_web_app,
            'mobile_app': self.check_mobile_app,
            'database': self.check_database,
            'system_resources': self.check_system_resources
        }
        
        results = []
        
        for service in self.config['services_to_monitor']:
            if service in monitoring_functions:
                try:
                    result = monitoring_functions[service]()
                    results.append(result)
                    
                    # Log result
                    self.log_monitoring_result(result)
                    
                    # Log system metrics separately
                    if service == 'system_resources':
                        self.log_system_metrics(result)
                    
                    # Check for alerts
                    alerts = self.check_alert_conditions(result)
                    for alert in alerts:
                        self.send_alert(alert)
                    
                    # Log status
                    status_emoji = "✅" if result['status'] == 'healthy' else "❌"
                    logging.info(f"{status_emoji} {service}: {result['status']}")
                    
                except Exception as e:
                    logging.error(f"Error monitoring {service}: {e}")
        
        logging.info(f"Monitoring cycle completed. Checked {len(results)} services.")
        return results
    
    def start_continuous_monitoring(self):
        """Start continuous monitoring in background thread"""
        def monitoring_loop():
            while True:
                try:
                    self.run_monitoring_cycle()
                    time.sleep(self.config['check_interval'])
                except KeyboardInterrupt:
                    logging.info("Monitoring stopped by user")
                    break
                except Exception as e:
                    logging.error(f"Error in monitoring loop: {e}")
                    time.sleep(30)  # Wait before retrying
        
        monitoring_thread = threading.Thread(target=monitoring_loop, daemon=True)
        monitoring_thread.start()
        logging.info(f"Continuous monitoring started (interval: {self.config['check_interval']}s)")
        
        return monitoring_thread
    
    def generate_monitoring_report(self, hours: int = 24) -> Dict[str, Any]:
        """Generate monitoring report for the last N hours"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get monitoring data
                cursor.execute('''
                    SELECT service_name, status, COUNT(*) as count,
                           AVG(response_time_ms) as avg_response_time
                    FROM monitoring_logs 
                    WHERE timestamp > datetime('now', '-{} hours')
                    GROUP BY service_name, status
                '''.format(hours))
                
                monitoring_data = cursor.fetchall()
                
                # Get alerts
                cursor.execute('''
                    SELECT alert_type, severity, COUNT(*) as count
                    FROM alerts 
                    WHERE timestamp > datetime('now', '-{} hours')
                    GROUP BY alert_type, severity
                '''.format(hours))
                
                alerts_data = cursor.fetchall()
                
                # Get system metrics
                cursor.execute('''
                    SELECT AVG(cpu_usage) as avg_cpu,
                           AVG(memory_usage) as avg_memory,
                           AVG(disk_usage) as avg_disk,
                           MAX(cpu_usage) as max_cpu,
                           MAX(memory_usage) as max_memory
                    FROM system_metrics 
                    WHERE timestamp > datetime('now', '-{} hours')
                '''.format(hours))
                
                system_data = cursor.fetchone()
                
                report = {
                    'report_period_hours': hours,
                    'generated_at': datetime.now().isoformat(),
                    'monitoring_summary': [
                        {
                            'service': row[0],
                            'status': row[1],
                            'count': row[2],
                            'avg_response_time_ms': row[3]
                        }
                        for row in monitoring_data
                    ],
                    'alerts_summary': [
                        {
                            'type': row[0],
                            'severity': row[1],
                            'count': row[2]
                        }
                        for row in alerts_data
                    ],
                    'system_metrics': {
                        'avg_cpu_usage': system_data[0] if system_data[0] else 0,
                        'avg_memory_usage': system_data[1] if system_data[1] else 0,
                        'avg_disk_usage': system_data[2] if system_data[2] else 0,
                        'max_cpu_usage': system_data[3] if system_data[3] else 0,
                        'max_memory_usage': system_data[4] if system_data[4] else 0
                    }
                }
                
                return report
                
        except Exception as e:
            logging.error(f"Error generating monitoring report: {e}")
            return {'error': str(e)}

def main():
    """Main function to run monitoring system"""
    # Create logs directory
    os.makedirs('/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/logs', exist_ok=True)
    
    # Initialize monitoring system
    monitor = AIMarketingMonitoringSystem()
    
    print("🔍 AI Marketing Tools Monitoring System")
    print("=====================================")
    
    # Run initial monitoring cycle
    print("Running initial monitoring cycle...")
    results = monitor.run_monitoring_cycle()
    
    # Generate and save report
    print("\nGenerating monitoring report...")
    report = monitor.generate_monitoring_report(24)
    
    report_path = '/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/reports/monitoring_report.json'
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📊 Monitoring report saved to: {report_path}")
    
    # Start continuous monitoring
    print(f"\n🚀 Starting continuous monitoring (interval: {monitor.config['check_interval']}s)")
    print("Press Ctrl+C to stop monitoring")
    
    monitoring_thread = monitor.start_continuous_monitoring()
    
    try:
        # Keep main thread alive
        while monitoring_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Monitoring stopped by user")

if __name__ == "__main__":
    main()

