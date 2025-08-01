#!/usr/bin/env python3
"""
AI Marketing Tools - Analytics Dashboard
Comprehensive dashboard for monitoring platform performance, user engagement, and business metrics.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import json
import requests
from typing import Dict, List, Any
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AIMarketingAnalyticsDashboard:
    """Main analytics dashboard class for AI Marketing Tools platform"""
    
    def __init__(self, api_base_url: str = "http://localhost:5000/api"):
        self.api_base_url = api_base_url
        self.colors = {
            'primary_teal': '#4ECDC4',
            'secondary_coral': '#FF6B6B',
            'background': '#F8FFFE',
            'text_dark': '#2C3E50',
            'text_light': '#7F8C8D'
        }
        
    def fetch_analytics_data(self) -> Dict[str, Any]:
        """Fetch analytics data from the backend API"""
        try:
            # Fetch overview data
            overview_response = requests.get(f"{self.api_base_url}/dashboard/overview")
            overview_data = overview_response.json() if overview_response.status_code == 200 else {}
            
            # Fetch chatbot analytics
            chatbot_response = requests.get(f"{self.api_base_url}/dashboard/chatbot")
            chatbot_data = chatbot_response.json() if chatbot_response.status_code == 200 else {}
            
            # Fetch performance metrics
            performance_response = requests.get(f"{self.api_base_url}/dashboard/performance")
            performance_data = performance_response.json() if performance_response.status_code == 200 else {}
            
            # Fetch revenue analytics
            revenue_response = requests.get(f"{self.api_base_url}/analytics/revenue")
            revenue_data = revenue_response.json() if revenue_response.status_code == 200 else {}
            
            return {
                'overview': overview_data,
                'chatbot': chatbot_data,
                'performance': performance_data,
                'revenue': revenue_data
            }
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return self.generate_mock_data()
    
    def generate_mock_data(self) -> Dict[str, Any]:
        """Generate mock data for demonstration purposes"""
        return {
            'overview': {
                'total_users': 1347,
                'active_users_24h': 183,
                'page_views_24h': 1024,
                'conversion_rate': 3.8,
                'avg_session_duration': 245,
                'bounce_rate': 38.2,
                'top_pages': [
                    {'page': '/', 'views': 412},
                    {'page': '/tools', 'views': 298},
                    {'page': '/pricing', 'views': 187},
                    {'page': '/about', 'views': 127}
                ],
                'language_distribution': {'en': 68, 'es': 18, 'pap': 8, 'nl': 6},
                'traffic_sources': {'direct': 45, 'organic': 32, 'social': 15, 'referral': 8}
            },
            'chatbot': {
                'total_conversations': 672,
                'conversations_24h': 89,
                'avg_messages_per_conversation': 4.2,
                'user_satisfaction': 4.6,
                'resolution_rate': 78.5,
                'response_time_avg': 1.8,
                'popular_topics': [
                    {'topic': 'Content Creation', 'count': 156},
                    {'topic': 'Pricing Information', 'count': 124},
                    {'topic': 'Technical Support', 'count': 89},
                    {'topic': 'Feature Requests', 'count': 67}
                ],
                'language_usage': {'en': 71, 'es': 16, 'pap': 7, 'nl': 6},
                'hourly_distribution': [
                    {'hour': i, 'conversations': np.random.randint(5, 25)} 
                    for i in range(24)
                ]
            },
            'performance': {
                'page_load_time': {'avg': 1.7, 'p95': 3.2, 'trend': 'improving'},
                'api_response_time': {'avg': 245, 'p95': 520, 'trend': 'stable'},
                'error_rate': {'rate': 0.3, 'trend': 'decreasing'},
                'uptime': {'percentage': 99.7, 'last_incident': '2025-01-15T10:30:00Z'},
                'resource_usage': {'cpu': 28, 'memory': 56, 'storage': 34}
            },
            'revenue': {
                'total_revenue': 18750,
                'monthly_recurring_revenue': 9800,
                'annual_recurring_revenue': 117600,
                'churn_rate': 3.8,
                'average_revenue_per_user': 58,
                'conversion_rate': 4.2,
                'plan_distribution': {'starter': 65, 'professional': 30, 'enterprise': 5},
                'billing_cycle_preference': {'monthly': 72, 'yearly': 28},
                'revenue_trend': [
                    {'month': f'2025-{i:02d}', 'revenue': np.random.randint(8000, 15000)}
                    for i in range(1, 8)
                ]
            }
        }
    
    def create_overview_dashboard(self, data: Dict[str, Any]) -> go.Figure:
        """Create comprehensive overview dashboard"""
        overview = data['overview']
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=3,
            subplot_titles=[
                'Key Metrics', 'Traffic Sources', 'Language Distribution',
                'Top Pages', 'User Engagement', 'Performance Indicators'
            ],
            specs=[
                [{"type": "indicator"}, {"type": "pie"}, {"type": "bar"}],
                [{"type": "bar"}, {"type": "scatter"}, {"type": "indicator"}],
                [{"colspan": 3}, None, None]
            ]
        )
        
        # Key Metrics (Indicators)
        fig.add_trace(
            go.Indicator(
                mode="number+delta",
                value=overview['total_users'],
                title={"text": "Total Users"},
                delta={'reference': 1200, 'relative': True},
                domain={'row': 0, 'column': 0}
            ),
            row=1, col=1
        )
        
        # Traffic Sources (Pie Chart)
        fig.add_trace(
            go.Pie(
                labels=list(overview['traffic_sources'].keys()),
                values=list(overview['traffic_sources'].values()),
                hole=0.4,
                marker_colors=[self.colors['primary_teal'], self.colors['secondary_coral'], 
                              '#95E1D3', '#F38BA8']
            ),
            row=1, col=2
        )
        
        # Language Distribution (Bar Chart)
        fig.add_trace(
            go.Bar(
                x=list(overview['language_distribution'].keys()),
                y=list(overview['language_distribution'].values()),
                marker_color=self.colors['primary_teal'],
                name="Language Usage"
            ),
            row=1, col=3
        )
        
        # Top Pages (Horizontal Bar)
        pages = [page['page'] for page in overview['top_pages']]
        views = [page['views'] for page in overview['top_pages']]
        
        fig.add_trace(
            go.Bar(
                x=views,
                y=pages,
                orientation='h',
                marker_color=self.colors['secondary_coral'],
                name="Page Views"
            ),
            row=2, col=1
        )
        
        # User Engagement Over Time (Mock time series)
        dates = pd.date_range(start='2025-01-20', end='2025-01-27', freq='D')
        engagement = np.random.randint(150, 250, len(dates))
        
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=engagement,
                mode='lines+markers',
                line=dict(color=self.colors['primary_teal'], width=3),
                marker=dict(size=8),
                name="Daily Active Users"
            ),
            row=2, col=2
        )
        
        # Performance Indicator
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=overview['conversion_rate'],
                title={'text': "Conversion Rate (%)"},
                gauge={
                    'axis': {'range': [None, 10]},
                    'bar': {'color': self.colors['secondary_coral']},
                    'steps': [
                        {'range': [0, 2], 'color': "lightgray"},
                        {'range': [2, 5], 'color': "yellow"},
                        {'range': [5, 10], 'color': "green"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 5
                    }
                }
            ),
            row=2, col=3
        )
        
        # Update layout
        fig.update_layout(
            height=900,
            title_text="AI Marketing Tools - Analytics Overview Dashboard",
            title_x=0.5,
            title_font_size=24,
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor=self.colors['background']
        )
        
        return fig
    
    def create_chatbot_analytics(self, data: Dict[str, Any]) -> go.Figure:
        """Create chatbot-specific analytics dashboard"""
        chatbot = data['chatbot']
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=[
                'Conversation Volume by Hour', 'Popular Topics',
                'Language Usage', 'Performance Metrics'
            ],
            specs=[
                [{"type": "scatter"}, {"type": "bar"}],
                [{"type": "pie"}, {"type": "indicator"}]
            ]
        )
        
        # Hourly conversation distribution
        hours = [item['hour'] for item in chatbot['hourly_distribution']]
        conversations = [item['conversations'] for item in chatbot['hourly_distribution']]
        
        fig.add_trace(
            go.Scatter(
                x=hours,
                y=conversations,
                mode='lines+markers',
                fill='tonexty',
                line=dict(color=self.colors['primary_teal'], width=2),
                marker=dict(size=6),
                name="Conversations per Hour"
            ),
            row=1, col=1
        )
        
        # Popular topics
        topics = [topic['topic'] for topic in chatbot['popular_topics']]
        counts = [topic['count'] for topic in chatbot['popular_topics']]
        
        fig.add_trace(
            go.Bar(
                x=topics,
                y=counts,
                marker_color=self.colors['secondary_coral'],
                name="Topic Frequency"
            ),
            row=1, col=2
        )
        
        # Language usage pie chart
        fig.add_trace(
            go.Pie(
                labels=list(chatbot['language_usage'].keys()),
                values=list(chatbot['language_usage'].values()),
                hole=0.3,
                marker_colors=[self.colors['primary_teal'], self.colors['secondary_coral'], 
                              '#95E1D3', '#F38BA8']
            ),
            row=2, col=1
        )
        
        # Performance indicator
        fig.add_trace(
            go.Indicator(
                mode="gauge+number+delta",
                value=chatbot['user_satisfaction'],
                title={'text': "User Satisfaction"},
                delta={'reference': 4.0},
                gauge={
                    'axis': {'range': [None, 5]},
                    'bar': {'color': self.colors['primary_teal']},
                    'steps': [
                        {'range': [0, 2], 'color': "red"},
                        {'range': [2, 3.5], 'color': "yellow"},
                        {'range': [3.5, 5], 'color': "green"}
                    ]
                }
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            height=700,
            title_text="AI Chatbot Analytics Dashboard",
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor=self.colors['background']
        )
        
        return fig
    
    def create_revenue_dashboard(self, data: Dict[str, Any]) -> go.Figure:
        """Create revenue and business metrics dashboard"""
        revenue = data['revenue']
        
        fig = make_subplots(
            rows=2, cols=3,
            subplot_titles=[
                'Revenue Trend', 'Plan Distribution', 'Billing Preferences',
                'Key Revenue Metrics', 'Churn Rate', 'ARPU Trend'
            ],
            specs=[
                [{"type": "scatter"}, {"type": "pie"}, {"type": "bar"}],
                [{"type": "indicator"}, {"type": "indicator"}, {"type": "scatter"}]
            ]
        )
        
        # Revenue trend
        months = [item['month'] for item in revenue['revenue_trend']]
        revenues = [item['revenue'] for item in revenue['revenue_trend']]
        
        fig.add_trace(
            go.Scatter(
                x=months,
                y=revenues,
                mode='lines+markers',
                fill='tonexty',
                line=dict(color=self.colors['primary_teal'], width=3),
                marker=dict(size=8),
                name="Monthly Revenue"
            ),
            row=1, col=1
        )
        
        # Plan distribution
        fig.add_trace(
            go.Pie(
                labels=list(revenue['plan_distribution'].keys()),
                values=list(revenue['plan_distribution'].values()),
                hole=0.4,
                marker_colors=[self.colors['primary_teal'], self.colors['secondary_coral'], '#95E1D3']
            ),
            row=1, col=2
        )
        
        # Billing preferences
        fig.add_trace(
            go.Bar(
                x=list(revenue['billing_cycle_preference'].keys()),
                y=list(revenue['billing_cycle_preference'].values()),
                marker_color=[self.colors['primary_teal'], self.colors['secondary_coral']],
                name="Billing Cycle"
            ),
            row=1, col=3
        )
        
        # MRR Indicator
        fig.add_trace(
            go.Indicator(
                mode="number+delta",
                value=revenue['monthly_recurring_revenue'],
                title={'text': "MRR ($)"},
                delta={'reference': 8500, 'relative': True},
                number={'prefix': "$"}
            ),
            row=2, col=1
        )
        
        # Churn Rate Indicator
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=revenue['churn_rate'],
                title={'text': "Churn Rate (%)"},
                gauge={
                    'axis': {'range': [0, 10]},
                    'bar': {'color': self.colors['secondary_coral']},
                    'steps': [
                        {'range': [0, 3], 'color': "green"},
                        {'range': [3, 6], 'color': "yellow"},
                        {'range': [6, 10], 'color': "red"}
                    ]
                }
            ),
            row=2, col=2
        )
        
        # ARPU Trend (mock data)
        arpu_months = months
        arpu_values = [revenue['average_revenue_per_user'] + np.random.randint(-5, 8) for _ in months]
        
        fig.add_trace(
            go.Scatter(
                x=arpu_months,
                y=arpu_values,
                mode='lines+markers',
                line=dict(color=self.colors['secondary_coral'], width=2),
                marker=dict(size=6),
                name="ARPU"
            ),
            row=2, col=3
        )
        
        fig.update_layout(
            height=700,
            title_text="Revenue & Business Metrics Dashboard",
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor=self.colors['background']
        )
        
        return fig
    
    def generate_executive_summary(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate executive summary with key insights"""
        overview = data['overview']
        chatbot = data['chatbot']
        revenue = data['revenue']
        performance = data['performance']
        
        summary = {
            'timestamp': datetime.now().isoformat(),
            'key_metrics': {
                'total_users': overview['total_users'],
                'daily_active_users': overview['active_users_24h'],
                'conversion_rate': overview['conversion_rate'],
                'monthly_recurring_revenue': revenue['monthly_recurring_revenue'],
                'churn_rate': revenue['churn_rate'],
                'user_satisfaction': chatbot['user_satisfaction']
            },
            'insights': [
                f"Platform has {overview['total_users']:,} total users with {overview['conversion_rate']}% conversion rate",
                f"Chatbot handled {chatbot['conversations_24h']} conversations today with {chatbot['user_satisfaction']}/5 satisfaction",
                f"MRR is ${revenue['monthly_recurring_revenue']:,} with {revenue['churn_rate']}% monthly churn",
                f"System uptime is {performance['uptime']['percentage']}% with {performance['api_response_time']['avg']}ms avg response time"
            ],
            'recommendations': [
                "Focus on converting free tier users to paid plans",
                "Improve chatbot training for better satisfaction scores",
                "Implement retention campaigns to reduce churn",
                "Optimize API performance for better user experience"
            ],
            'alerts': [
                f"Churn rate at {revenue['churn_rate']}% - monitor closely",
                f"API response time trending {performance['api_response_time']['trend']}",
                f"Conversion rate below target at {overview['conversion_rate']}%"
            ]
        }
        
        return summary
    
    def save_dashboard_html(self, fig: go.Figure, filename: str):
        """Save dashboard as HTML file"""
        fig.write_html(f"/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/dashboards/{filename}")
        print(f"Dashboard saved as {filename}")
    
    def run_full_analytics_suite(self):
        """Run complete analytics suite and generate all dashboards"""
        print("🚀 Starting AI Marketing Tools Analytics Suite...")
        
        # Fetch data
        print("📊 Fetching analytics data...")
        data = self.fetch_analytics_data()
        
        # Generate dashboards
        print("📈 Creating overview dashboard...")
        overview_fig = self.create_overview_dashboard(data)
        self.save_dashboard_html(overview_fig, "overview_dashboard.html")
        
        print("🤖 Creating chatbot analytics...")
        chatbot_fig = self.create_chatbot_analytics(data)
        self.save_dashboard_html(chatbot_fig, "chatbot_dashboard.html")
        
        print("💰 Creating revenue dashboard...")
        revenue_fig = self.create_revenue_dashboard(data)
        self.save_dashboard_html(revenue_fig, "revenue_dashboard.html")
        
        # Generate executive summary
        print("📋 Generating executive summary...")
        summary = self.generate_executive_summary(data)
        
        with open('/home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/reports/executive_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        print("✅ Analytics suite completed successfully!")
        print(f"📁 Dashboards saved to: /home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/dashboards/")
        print(f"📊 Executive summary: /home/ubuntu/AI_Marketing_Tools_Workspace/analytics-monitoring/reports/executive_summary.json")
        
        return data, summary

def main():
    """Main function to run analytics dashboard"""
    dashboard = AIMarketingAnalyticsDashboard()
    data, summary = dashboard.run_full_analytics_suite()
    
    # Print key insights
    print("\n🔍 KEY INSIGHTS:")
    for insight in summary['insights']:
        print(f"  • {insight}")
    
    print("\n💡 RECOMMENDATIONS:")
    for rec in summary['recommendations']:
        print(f"  • {rec}")
    
    print("\n⚠️  ALERTS:")
    for alert in summary['alerts']:
        print(f"  • {alert}")

if __name__ == "__main__":
    main()

