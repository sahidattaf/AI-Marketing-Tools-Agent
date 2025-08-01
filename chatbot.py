from flask import Blueprint, request, jsonify
from datetime import datetime
import random
import json

chatbot_bp = Blueprint('chatbot', __name__)

# Mock AI responses for different languages
AI_RESPONSES = {
    'en': [
        "That's a great question! Let me help you with that. Based on your needs, I'd recommend starting with our content generation tools to create engaging social media posts and email campaigns.",
        "I can definitely assist you with that! Here are some proven marketing strategies that work well for businesses like yours: 1) Focus on your target audience, 2) Create valuable content, 3) Use data-driven insights.",
        "Excellent! I have some techniques that can help you achieve better results. For tropical businesses like restaurants, visual storytelling and local community engagement are key.",
        "Perfect timing for that question! I've helped many businesses with similar challenges. Let's start by analyzing your current marketing approach and identifying opportunities for improvement."
    ],
    'es': [
        "¡Esa es una gran pregunta! Déjame ayudarte con eso. Basándome en tus necesidades, recomendaría empezar con nuestras herramientas de generación de contenido para crear posts atractivos y campañas de email.",
        "¡Definitivamente puedo ayudarte con eso! Aquí tienes algunas estrategias de marketing probadas que funcionan bien para negocios como el tuyo: 1) Enfócate en tu audiencia objetivo, 2) Crea contenido valioso, 3) Usa insights basados en datos.",
        "¡Excelente! Tengo algunas técnicas que pueden ayudarte a lograr mejores resultados. Para negocios tropicales como restaurantes, la narrativa visual y el compromiso con la comunidad local son clave.",
        "¡Momento perfecto para esa pregunta! He ayudado a muchos negocios con desafíos similares. Empecemos analizando tu enfoque de marketing actual e identificando oportunidades de mejora."
    ],
    'pap': [
        "Esey ta un pregunta bunita! Laga mi yudabo ku esey. Basá riba bo nesesidat, mi ta rekomendá kuminsá ku nos hermentnan di generashon di kontenido pa krea posts atraktivo y kampañanan di email.",
        "Definitivamente mi por yudabo ku esey! Aki tin algun estrategianan di marketing probá ku ta funshona bon pa negoshinan manera bo su: 1) Konsentrá riba bo audienshia objetivo, 2) Krea kontenido valioso, 3) Usa insights basá riba data.",
        "Eksèlente! Mi tin algun téknikanan ku por yudabo haña resultado miho. Pa negoshinan tropikal manera restoran, narrativa visual y kompromiso ku komunidat lokal ta klave.",
        "Momento perfekto pa e pregunta ey! Mi a yuda hopi negoshi ku desafíonan similar. Laga nos kuminsá analisando bo enfoke di marketing aktual y identifiká oportunidatnan pa mehora."
    ],
    'nl': [
        "Dat is een geweldige vraag! Laat me je daarmee helpen. Gebaseerd op je behoeften zou ik aanraden om te beginnen met onze content generatie tools om boeiende social media posts en email campagnes te maken.",
        "Ik kan je daar zeker mee helpen! Hier zijn enkele bewezen marketingstrategieën die goed werken voor bedrijven zoals het jouwe: 1) Focus op je doelgroep, 2) Creëer waardevolle content, 3) Gebruik data-gedreven inzichten.",
        "Uitstekend! Ik heb enkele technieken die je kunnen helpen betere resultaten te behalen. Voor tropische bedrijven zoals restaurants zijn visuele verhalen en lokale gemeenschapsbetrokkenheid essentieel.",
        "Perfect moment voor die vraag! Ik heb veel bedrijven geholpen met vergelijkbare uitdagingen. Laten we beginnen met het analyseren van je huidige marketingaanpak en het identificeren van verbeterkansen."
    ]
}

# Store conversation history (in production, use a proper database)
conversation_history = {}

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        language = data.get('language', 'en')
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Initialize conversation history for new sessions
        if session_id not in conversation_history:
            conversation_history[session_id] = []
        
        # Add user message to history
        conversation_history[session_id].append({
            'sender': 'user',
            'message': user_message,
            'timestamp': datetime.now().isoformat(),
            'language': language
        })
        
        # Generate AI response based on language
        responses = AI_RESPONSES.get(language, AI_RESPONSES['en'])
        ai_response = random.choice(responses)
        
        # Add AI response to history
        conversation_history[session_id].append({
            'sender': 'bot',
            'message': ai_response,
            'timestamp': datetime.now().isoformat(),
            'language': language
        })
        
        # Log the interaction for analytics
        log_chat_interaction(session_id, user_message, ai_response, language)
        
        return jsonify({
            'response': ai_response,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'language': language
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chatbot_bp.route('/chat/history/<session_id>', methods=['GET'])
def get_chat_history(session_id):
    try:
        history = conversation_history.get(session_id, [])
        return jsonify({
            'session_id': session_id,
            'history': history,
            'total_messages': len(history)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chatbot_bp.route('/chat/sessions', methods=['GET'])
def get_active_sessions():
    try:
        sessions = list(conversation_history.keys())
        return jsonify({
            'active_sessions': sessions,
            'total_sessions': len(sessions)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def log_chat_interaction(session_id, user_message, ai_response, language):
    """Log chat interactions for analytics"""
    try:
        # In production, this would write to a proper logging system or database
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'session_id': session_id,
            'user_message': user_message,
            'ai_response': ai_response,
            'language': language,
            'message_length': len(user_message),
            'response_length': len(ai_response)
        }
        
        # For demo purposes, we'll just print to console
        print(f"Chat Log: {json.dumps(log_entry, indent=2)}")
        
    except Exception as e:
        print(f"Error logging chat interaction: {e}")

@chatbot_bp.route('/chat/analytics', methods=['GET'])
def get_chat_analytics():
    try:
        total_conversations = len(conversation_history)
        total_messages = sum(len(history) for history in conversation_history.values())
        
        # Language distribution
        language_stats = {}
        for history in conversation_history.values():
            for message in history:
                lang = message.get('language', 'en')
                language_stats[lang] = language_stats.get(lang, 0) + 1
        
        # Average messages per conversation
        avg_messages = total_messages / total_conversations if total_conversations > 0 else 0
        
        return jsonify({
            'total_conversations': total_conversations,
            'total_messages': total_messages,
            'average_messages_per_conversation': round(avg_messages, 2),
            'language_distribution': language_stats,
            'active_sessions': len(conversation_history)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

