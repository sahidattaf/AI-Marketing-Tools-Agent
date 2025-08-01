#!/usr/bin/env python3
"""
AI Marketing Tools - Performance Analyzer
Advanced performance analysis and optimization recommendations.
"""

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
import os
from typing import Dict, List, Any, Tuple
import warnings
warnings.filterwarnings('ignore')

class PerformanceAnalyzer:
    """Advanced performance analysis for AI Marketing Tools platform"""
    
    def __init__(self, db_path: str = None):
        self.db_path = db_path or '/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/monitoring.db'
        self.output_dir = '/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/reports'
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_monitoring_data(self, hours: int = 168) -> pd.DataFrame:
        """Load monitoring data from database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                query = '''
                    SELECT * FROM monitoring_logs 
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp
                '''.format(hours)
                
                df = pd.read_sql_query(query, conn)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df
                
        except Exception as e:
            print(f"Error loading monitoring data: {e}")
            return pd.DataFrame()
    
    def load_system_metrics(self, hours: int = 168) -> pd.DataFrame:
        """Load system metrics from database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                query = '''
                    SELECT * FROM system_metrics 
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp
                '''.format(hours)
                
                df = pd.read_sql_query(query, conn)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df
                
        except Exception as e:
            print(f"Error loading system metrics: {e}")
            return pd.DataFrame()
    
    def analyze_response_times(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze response time patterns and trends"""
        if df.empty:
            return {'error': 'No data available'}
        
        # Filter out null response times
        df_filtered = df[df['response_time_ms'].notna()]
        
        if df_filtered.empty:
            return {'error': 'No response time data available'}
        
        analysis = {
            'overall_stats': {
                'mean': df_filtered['response_time_ms'].mean(),
                'median': df_filtered['response_time_ms'].median(),
                'p95': df_filtered['response_time_ms'].quantile(0.95),
                'p99': df_filtered['response_time_ms'].quantile(0.99),
                'std': df_filtered['response_time_ms'].std(),
                'min': df_filtered['response_time_ms'].min(),
                'max': df_filtered['response_time_ms'].max()
            },
            'by_service': {},
            'trends': {},
            'anomalies': []
        }
        
        # Analysis by service
        for service in df_filtered['service_name'].unique():
            service_data = df_filtered[df_filtered['service_name'] == service]['response_time_ms']
            analysis['by_service'][service] = {
                'mean': service_data.mean(),
                'median': service_data.median(),
                'p95': service_data.quantile(0.95),
                'count': len(service_data)
            }
        
        # Trend analysis (hourly averages)
        df_filtered['hour'] = df_filtered['timestamp'].dt.floor('H')
        hourly_avg = df_filtered.groupby('hour')['response_time_ms'].mean()
        
        if len(hourly_avg) > 1:
            # Calculate trend slope
            x = np.arange(len(hourly_avg))
            y = hourly_avg.values
            slope = np.polyfit(x, y, 1)[0]
            
            analysis['trends'] = {
                'hourly_average': hourly_avg.to_dict(),
                'trend_slope': slope,
                'trend_direction': 'improving' if slope < 0 else 'degrading' if slope > 0 else 'stable'
            }
        
        # Detect anomalies (values > 2 standard deviations from mean)
        mean_rt = analysis['overall_stats']['mean']
        std_rt = analysis['overall_stats']['std']
        threshold = mean_rt + (2 * std_rt)
        
        anomalies = df_filtered[df_filtered['response_time_ms'] > threshold]
        analysis['anomalies'] = [
            {
                'timestamp': row['timestamp'].isoformat(),
                'service': row['service_name'],
                'response_time_ms': row['response_time_ms'],
                'deviation_factor': (row['response_time_ms'] - mean_rt) / std_rt
            }
            for _, row in anomalies.iterrows()
        ]
        
        return analysis
    
    def analyze_availability(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze service availability and uptime"""
        if df.empty:
            return {'error': 'No data available'}
        
        analysis = {
            'overall_uptime': {},
            'by_service': {},
            'downtime_incidents': [],
            'mttr': {}  # Mean Time To Recovery
        }
        
        # Overall uptime calculation
        total_checks = len(df)
        healthy_checks = len(df[df['status'] == 'healthy'])
        overall_uptime = (healthy_checks / total_checks) * 100 if total_checks > 0 else 0
        
        analysis['overall_uptime'] = {
            'percentage': overall_uptime,
            'total_checks': total_checks,
            'healthy_checks': healthy_checks,
            'failed_checks': total_checks - healthy_checks
        }
        
        # Uptime by service
        for service in df['service_name'].unique():
            service_data = df[df['service_name'] == service]
            service_total = len(service_data)
            service_healthy = len(service_data[service_data['status'] == 'healthy'])
            service_uptime = (service_healthy / service_total) * 100 if service_total > 0 else 0
            
            analysis['by_service'][service] = {
                'uptime_percentage': service_uptime,
                'total_checks': service_total,
                'healthy_checks': service_healthy,
                'failed_checks': service_total - service_healthy
            }
        
        # Identify downtime incidents
        df_sorted = df.sort_values(['service_name', 'timestamp'])
        
        for service in df['service_name'].unique():
            service_data = df_sorted[df_sorted['service_name'] == service]
            
            # Find consecutive failures
            service_data['is_down'] = service_data['status'] != 'healthy'
            service_data['incident_group'] = (service_data['is_down'] != service_data['is_down'].shift()).cumsum()
            
            incidents = service_data[service_data['is_down']].groupby('incident_group').agg({
                'timestamp': ['min', 'max', 'count'],
                'status': 'first',
                'error_message': 'first'
            }).reset_index()
            
            for _, incident in incidents.iterrows():
                start_time = incident[('timestamp', 'min')]
                end_time = incident[('timestamp', 'max')]
                duration_minutes = (end_time - start_time).total_seconds() / 60
                
                analysis['downtime_incidents'].append({
                    'service': service,
                    'start_time': start_time.isoformat(),
                    'end_time': end_time.isoformat(),
                    'duration_minutes': duration_minutes,
                    'status': incident[('status', 'first')],
                    'error': incident[('error_message', 'first')]
                })
        
        return analysis
    
    def analyze_system_performance(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze system resource usage patterns"""
        if df.empty:
            return {'error': 'No system metrics data available'}
        
        analysis = {
            'cpu_analysis': {},
            'memory_analysis': {},
            'disk_analysis': {},
            'resource_correlations': {},
            'peak_usage_times': {}
        }
        
        # CPU Analysis
        if 'cpu_usage' in df.columns:
            cpu_data = df['cpu_usage'].dropna()
            analysis['cpu_analysis'] = {
                'average': cpu_data.mean(),
                'peak': cpu_data.max(),
                'p95': cpu_data.quantile(0.95),
                'std': cpu_data.std(),
                'above_80_percent': len(cpu_data[cpu_data > 80]) / len(cpu_data) * 100
            }
        
        # Memory Analysis
        if 'memory_usage' in df.columns:
            memory_data = df['memory_usage'].dropna()
            analysis['memory_analysis'] = {
                'average': memory_data.mean(),
                'peak': memory_data.max(),
                'p95': memory_data.quantile(0.95),
                'std': memory_data.std(),
                'above_85_percent': len(memory_data[memory_data > 85]) / len(memory_data) * 100
            }
        
        # Disk Analysis
        if 'disk_usage' in df.columns:
            disk_data = df['disk_usage'].dropna()
            analysis['disk_analysis'] = {
                'average': disk_data.mean(),
                'peak': disk_data.max(),
                'p95': disk_data.quantile(0.95),
                'std': disk_data.std(),
                'above_90_percent': len(disk_data[disk_data > 90]) / len(disk_data) * 100
            }
        
        # Resource correlations
        numeric_cols = ['cpu_usage', 'memory_usage', 'disk_usage']
        available_cols = [col for col in numeric_cols if col in df.columns]
        
        if len(available_cols) > 1:
            correlation_matrix = df[available_cols].corr()
            analysis['resource_correlations'] = correlation_matrix.to_dict()
        
        # Peak usage times
        if 'cpu_usage' in df.columns:
            df['hour'] = df['timestamp'].dt.hour
            hourly_cpu = df.groupby('hour')['cpu_usage'].mean()
            peak_hour = hourly_cpu.idxmax()
            analysis['peak_usage_times']['cpu_peak_hour'] = int(peak_hour)
            analysis['peak_usage_times']['hourly_cpu_avg'] = hourly_cpu.to_dict()
        
        return analysis
    
    def generate_optimization_recommendations(self, 
                                            response_analysis: Dict[str, Any],
                                            availability_analysis: Dict[str, Any],
                                            system_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate optimization recommendations based on analysis"""
        recommendations = []
        
        # Response time recommendations
        if 'overall_stats' in response_analysis:
            mean_rt = response_analysis['overall_stats']['mean']
            p95_rt = response_analysis['overall_stats']['p95']
            
            if mean_rt > 1000:  # > 1 second
                recommendations.append({
                    'category': 'Performance',
                    'priority': 'High',
                    'issue': f'High average response time ({mean_rt:.0f}ms)',
                    'recommendation': 'Optimize database queries, implement caching, or scale infrastructure',
                    'impact': 'User experience improvement'
                })
            
            if p95_rt > 5000:  # > 5 seconds
                recommendations.append({
                    'category': 'Performance',
                    'priority': 'Critical',
                    'issue': f'Very high P95 response time ({p95_rt:.0f}ms)',
                    'recommendation': 'Investigate slow queries, add load balancing, or increase server capacity',
                    'impact': 'Prevent user abandonment'
                })
        
        # Availability recommendations
        if 'overall_uptime' in availability_analysis:
            uptime = availability_analysis['overall_uptime']['percentage']
            
            if uptime < 99.0:
                recommendations.append({
                    'category': 'Reliability',
                    'priority': 'Critical',
                    'issue': f'Low uptime ({uptime:.2f}%)',
                    'recommendation': 'Implement redundancy, improve error handling, and add health checks',
                    'impact': 'Business continuity'
                })
            elif uptime < 99.9:
                recommendations.append({
                    'category': 'Reliability',
                    'priority': 'High',
                    'issue': f'Uptime below target ({uptime:.2f}%)',
                    'recommendation': 'Review and strengthen monitoring, implement auto-recovery mechanisms',
                    'impact': 'Service reliability'
                })
        
        # System resource recommendations
        if 'cpu_analysis' in system_analysis and system_analysis['cpu_analysis']:
            cpu_avg = system_analysis['cpu_analysis'].get('average', 0)
            cpu_peak = system_analysis['cpu_analysis'].get('peak', 0)
            
            if cpu_avg > 70:
                recommendations.append({
                    'category': 'Infrastructure',
                    'priority': 'High',
                    'issue': f'High average CPU usage ({cpu_avg:.1f}%)',
                    'recommendation': 'Scale up CPU resources or optimize application code',
                    'impact': 'System stability and performance'
                })
            
            if cpu_peak > 95:
                recommendations.append({
                    'category': 'Infrastructure',
                    'priority': 'Medium',
                    'issue': f'CPU spikes detected ({cpu_peak:.1f}%)',
                    'recommendation': 'Implement CPU throttling or add auto-scaling',
                    'impact': 'Prevent system overload'
                })
        
        if 'memory_analysis' in system_analysis and system_analysis['memory_analysis']:
            memory_avg = system_analysis['memory_analysis'].get('average', 0)
            
            if memory_avg > 80:
                recommendations.append({
                    'category': 'Infrastructure',
                    'priority': 'High',
                    'issue': f'High memory usage ({memory_avg:.1f}%)',
                    'recommendation': 'Increase RAM or optimize memory usage in applications',
                    'impact': 'Prevent out-of-memory errors'
                })
        
        # Anomaly recommendations
        if 'anomalies' in response_analysis and response_analysis['anomalies']:
            anomaly_count = len(response_analysis['anomalies'])
            if anomaly_count > 10:
                recommendations.append({
                    'category': 'Monitoring',
                    'priority': 'Medium',
                    'issue': f'Multiple response time anomalies detected ({anomaly_count})',
                    'recommendation': 'Investigate root causes and implement alerting for anomalies',
                    'impact': 'Early problem detection'
                })
        
        return recommendations
    
    def create_performance_visualizations(self, 
                                        monitoring_df: pd.DataFrame, 
                                        system_df: pd.DataFrame):
        """Create performance visualization charts"""
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('AI Marketing Tools - Performance Analysis', fontsize=16, fontweight='bold')
        
        # Response time trends
        if not monitoring_df.empty and 'response_time_ms' in monitoring_df.columns:
            monitoring_df_clean = monitoring_df[monitoring_df['response_time_ms'].notna()]
            if not monitoring_df_clean.empty:
                for service in monitoring_df_clean['service_name'].unique():
                    service_data = monitoring_df_clean[monitoring_df_clean['service_name'] == service]
                    axes[0, 0].plot(service_data['timestamp'], service_data['response_time_ms'], 
                                  label=service, alpha=0.7)
                
                axes[0, 0].set_title('Response Time Trends by Service')
                axes[0, 0].set_xlabel('Time')
                axes[0, 0].set_ylabel('Response Time (ms)')
                axes[0, 0].legend()
                axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Service availability
        if not monitoring_df.empty:
            availability_data = monitoring_df.groupby('service_name')['status'].apply(
                lambda x: (x == 'healthy').sum() / len(x) * 100
            )
            
            axes[0, 1].bar(availability_data.index, availability_data.values, 
                          color=['green' if x > 99 else 'orange' if x > 95 else 'red' for x in availability_data.values])
            axes[0, 1].set_title('Service Availability (%)')
            axes[0, 1].set_ylabel('Uptime Percentage')
            axes[0, 1].tick_params(axis='x', rotation=45)
            axes[0, 1].axhline(y=99, color='red', linestyle='--', alpha=0.7, label='Target (99%)')
            axes[0, 1].legend()
        
        # System resource usage
        if not system_df.empty:
            if 'cpu_usage' in system_df.columns:
                axes[1, 0].plot(system_df['timestamp'], system_df['cpu_usage'], 
                              label='CPU', color='blue', alpha=0.7)
            if 'memory_usage' in system_df.columns:
                axes[1, 0].plot(system_df['timestamp'], system_df['memory_usage'], 
                              label='Memory', color='red', alpha=0.7)
            if 'disk_usage' in system_df.columns:
                axes[1, 0].plot(system_df['timestamp'], system_df['disk_usage'], 
                              label='Disk', color='green', alpha=0.7)
            
            axes[1, 0].set_title('System Resource Usage')
            axes[1, 0].set_xlabel('Time')
            axes[1, 0].set_ylabel('Usage (%)')
            axes[1, 0].legend()
            axes[1, 0].tick_params(axis='x', rotation=45)
            axes[1, 0].axhline(y=80, color='orange', linestyle='--', alpha=0.5, label='Warning (80%)')
            axes[1, 0].axhline(y=90, color='red', linestyle='--', alpha=0.5, label='Critical (90%)')
        
        # Response time distribution
        if not monitoring_df.empty and 'response_time_ms' in monitoring_df.columns:
            monitoring_df_clean = monitoring_df[monitoring_df['response_time_ms'].notna()]
            if not monitoring_df_clean.empty:
                axes[1, 1].hist(monitoring_df_clean['response_time_ms'], bins=30, 
                              alpha=0.7, color='skyblue', edgecolor='black')
                axes[1, 1].set_title('Response Time Distribution')
                axes[1, 1].set_xlabel('Response Time (ms)')
                axes[1, 1].set_ylabel('Frequency')
                
                # Add mean and P95 lines
                mean_rt = monitoring_df_clean['response_time_ms'].mean()
                p95_rt = monitoring_df_clean['response_time_ms'].quantile(0.95)
                axes[1, 1].axvline(mean_rt, color='red', linestyle='--', label=f'Mean ({mean_rt:.0f}ms)')
                axes[1, 1].axvline(p95_rt, color='orange', linestyle='--', label=f'P95 ({p95_rt:.0f}ms)')
                axes[1, 1].legend()
        
        plt.tight_layout()
        
        # Save the plot
        plot_path = os.path.join(self.output_dir, 'performance_analysis.png')
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return plot_path
    
    def run_full_analysis(self, hours: int = 168) -> Dict[str, Any]:
        """Run complete performance analysis"""
        print(f"🔍 Running performance analysis for the last {hours} hours...")
        
        # Load data
        monitoring_df = self.load_monitoring_data(hours)
        system_df = self.load_system_metrics(hours)
        
        print(f"📊 Loaded {len(monitoring_df)} monitoring records and {len(system_df)} system metrics")
        
        # Run analyses
        response_analysis = self.analyze_response_times(monitoring_df)
        availability_analysis = self.analyze_availability(monitoring_df)
        system_analysis = self.analyze_system_performance(system_df)
        
        # Generate recommendations
        recommendations = self.generate_optimization_recommendations(
            response_analysis, availability_analysis, system_analysis
        )
        
        # Create visualizations
        plot_path = self.create_performance_visualizations(monitoring_df, system_df)
        
        # Compile full report
        full_report = {
            'analysis_period_hours': hours,
            'generated_at': datetime.now().isoformat(),
            'data_summary': {
                'monitoring_records': len(monitoring_df),
                'system_metrics_records': len(system_df),
                'services_analyzed': monitoring_df['service_name'].nunique() if not monitoring_df.empty else 0
            },
            'response_time_analysis': response_analysis,
            'availability_analysis': availability_analysis,
            'system_performance_analysis': system_analysis,
            'optimization_recommendations': recommendations,
            'visualization_path': plot_path
        }
        
        # Save report
        report_path = os.path.join(self.output_dir, 'performance_analysis_report.json')
        with open(report_path, 'w') as f:
            json.dump(full_report, f, indent=2, default=str)
        
        print(f"✅ Performance analysis completed!")
        print(f"📊 Report saved to: {report_path}")
        print(f"📈 Visualization saved to: {plot_path}")
        
        return full_report

def main():
    """Main function to run performance analysis"""
    analyzer = PerformanceAnalyzer()
    
    # Run analysis for the last week
    report = analyzer.run_full_analysis(hours=168)
    
    # Print summary
    print("\n🔍 PERFORMANCE ANALYSIS SUMMARY:")
    print("=" * 50)
    
    if 'response_time_analysis' in report and 'overall_stats' in report['response_time_analysis']:
        stats = report['response_time_analysis']['overall_stats']
        print(f"📈 Response Time - Mean: {stats['mean']:.0f}ms, P95: {stats['p95']:.0f}ms")
    
    if 'availability_analysis' in report and 'overall_uptime' in report['availability_analysis']:
        uptime = report['availability_analysis']['overall_uptime']['percentage']
        print(f"⏱️  Overall Uptime: {uptime:.2f}%")
    
    if 'system_performance_analysis' in report:
        sys_analysis = report['system_performance_analysis']
        if 'cpu_analysis' in sys_analysis and sys_analysis['cpu_analysis']:
            cpu_avg = sys_analysis['cpu_analysis'].get('average', 0)
            print(f"💻 Average CPU Usage: {cpu_avg:.1f}%")
        if 'memory_analysis' in sys_analysis and sys_analysis['memory_analysis']:
            mem_avg = sys_analysis['memory_analysis'].get('average', 0)
            print(f"🧠 Average Memory Usage: {mem_avg:.1f}%")
    
    print(f"\n💡 OPTIMIZATION RECOMMENDATIONS ({len(report['optimization_recommendations'])}):")
    for i, rec in enumerate(report['optimization_recommendations'][:5], 1):
        print(f"  {i}. [{rec['priority']}] {rec['issue']}")
        print(f"     → {rec['recommendation']}")

if __name__ == "__main__":
    main()

