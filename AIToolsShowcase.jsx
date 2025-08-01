import { useState } from 'react';
import { Button } from '@/components/ui/button.jsx';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx';
import { 
  MessageSquare, 
  PenTool, 
  BarChart3, 
  Mail, 
  Image, 
  Video,
  Mic,
  Globe,
  ArrowRight,
  Play,
  Sparkles
} from 'lucide-react';

const AIToolsShowcase = ({ language }) => {
  const [activeDemo, setActiveDemo] = useState(null);

  const translations = {
    en: {
      title: "Powerful AI Tools",
      subtitle: "Everything you need to supercharge your marketing",
      description: "Our comprehensive suite of AI-powered tools helps you create, optimize, and automate your marketing efforts with professional results.",
      tryDemo: "Try Demo",
      learnMore: "Learn More",
      tools: [
        {
          icon: MessageSquare,
          title: "AI Chatbot",
          description: "Intelligent customer support that never sleeps",
          features: ["24/7 availability", "Multilingual support", "Smart responses", "Lead generation"],
          demo: "Chat with our AI assistant right now!"
        },
        {
          icon: PenTool,
          title: "Content Generator",
          description: "Create engaging content in seconds",
          features: ["Blog posts", "Social media", "Email campaigns", "Ad copy"],
          demo: "Generate a social media post about tropical marketing"
        },
        {
          icon: BarChart3,
          title: "Analytics Dashboard",
          description: "Deep insights into your marketing performance",
          features: ["Real-time data", "Custom reports", "ROI tracking", "Predictive analytics"],
          demo: "View sample analytics dashboard"
        },
        {
          icon: Mail,
          title: "Email Automation",
          description: "Personalized email campaigns that convert",
          features: ["Smart segmentation", "A/B testing", "Drip campaigns", "Performance tracking"],
          demo: "Create an automated welcome email sequence"
        },
        {
          icon: Image,
          title: "Visual Creator",
          description: "AI-generated images and graphics",
          features: ["Custom graphics", "Brand consistency", "Multiple formats", "Instant generation"],
          demo: "Generate a tropical-themed marketing banner"
        },
        {
          icon: Video,
          title: "Video Producer",
          description: "Professional videos without the complexity",
          features: ["Template library", "Auto-editing", "Voice synthesis", "Multi-platform export"],
          demo: "Create a 30-second product showcase video"
        }
      ]
    },
    es: {
      title: "Herramientas IA Potentes",
      subtitle: "Todo lo que necesitas para potenciar tu marketing",
      description: "Nuestra suite completa de herramientas impulsadas por IA te ayuda a crear, optimizar y automatizar tus esfuerzos de marketing con resultados profesionales.",
      tryDemo: "Probar Demo",
      learnMore: "Saber Más",
      tools: [
        {
          icon: MessageSquare,
          title: "Chatbot IA",
          description: "Soporte inteligente al cliente que nunca duerme",
          features: ["Disponibilidad 24/7", "Soporte multiidioma", "Respuestas inteligentes", "Generación de leads"],
          demo: "¡Chatea con nuestro asistente IA ahora mismo!"
        },
        {
          icon: PenTool,
          title: "Generador de Contenido",
          description: "Crea contenido atractivo en segundos",
          features: ["Posts de blog", "Redes sociales", "Campañas de email", "Copy publicitario"],
          demo: "Genera un post de redes sociales sobre marketing tropical"
        },
        {
          icon: BarChart3,
          title: "Panel de Análisis",
          description: "Insights profundos sobre tu rendimiento de marketing",
          features: ["Datos en tiempo real", "Reportes personalizados", "Seguimiento ROI", "Análisis predictivo"],
          demo: "Ver panel de análisis de muestra"
        },
        {
          icon: Mail,
          title: "Automatización de Email",
          description: "Campañas de email personalizadas que convierten",
          features: ["Segmentación inteligente", "Pruebas A/B", "Campañas goteo", "Seguimiento de rendimiento"],
          demo: "Crear secuencia automatizada de emails de bienvenida"
        },
        {
          icon: Image,
          title: "Creador Visual",
          description: "Imágenes y gráficos generados por IA",
          features: ["Gráficos personalizados", "Consistencia de marca", "Múltiples formatos", "Generación instantánea"],
          demo: "Generar un banner de marketing con tema tropical"
        },
        {
          icon: Video,
          title: "Productor de Video",
          description: "Videos profesionales sin la complejidad",
          features: ["Biblioteca de plantillas", "Auto-edición", "Síntesis de voz", "Exportación multiplataforma"],
          demo: "Crear un video de showcase de producto de 30 segundos"
        }
      ]
    },
    pap: {
      title: "Hermentnan AI Fuerte",
      subtitle: "Tur kos ku bo mester pa mehora bo marketing",
      description: "Nos suite kompleto di hermentnan ku AI ta yudabo krea, optimisá y automatisá bo esfuersonan di marketing ku resultado profesional.",
      tryDemo: "Purba Demo",
      learnMore: "Siña Mas",
      tools: [
        {
          icon: MessageSquare,
          title: "Chatbot AI",
          description: "Soporte inteligente pa kliente ku nunka ta drumi",
          features: ["Disponibel 24/7", "Soporte multi-idioma", "Respuestanan inteligente", "Generashon di lead"],
          demo: "¡Chat ku nos asistente AI awor mes!"
        },
        {
          icon: PenTool,
          title: "Generador di Kontenido",
          description: "Krea kontenido atraktivo den segundonan",
          features: ["Blog posts", "Social media", "Kampañanan di email", "Copy publisitario"],
          demo: "Genera un post di social media tokante marketing tropikal"
        },
        {
          icon: BarChart3,
          title: "Dashboard di Analítika",
          description: "Insight profundo tokante bo rendimento di marketing",
          features: ["Data real-time", "Reportenan personalisa", "Seguimiento ROI", "Analítika prediktivo"],
          demo: "Mira dashboard di analítika di muestra"
        },
        {
          icon: Mail,
          title: "Automatisashon di Email",
          description: "Kampañanan di email personalisa ku ta konvertí",
          features: ["Segmentashon inteligente", "Pruebanan A/B", "Kampañanan goteo", "Seguimiento di rendimento"],
          demo: "Krea sekuensia automatisa di emails di bienvenida"
        },
        {
          icon: Image,
          title: "Kreador Visual",
          description: "Imagennan y gráfikonan generá pa AI",
          features: ["Gráfikonan personalisa", "Konsistensia di marka", "Múltiple formato", "Generashon instantáneo"],
          demo: "Genera un banner di marketing ku tema tropikal"
        },
        {
          icon: Video,
          title: "Produktor di Video",
          description: "Videonan profesional sin komplikashon",
          features: ["Biblioteca di template", "Auto-edishon", "Síntesis di bos", "Eksportashon multiplataforma"],
          demo: "Krea un video di showcase di produkto di 30 segundo"
        }
      ]
    },
    nl: {
      title: "Krachtige AI Tools",
      subtitle: "Alles wat je nodig hebt om je marketing te versterken",
      description: "Onze uitgebreide suite van AI-gedreven tools helpt je bij het creëren, optimaliseren en automatiseren van je marketinginspanningen met professionele resultaten.",
      tryDemo: "Probeer Demo",
      learnMore: "Meer Leren",
      tools: [
        {
          icon: MessageSquare,
          title: "AI Chatbot",
          description: "Intelligente klantenservice die nooit slaapt",
          features: ["24/7 beschikbaarheid", "Meertalige ondersteuning", "Slimme antwoorden", "Lead generatie"],
          demo: "Chat nu met onze AI-assistent!"
        },
        {
          icon: PenTool,
          title: "Content Generator",
          description: "Creëer boeiende content in seconden",
          features: ["Blog posts", "Social media", "Email campagnes", "Advertentietekst"],
          demo: "Genereer een social media post over tropische marketing"
        },
        {
          icon: BarChart3,
          title: "Analytics Dashboard",
          description: "Diepgaande inzichten in je marketingprestaties",
          features: ["Real-time data", "Aangepaste rapporten", "ROI tracking", "Voorspellende analytics"],
          demo: "Bekijk voorbeeld analytics dashboard"
        },
        {
          icon: Mail,
          title: "Email Automatisering",
          description: "Gepersonaliseerde email campagnes die converteren",
          features: ["Slimme segmentatie", "A/B testing", "Drip campagnes", "Prestatie tracking"],
          demo: "Creëer een geautomatiseerde welkomst email reeks"
        },
        {
          icon: Image,
          title: "Visuele Creator",
          description: "AI-gegenereerde afbeeldingen en graphics",
          features: ["Aangepaste graphics", "Merkconsistentie", "Meerdere formaten", "Instant generatie"],
          demo: "Genereer een tropisch-thema marketing banner"
        },
        {
          icon: Video,
          title: "Video Producer",
          description: "Professionele video's zonder complexiteit",
          features: ["Template bibliotheek", "Auto-editing", "Spraaksynthese", "Multi-platform export"],
          demo: "Creëer een 30-seconden product showcase video"
        }
      ]
    }
  };

  const t = translations[language] || translations.en;

  const handleDemoClick = (index) => {
    setActiveDemo(activeDemo === index ? null : index);
  };

  return (
    <section id="tools" className="py-20 relative overflow-hidden">
      {/* Background Elements */}
      <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-primary/5 via-transparent to-accent/5"></div>
      
      <div className="container mx-auto px-4 relative z-10">
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="flex items-center justify-center space-x-2 text-primary mb-4">
            <Sparkles className="w-5 h-5" />
            <span className="text-sm font-medium uppercase tracking-wider">
              AI-Powered Solutions
            </span>
          </div>
          <h2 className="text-3xl md:text-5xl font-bold mb-6">
            <span className="tropical-text-gradient">{t.title}</span>
          </h2>
          <p className="text-xl text-muted-foreground mb-4">{t.subtitle}</p>
          <p className="text-muted-foreground">{t.description}</p>
        </div>

        {/* Tools Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {t.tools.map((tool, index) => {
            const IconComponent = tool.icon;
            const isActive = activeDemo === index;
            
            return (
              <Card key={index} className={`hover-lift transition-all duration-300 ${isActive ? 'ring-2 ring-primary shadow-2xl' : ''}`}>
                <CardHeader>
                  <div className="flex items-center space-x-4">
                    <div className="w-12 h-12 tropical-gradient rounded-xl flex items-center justify-center">
                      <IconComponent className="w-6 h-6 text-white" />
                    </div>
                    <div>
                      <CardTitle className="text-lg">{tool.title}</CardTitle>
                      <CardDescription>{tool.description}</CardDescription>
                    </div>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  {/* Features */}
                  <div className="grid grid-cols-2 gap-2">
                    {tool.features.map((feature, featureIndex) => (
                      <div key={featureIndex} className="flex items-center space-x-2 text-sm">
                        <div className="w-1.5 h-1.5 bg-primary rounded-full"></div>
                        <span className="text-muted-foreground">{feature}</span>
                      </div>
                    ))}
                  </div>

                  {/* Demo Section */}
                  {isActive && (
                    <div className="bg-muted/50 rounded-lg p-4 border-l-4 border-primary animate-in slide-in-from-top-2 duration-300">
                      <div className="flex items-center space-x-2 mb-2">
                        <Play className="w-4 h-4 text-primary" />
                        <span className="text-sm font-medium text-primary">Demo Preview</span>
                      </div>
                      <p className="text-sm text-muted-foreground">{tool.demo}</p>
                    </div>
                  )}

                  {/* Action Buttons */}
                  <div className="flex space-x-2 pt-2">
                    <Button 
                      size="sm" 
                      onClick={() => handleDemoClick(index)}
                      className={`flex-1 ${isActive ? 'tropical-gradient text-white' : ''}`}
                      variant={isActive ? 'default' : 'outline'}
                    >
                      {t.tryDemo}
                      <Play className="w-4 h-4 ml-2" />
                    </Button>
                    <Button size="sm" variant="ghost" className="flex-1">
                      {t.learnMore}
                      <ArrowRight className="w-4 h-4 ml-2" />
                    </Button>
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>

        {/* Bottom CTA */}
        <div className="text-center mt-16">
          <div className="bg-card border rounded-3xl p-8 max-w-2xl mx-auto glass-effect">
            <h3 className="text-2xl font-bold mb-4">
              {language === 'es' ? 'Listo para comenzar?' :
               language === 'pap' ? 'Kla pa kuminsá?' :
               language === 'nl' ? 'Klaar om te beginnen?' :
               'Ready to get started?'}
            </h3>
            <p className="text-muted-foreground mb-6">
              {language === 'es' ? 'Únete a miles de empresas que ya están usando nuestras herramientas de IA.' :
               language === 'pap' ? 'Únete ku miles di kompañia ku ya ta usando nos hermentnan di AI.' :
               language === 'nl' ? 'Sluit je aan bij duizenden bedrijven die al onze AI-tools gebruiken.' :
               'Join thousands of businesses already using our AI tools.'}
            </p>
            <Button size="lg" className="tropical-gradient text-white hover:opacity-90 pulse-glow">
              {language === 'es' ? 'Comenzar Gratis' :
               language === 'pap' ? 'Kuminsá Gratis' :
               language === 'nl' ? 'Gratis Beginnen' :
               'Start Free Trial'}
              <ArrowRight className="w-5 h-5 ml-2" />
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AIToolsShowcase;

