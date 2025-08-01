import { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/button.jsx';
import { Card, CardContent, CardHeader } from '@/components/ui/card.jsx';
import { 
  MessageCircle, 
  X, 
  Send, 
  Bot, 
  User,
  Minimize2,
  Maximize2,
  RotateCcw
} from 'lucide-react';

const Chatbot = ({ isOpen, onToggle, language }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  const messagesEndRef = useRef(null);

  const translations = {
    en: {
      title: "AI Marketing Assistant",
      placeholder: "Type your message...",
      send: "Send",
      minimize: "Minimize",
      maximize: "Maximize",
      close: "Close",
      reset: "Reset Chat",
      typing: "AI is typing...",
      welcome: "Hello! I'm your AI Marketing Assistant. How can I help you grow your business today?",
      suggestions: [
        "Create a social media campaign",
        "Help with email marketing",
        "Analyze my website traffic",
        "Generate blog content ideas"
      ]
    },
    es: {
      title: "Asistente de Marketing IA",
      placeholder: "Escribe tu mensaje...",
      send: "Enviar",
      minimize: "Minimizar",
      maximize: "Maximizar",
      close: "Cerrar",
      reset: "Reiniciar Chat",
      typing: "IA está escribiendo...",
      welcome: "¡Hola! Soy tu Asistente de Marketing IA. ¿Cómo puedo ayudarte a hacer crecer tu negocio hoy?",
      suggestions: [
        "Crear una campaña de redes sociales",
        "Ayuda con email marketing",
        "Analizar el tráfico de mi sitio web",
        "Generar ideas de contenido para blog"
      ]
    },
    pap: {
      title: "Asistente di Marketing AI",
      placeholder: "Tipa bo mensahe...",
      send: "Manda",
      minimize: "Minimisá",
      maximize: "Maksimisá",
      close: "Sera",
      reset: "Reset Chat",
      typing: "AI ta tipa...",
      welcome: "Bon dia! Mi ta bo Asistente di Marketing AI. Kon mi por yudabo laga bo negoshi krece awe?",
      suggestions: [
        "Krea un kampaña di social media",
        "Yudansa ku email marketing",
        "Analisá tráfiko di mi website",
        "Genera ideanan di kontenido pa blog"
      ]
    },
    nl: {
      title: "AI Marketing Assistent",
      placeholder: "Typ je bericht...",
      send: "Versturen",
      minimize: "Minimaliseren",
      maximize: "Maximaliseren",
      close: "Sluiten",
      reset: "Chat Resetten",
      typing: "AI is aan het typen...",
      welcome: "Hallo! Ik ben je AI Marketing Assistent. Hoe kan ik je helpen je bedrijf vandaag te laten groeien?",
      suggestions: [
        "Maak een social media campagne",
        "Help met email marketing",
        "Analyseer mijn website verkeer",
        "Genereer blog content ideeën"
      ]
    }
  };

  const t = translations[language] || translations.en;

  // Initialize with welcome message
  useEffect(() => {
    if (messages.length === 0) {
      setMessages([
        {
          id: 1,
          text: t.welcome,
          sender: 'bot',
          timestamp: new Date()
        }
      ]);
    }
  }, [t.welcome, messages.length]);

  // Auto scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsTyping(true);

    // Simulate AI response
    setTimeout(() => {
      const responses = {
        en: [
          "That's a great question! Let me help you with that. Based on your needs, I'd recommend starting with...",
          "I can definitely assist you with that! Here are some strategies that work well for businesses like yours...",
          "Excellent! I have some proven techniques that can help you achieve better results. Let me share...",
          "Perfect timing for that question! I've helped many businesses with similar challenges. Here's what I suggest..."
        ],
        es: [
          "¡Esa es una gran pregunta! Déjame ayudarte con eso. Basándome en tus necesidades, recomendaría empezar con...",
          "¡Definitivamente puedo ayudarte con eso! Aquí tienes algunas estrategias que funcionan bien para negocios como el tuyo...",
          "¡Excelente! Tengo algunas técnicas probadas que pueden ayudarte a lograr mejores resultados. Déjame compartir...",
          "¡Momento perfecto para esa pregunta! He ayudado a muchos negocios con desafíos similares. Esto es lo que sugiero..."
        ],
        pap: [
          "Esey ta un pregunta bunita! Laga mi yudabo ku esey. Basá riba bo nesesidat, mi ta rekomendá kuminsá ku...",
          "Definitivamente mi por yudabo ku esey! Aki tin algun estrategianan ku ta funshona bon pa negoshinan manera bo su...",
          "Eksèlente! Mi tin algun téknikanan probá ku por yudabo haña resultado miho. Laga mi kompartí...",
          "Momento perfekto pa e pregunta ey! Mi a yuda hopi negoshi ku desafíonan similar. Esaki ta loke mi ta sugerí..."
        ],
        nl: [
          "Dat is een geweldige vraag! Laat me je daarmee helpen. Gebaseerd op je behoeften zou ik aanraden om te beginnen met...",
          "Ik kan je daar zeker mee helpen! Hier zijn enkele strategieën die goed werken voor bedrijven zoals het jouwe...",
          "Uitstekend! Ik heb enkele bewezen technieken die je kunnen helpen betere resultaten te behalen. Laat me delen...",
          "Perfect moment voor die vraag! Ik heb veel bedrijven geholpen met vergelijkbare uitdagingen. Dit is wat ik voorstel..."
        ]
      };

      const responseTexts = responses[language] || responses.en;
      const randomResponse = responseTexts[Math.floor(Math.random() * responseTexts.length)];

      const botMessage = {
        id: Date.now() + 1,
        text: randomResponse,
        sender: 'bot',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);
      setIsTyping(false);
    }, 1500 + Math.random() * 1000);
  };

  const handleSuggestionClick = (suggestion) => {
    setInputValue(suggestion);
  };

  const handleReset = () => {
    setMessages([
      {
        id: 1,
        text: t.welcome,
        sender: 'bot',
        timestamp: new Date()
      }
    ]);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  if (!isOpen) {
    return (
      <div className="chatbot-container">
        <div className="chatbot-bubble" onClick={onToggle}>
          <MessageCircle className="w-6 h-6 text-white" />
        </div>
      </div>
    );
  }

  return (
    <div className="chatbot-container">
      <div className={`chatbot-window ${isOpen ? 'open' : ''} ${isMinimized ? 'h-16' : ''}`}>
        <Card className="h-full flex flex-col border-0 shadow-none">
          {/* Header */}
          <CardHeader className="tropical-gradient text-white p-4 rounded-t-3xl">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <div className="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                  <Bot className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-semibold text-sm">{t.title}</h3>
                  <p className="text-xs opacity-90">
                    {isTyping ? t.typing : 'Online'}
                  </p>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Button
                  size="sm"
                  variant="ghost"
                  className="text-white hover:bg-white/20 p-1 h-8 w-8"
                  onClick={() => setIsMinimized(!isMinimized)}
                >
                  {isMinimized ? <Maximize2 className="w-4 h-4" /> : <Minimize2 className="w-4 h-4" />}
                </Button>
                <Button
                  size="sm"
                  variant="ghost"
                  className="text-white hover:bg-white/20 p-1 h-8 w-8"
                  onClick={handleReset}
                >
                  <RotateCcw className="w-4 h-4" />
                </Button>
                <Button
                  size="sm"
                  variant="ghost"
                  className="text-white hover:bg-white/20 p-1 h-8 w-8"
                  onClick={onToggle}
                >
                  <X className="w-4 h-4" />
                </Button>
              </div>
            </div>
          </CardHeader>

          {!isMinimized && (
            <>
              {/* Messages */}
              <CardContent className="flex-1 p-4 overflow-y-auto max-h-80">
                <div className="space-y-4">
                  {messages.map((message) => (
                    <div
                      key={message.id}
                      className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                      <div className={`flex items-start space-x-2 max-w-[80%] ${message.sender === 'user' ? 'flex-row-reverse space-x-reverse' : ''}`}>
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                          message.sender === 'user' 
                            ? 'bg-primary text-primary-foreground' 
                            : 'tropical-gradient text-white'
                        }`}>
                          {message.sender === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
                        </div>
                        <div className={`rounded-2xl p-3 ${
                          message.sender === 'user'
                            ? 'bg-primary text-primary-foreground'
                            : 'bg-muted'
                        }`}>
                          <p className="text-sm">{message.text}</p>
                          <p className="text-xs opacity-70 mt-1">
                            {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                          </p>
                        </div>
                      </div>
                    </div>
                  ))}
                  
                  {isTyping && (
                    <div className="flex justify-start">
                      <div className="flex items-start space-x-2">
                        <div className="w-8 h-8 tropical-gradient rounded-full flex items-center justify-center">
                          <Bot className="w-4 h-4 text-white" />
                        </div>
                        <div className="bg-muted rounded-2xl p-3">
                          <div className="flex space-x-1">
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce"></div>
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                  <div ref={messagesEndRef} />
                </div>

                {/* Suggestions */}
                {messages.length === 1 && (
                  <div className="mt-4 space-y-2">
                    <p className="text-xs text-muted-foreground">{language === 'es' ? 'Sugerencias:' : language === 'pap' ? 'Sugerenshanan:' : language === 'nl' ? 'Suggesties:' : 'Suggestions:'}</p>
                    {t.suggestions.map((suggestion, index) => (
                      <button
                        key={index}
                        onClick={() => handleSuggestionClick(suggestion)}
                        className="block w-full text-left text-xs p-2 bg-muted hover:bg-muted/80 rounded-lg transition-colors"
                      >
                        {suggestion}
                      </button>
                    ))}
                  </div>
                )}
              </CardContent>

              {/* Input */}
              <div className="p-4 border-t">
                <div className="flex space-x-2">
                  <textarea
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder={t.placeholder}
                    className="flex-1 resize-none border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
                    rows="1"
                  />
                  <Button
                    onClick={handleSendMessage}
                    disabled={!inputValue.trim() || isTyping}
                    size="sm"
                    className="tropical-gradient text-white hover:opacity-90"
                  >
                    <Send className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </>
          )}
        </Card>
      </div>
    </div>
  );
};

export default Chatbot;

