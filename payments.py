from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import uuid
import random

payments_bp = Blueprint('payments', __name__)

# Mock payment data storage (in production, use a proper database and payment processor)
payment_data = {
    'subscriptions': {},
    'transactions': [],
    'customers': {}
}

# Mock pricing plans
PRICING_PLANS = {
    'starter': {
        'name': 'Starter',
        'monthly_price': 0,
        'yearly_price': 0,
        'features': [
            'AI Chatbot (100 conversations/month)',
            'Basic Content Generator',
            'Email Support',
            'Standard Templates',
            'Basic Analytics'
        ]
    },
    'professional': {
        'name': 'Professional',
        'monthly_price': 49,
        'yearly_price': 39,
        'features': [
            'AI Chatbot (1,000 conversations/month)',
            'Advanced Content Generator',
            'Priority Email Support',
            'Premium Templates',
            'Advanced Analytics',
            'Custom Branding',
            'API Access',
            'A/B Testing'
        ]
    },
    'enterprise': {
        'name': 'Enterprise',
        'monthly_price': 199,
        'yearly_price': 159,
        'features': [
            'Unlimited AI Conversations',
            'Full Content Suite',
            '24/7 Phone & Chat Support',
            'Custom Templates',
            'Enterprise Analytics',
            'White-label Solution',
            'Full API Access',
            'Advanced Integrations',
            'Dedicated Account Manager',
            'Custom Training'
        ]
    }
}

@payments_bp.route('/plans', methods=['GET'])
def get_pricing_plans():
    try:
        return jsonify({
            'plans': PRICING_PLANS,
            'currency': 'USD',
            'billing_cycles': ['monthly', 'yearly'],
            'yearly_discount': 20
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/subscribe', methods=['POST'])
def create_subscription():
    try:
        data = request.get_json()
        
        plan_id = data.get('plan_id')
        billing_cycle = data.get('billing_cycle', 'monthly')
        customer_email = data.get('customer_email')
        payment_method = data.get('payment_method', {})
        
        if not plan_id or plan_id not in PRICING_PLANS:
            return jsonify({'error': 'Invalid plan selected'}), 400
        
        if not customer_email:
            return jsonify({'error': 'Customer email is required'}), 400
        
        # Generate subscription ID
        subscription_id = str(uuid.uuid4())
        customer_id = str(uuid.uuid4())
        
        # Calculate pricing
        plan = PRICING_PLANS[plan_id]
        amount = plan['yearly_price'] if billing_cycle == 'yearly' else plan['monthly_price']
        
        # Create customer record
        payment_data['customers'][customer_id] = {
            'id': customer_id,
            'email': customer_email,
            'created_at': datetime.now().isoformat(),
            'payment_method': payment_method
        }
        
        # Create subscription
        next_billing_date = datetime.now() + timedelta(
            days=365 if billing_cycle == 'yearly' else 30
        )
        
        subscription = {
            'id': subscription_id,
            'customer_id': customer_id,
            'plan_id': plan_id,
            'plan_name': plan['name'],
            'billing_cycle': billing_cycle,
            'amount': amount,
            'currency': 'USD',
            'status': 'active',
            'created_at': datetime.now().isoformat(),
            'next_billing_date': next_billing_date.isoformat(),
            'trial_end': None
        }
        
        payment_data['subscriptions'][subscription_id] = subscription
        
        # Create initial transaction
        transaction = {
            'id': str(uuid.uuid4()),
            'subscription_id': subscription_id,
            'customer_id': customer_id,
            'amount': amount,
            'currency': 'USD',
            'status': 'completed',
            'type': 'subscription_payment',
            'created_at': datetime.now().isoformat(),
            'description': f'{plan["name"]} - {billing_cycle} subscription'
        }
        
        payment_data['transactions'].append(transaction)
        
        return jsonify({
            'status': 'success',
            'subscription': subscription,
            'transaction': transaction,
            'message': 'Subscription created successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/subscription/<subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    try:
        subscription = payment_data['subscriptions'].get(subscription_id)
        
        if not subscription:
            return jsonify({'error': 'Subscription not found'}), 404
        
        # Get customer info
        customer = payment_data['customers'].get(subscription['customer_id'])
        
        # Get recent transactions
        recent_transactions = [
            t for t in payment_data['transactions']
            if t['subscription_id'] == subscription_id
        ][-5:]  # Last 5 transactions
        
        return jsonify({
            'subscription': subscription,
            'customer': customer,
            'recent_transactions': recent_transactions
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/subscription/<subscription_id>/cancel', methods=['POST'])
def cancel_subscription(subscription_id):
    try:
        subscription = payment_data['subscriptions'].get(subscription_id)
        
        if not subscription:
            return jsonify({'error': 'Subscription not found'}), 404
        
        # Update subscription status
        subscription['status'] = 'cancelled'
        subscription['cancelled_at'] = datetime.now().isoformat()
        
        # Create cancellation transaction
        transaction = {
            'id': str(uuid.uuid4()),
            'subscription_id': subscription_id,
            'customer_id': subscription['customer_id'],
            'amount': 0,
            'currency': 'USD',
            'status': 'completed',
            'type': 'cancellation',
            'created_at': datetime.now().isoformat(),
            'description': f'Subscription cancelled - {subscription["plan_name"]}'
        }
        
        payment_data['transactions'].append(transaction)
        
        return jsonify({
            'status': 'success',
            'subscription': subscription,
            'message': 'Subscription cancelled successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/webhook', methods=['POST'])
def payment_webhook():
    try:
        # Mock webhook handler for payment processor events
        data = request.get_json()
        event_type = data.get('type', 'unknown')
        
        # Log the webhook event
        webhook_log = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'data': data,
            'processed': True
        }
        
        # Handle different event types
        if event_type == 'payment.succeeded':
            # Handle successful payment
            pass
        elif event_type == 'payment.failed':
            # Handle failed payment
            pass
        elif event_type == 'subscription.updated':
            # Handle subscription updates
            pass
        
        return jsonify({
            'status': 'success',
            'message': f'Webhook {event_type} processed successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/analytics/revenue', methods=['GET'])
def get_revenue_analytics():
    try:
        # Mock revenue analytics
        revenue_data = {
            'total_revenue': random.randint(15000, 25000),
            'monthly_recurring_revenue': random.randint(8000, 12000),
            'annual_recurring_revenue': random.randint(96000, 144000),
            'churn_rate': round(random.uniform(2.5, 5.2), 2),
            'average_revenue_per_user': random.randint(45, 75),
            'conversion_rate': round(random.uniform(3.2, 6.8), 2),
            'plan_distribution': {
                'starter': random.randint(60, 70),
                'professional': random.randint(25, 35),
                'enterprise': random.randint(5, 10)
            },
            'billing_cycle_preference': {
                'monthly': random.randint(65, 75),
                'yearly': random.randint(25, 35)
            },
            'revenue_trend': [
                {'month': f'2025-{i:02d}', 'revenue': random.randint(8000, 15000)}
                for i in range(1, 8)
            ]
        }
        
        return jsonify(revenue_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/customers/<customer_id>/usage', methods=['GET'])
def get_customer_usage(customer_id):
    try:
        # Mock usage data for billing
        usage_data = {
            'customer_id': customer_id,
            'billing_period': {
                'start': (datetime.now() - timedelta(days=30)).isoformat(),
                'end': datetime.now().isoformat()
            },
            'usage_metrics': {
                'chatbot_conversations': random.randint(50, 950),
                'content_generations': random.randint(20, 200),
                'api_calls': random.randint(100, 5000),
                'storage_used_mb': random.randint(50, 500)
            },
            'limits': {
                'chatbot_conversations': 1000,
                'content_generations': 500,
                'api_calls': 10000,
                'storage_limit_mb': 1000
            },
            'overage_charges': 0,
            'next_reset_date': (datetime.now() + timedelta(days=5)).isoformat()
        }
        
        return jsonify(usage_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/health', methods=['GET'])
def payments_health_check():
    try:
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'payments',
            'version': '1.0.0',
            'data_points': {
                'active_subscriptions': len([
                    s for s in payment_data['subscriptions'].values()
                    if s['status'] == 'active'
                ]),
                'total_transactions': len(payment_data['transactions']),
                'total_customers': len(payment_data['customers'])
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

