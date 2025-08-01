from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import json
import random

analytics_bp = Blueprint('analytics', __name__)

# Mock analytics data storage (in production, use a proper database)
analytics_data = {
    'page_views': [],
    'user_interactions': [],
    'conversion_events': [],
    'performance_metrics': []
}

@analytics_bp.route('/track/pageview', methods=['POST'])
def track_pageview():
    try:
        data = request.get_json()
        
        pageview_data = {
            'timestamp': datetime.now().isoformat(),
            'page': data.get('page', '/'),
            'user_agent': request.headers.get('User-Agent', ''),
            'ip_address': request.remote_addr,
            'referrer': data.get('referrer', ''),
            'language': data.get('language', 'en'),
            'session_id': data.get('session_id', ''),
            'user_id': data.get('user_id', None)
        }
        
        analytics_data['page_views'].append(pageview_data)
        
        return jsonify({
            'status': 'success',
            'message': 'Pageview tracked successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/track/interaction', methods=['POST'])
def track_interaction():
    try:
        data = request.get_json()
        
        interaction_data = {
            'timestamp': datetime.now().isoformat(),
            'event_type': data.get('event_type', 'click'),
            'element': data.get('element', ''),
            'page': data.get('page', '/'),
            'user_id': data.get('user_id', None),
            'session_id': data.get('session_id', ''),
            'language': data.get('language', 'en'),
            'additional_data': data.get('additional_data', {})
        }
        
        analytics_data['user_interactions'].append(interaction_data)
        
        return jsonify({
            'status': 'success',
            'message': 'Interaction tracked successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/track/conversion', methods=['POST'])
def track_conversion():
    try:
        data = request.get_json()
        
        conversion_data = {
            'timestamp': datetime.now().isoformat(),
            'conversion_type': data.get('conversion_type', 'signup'),
            'value': data.get('value', 0),
            'currency': data.get('currency', 'USD'),
            'user_id': data.get('user_id', None),
            'session_id': data.get('session_id', ''),
            'source': data.get('source', 'direct'),
            'campaign': data.get('campaign', ''),
            'language': data.get('language', 'en')
        }
        
        analytics_data['conversion_events'].append(conversion_data)
        
        return jsonify({
            'status': 'success',
            'message': 'Conversion tracked successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/dashboard/overview', methods=['GET'])
def get_dashboard_overview():
    try:
        # Calculate time ranges
        now = datetime.now()
        last_24h = now - timedelta(hours=24)
        last_7d = now - timedelta(days=7)
        last_30d = now - timedelta(days=30)
        
        # Mock data for demonstration
        overview_data = {
            'total_users': random.randint(1200, 1500),
            'active_users_24h': random.randint(150, 200),
            'page_views_24h': random.randint(800, 1200),
            'conversion_rate': round(random.uniform(2.5, 4.2), 2),
            'avg_session_duration': random.randint(180, 300),
            'bounce_rate': round(random.uniform(35, 45), 1),
            'top_pages': [
                {'page': '/', 'views': random.randint(300, 500)},
                {'page': '/tools', 'views': random.randint(200, 350)},
                {'page': '/pricing', 'views': random.randint(150, 250)},
                {'page': '/about', 'views': random.randint(100, 180)}
            ],
            'language_distribution': {
                'en': random.randint(60, 70),
                'es': random.randint(15, 25),
                'pap': random.randint(5, 10),
                'nl': random.randint(5, 10)
            },
            'traffic_sources': {
                'direct': random.randint(40, 50),
                'organic': random.randint(25, 35),
                'social': random.randint(10, 20),
                'referral': random.randint(5, 15),
                'paid': random.randint(3, 8)
            }
        }
        
        return jsonify(overview_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/dashboard/chatbot', methods=['GET'])
def get_chatbot_analytics():
    try:
        # Mock chatbot analytics data
        chatbot_analytics = {
            'total_conversations': random.randint(500, 800),
            'conversations_24h': random.randint(50, 100),
            'avg_messages_per_conversation': round(random.uniform(3.2, 5.8), 1),
            'user_satisfaction': round(random.uniform(4.2, 4.8), 1),
            'resolution_rate': round(random.uniform(75, 85), 1),
            'response_time_avg': round(random.uniform(1.2, 2.5), 1),
            'popular_topics': [
                {'topic': 'Content Creation', 'count': random.randint(120, 180)},
                {'topic': 'Pricing Information', 'count': random.randint(80, 140)},
                {'topic': 'Technical Support', 'count': random.randint(60, 100)},
                {'topic': 'Feature Requests', 'count': random.randint(40, 80)}
            ],
            'language_usage': {
                'en': random.randint(65, 75),
                'es': random.randint(12, 20),
                'pap': random.randint(5, 10),
                'nl': random.randint(5, 10)
            },
            'hourly_distribution': [
                {'hour': i, 'conversations': random.randint(5, 25)} 
                for i in range(24)
            ]
        }
        
        return jsonify(chatbot_analytics)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/dashboard/performance', methods=['GET'])
def get_performance_metrics():
    try:
        # Mock performance metrics
        performance_data = {
            'page_load_time': {
                'avg': round(random.uniform(1.2, 2.1), 2),
                'p95': round(random.uniform(2.5, 3.8), 2),
                'trend': 'improving'
            },
            'api_response_time': {
                'avg': round(random.uniform(150, 300), 0),
                'p95': round(random.uniform(400, 600), 0),
                'trend': 'stable'
            },
            'error_rate': {
                'rate': round(random.uniform(0.1, 0.5), 2),
                'trend': 'decreasing'
            },
            'uptime': {
                'percentage': round(random.uniform(99.5, 99.9), 2),
                'last_incident': '2025-01-15T10:30:00Z'
            },
            'resource_usage': {
                'cpu': random.randint(15, 35),
                'memory': random.randint(40, 70),
                'storage': random.randint(25, 45)
            }
        }
        
        return jsonify(performance_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/reports/export', methods=['POST'])
def export_analytics_report():
    try:
        data = request.get_json()
        report_type = data.get('report_type', 'overview')
        date_range = data.get('date_range', '7d')
        format_type = data.get('format', 'json')
        
        # Mock report generation
        report_data = {
            'report_id': f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'type': report_type,
            'date_range': date_range,
            'generated_at': datetime.now().isoformat(),
            'data': {
                'summary': 'Analytics report generated successfully',
                'metrics_included': ['page_views', 'user_interactions', 'conversions'],
                'total_records': random.randint(1000, 5000)
            }
        }
        
        return jsonify({
            'status': 'success',
            'message': 'Report generated successfully',
            'report': report_data,
            'download_url': f'/api/reports/download/{report_data["report_id"]}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@analytics_bp.route('/health', methods=['GET'])
def analytics_health_check():
    try:
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'analytics',
            'version': '1.0.0',
            'data_points': {
                'page_views': len(analytics_data['page_views']),
                'interactions': len(analytics_data['user_interactions']),
                'conversions': len(analytics_data['conversion_events'])
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

