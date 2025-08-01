import { Button } from '@/components/ui/button.jsx';
import { ArrowRight, Sparkles, Zap, Globe } from 'lucide-react';

const Hero = ({ language }) => {
  const translations = {
    en: {
      title: "Boost Your Business with",
      titleHighlight: "AI Marketing Tools",
      subtitle: "Professional AI-powered marketing solutions that help you create engaging content, automate customer interactions, and grow your business with intelligent insights.",
      cta1: "Start Free Trial",
      cta2: "Watch Demo",
      features: [
        "AI-Powered Chatbot",
        "Multilingual Support", 
        "Analytics Dashboard",
        "24/7 Customer Support"
      ]
    },
    es: {
      title: "Impulsa Tu Negocio con",
      titleHighlight: "Herramientas de Marketing IA",
      subtitle: "Soluciones de marketing profesionales impulsadas por IA que te ayudan a crear contenido atractivo, automatizar interacciones con clientes y hacer crecer tu negocio con insights inteligentes.",
      cta1: "Prueba Gratuita",
      cta2: "Ver Demo",
      features: [
        "Chatbot con IA",
        "Soporte Multiidioma",
        "Panel de Análisis", 
        "Soporte 24/7"
      ]
    },
    pap: {
      title: "Mehora Bo Negoshi ku",
      titleHighlight: "Hermentnan di Marketing AI",
      subtitle: "Solushonnan di marketing profesional ku AI ku ta yudabo krea kontenido atraktivo, automatisa interakshon ku kliente, y laga bo negoshi krece ku insight inteligente.",
      cta1: "Kuminsá Gratis",
      cta2: "Mira Demo",
      features: [
        "Chatbot ku AI",
        "Soporte Multi-idioma",
        "Dashboard di Analítika",
        "Soporte 24/7"
      ]
    },
    nl: {
      title: "Versterk Je Bedrijf met",
      titleHighlight: "AI Marketing Tools",
      subtitle: "Professionele AI-gedreven marketingoplossingen die je helpen boeiende content te creëren, klantinteracties te automatiseren en je bedrijf te laten groeien met intelligente inzichten.",
      cta1: "Gratis Proefperiode",
      cta2: "Bekijk Demo",
      features: [
        "AI-Powered Chatbot",
        "Meertalige Ondersteuning",
        "Analytics Dashboard",
        "24/7 Klantenservice"
      ]
    }
  };

  const t = translations[language] || translations.en;

  return (
    <section id="home" className="min-h-screen flex items-center justify-center relative overflow-hidden">
      {/* Background Elements */}
      <div className="absolute inset-0 tropical-gradient opacity-5"></div>
      <div className="absolute top-20 left-10 w-32 h-32 bg-primary/10 rounded-full blur-3xl floating-animation"></div>
      <div className="absolute bottom-20 right-10 w-40 h-40 bg-accent/10 rounded-full blur-3xl floating-animation" style={{animationDelay: '2s'}}></div>
      <div className="absolute top-1/2 left-1/4 w-24 h-24 bg-secondary/10 rounded-full blur-2xl floating-animation" style={{animationDelay: '4s'}}></div>

      <div className="container mx-auto px-4 py-20 relative z-10">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Column - Content */}
          <div className="space-y-8">
            <div className="space-y-4">
              <div className="flex items-center space-x-2 text-primary">
                <Sparkles className="w-5 h-5" />
                <span className="text-sm font-medium uppercase tracking-wider">
                  AI-Powered Marketing
                </span>
              </div>
              
              <h1 className="text-4xl md:text-6xl font-bold leading-tight">
                {t.title}{' '}
                <span className="tropical-text-gradient">
                  {t.titleHighlight}
                </span>
              </h1>
              
              <p className="text-lg md:text-xl text-muted-foreground leading-relaxed max-w-2xl">
                {t.subtitle}
              </p>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <Button 
                size="lg" 
                className="tropical-gradient text-white hover:opacity-90 pulse-glow group"
              >
                {t.cta1}
                <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </Button>
              <Button 
                size="lg" 
                variant="outline" 
                className="hover-lift"
              >
                {t.cta2}
              </Button>
            </div>

            {/* Features List */}
            <div className="grid grid-cols-2 gap-4 pt-8">
              {t.features.map((feature, index) => (
                <div key={index} className="flex items-center space-x-3">
                  <div className="w-8 h-8 tropical-gradient rounded-full flex items-center justify-center">
                    <Zap className="w-4 h-4 text-white" />
                  </div>
                  <span className="text-sm font-medium">{feature}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Right Column - Visual */}
          <div className="relative">
            <div className="relative z-10">
              {/* Main Card */}
              <div className="bg-card border rounded-3xl p-8 shadow-2xl hover-lift glass-effect">
                <div className="space-y-6">
                  {/* Header */}
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <div className="w-12 h-12 tropical-gradient rounded-xl flex items-center justify-center">
                        <Globe className="w-6 h-6 text-white" />
                      </div>
                      <div>
                        <h3 className="font-semibold">AI Marketing Assistant</h3>
                        <p className="text-sm text-muted-foreground">Online now</p>
                      </div>
                    </div>
                    <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                  </div>

                  {/* Chat Messages */}
                  <div className="space-y-4">
                    <div className="bg-muted rounded-2xl p-4 max-w-xs">
                      <p className="text-sm">
                        {language === 'es' ? '¡Hola! ¿Cómo puedo ayudarte con tu marketing hoy?' :
                         language === 'pap' ? 'Bon dia! Kon mi por yudabo ku bo marketing awe?' :
                         language === 'nl' ? 'Hallo! Hoe kan ik je vandaag helpen met je marketing?' :
                         'Hello! How can I help you with your marketing today?'}
                      </p>
                    </div>
                    <div className="bg-primary text-primary-foreground rounded-2xl p-4 max-w-xs ml-auto">
                      <p className="text-sm">
                        {language === 'es' ? 'Necesito ayuda con contenido para redes sociales' :
                         language === 'pap' ? 'Mi mester yudansa ku kontenido pa social media' :
                         language === 'nl' ? 'Ik heb hulp nodig met social media content' :
                         'I need help with social media content'}
                      </p>
                    </div>
                    <div className="bg-muted rounded-2xl p-4 max-w-xs">
                      <p className="text-sm">
                        {language === 'es' ? '¡Perfecto! Puedo ayudarte a crear contenido atractivo...' :
                         language === 'pap' ? 'Perfekto! Mi por yudabo krea kontenido atraktivo...' :
                         language === 'nl' ? 'Perfect! Ik kan je helpen boeiende content te maken...' :
                         'Perfect! I can help you create engaging content...'}
                      </p>
                    </div>
                  </div>

                  {/* Typing Indicator */}
                  <div className="flex items-center space-x-2 text-muted-foreground">
                    <div className="flex space-x-1">
                      <div className="w-2 h-2 bg-primary rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                      <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                    </div>
                    <span className="text-xs">AI is typing...</span>
                  </div>
                </div>
              </div>

              {/* Floating Elements */}
              <div className="absolute -top-4 -right-4 w-16 h-16 tropical-gradient rounded-2xl flex items-center justify-center shadow-lg floating-animation">
                <Sparkles className="w-8 h-8 text-white" />
              </div>
              <div className="absolute -bottom-4 -left-4 w-12 h-12 bg-accent rounded-xl flex items-center justify-center shadow-lg floating-animation" style={{animationDelay: '1s'}}>
                <Zap className="w-6 h-6 text-white" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;

