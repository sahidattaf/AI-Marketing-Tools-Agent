import { useState } from 'react';
import { Button } from '@/components/ui/button.jsx';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx';
import { Badge } from '@/components/ui/badge.jsx';
import { 
  Check, 
  X, 
  Star, 
  Zap, 
  Crown,
  ArrowRight,
  CreditCard,
  Shield,
  Sparkles
} from 'lucide-react';

const PricingSection = ({ language }) => {
  const [billingCycle, setBillingCycle] = useState('monthly');

  const translations = {
    en: {
      title: "Simple, Transparent Pricing",
      subtitle: "Choose the perfect plan for your business",
      description: "Start free, upgrade when you're ready. All plans include our core AI features.",
      monthly: "Monthly",
      yearly: "Yearly",
      yearlyDiscount: "Save 20%",
      mostPopular: "Most Popular",
      getStarted: "Get Started",
      choosePlan: "Choose Plan",
      contactSales: "Contact Sales",
      features: "Everything in",
      unlimited: "Unlimited",
      support: "Priority Support",
      analytics: "Advanced Analytics",
      customization: "Custom Branding",
      integration: "API Integration",
      training: "Team Training",
      plans: [
        {
          name: "Starter",
          description: "Perfect for small businesses getting started",
          monthlyPrice: 0,
          yearlyPrice: 0,
          features: [
            "AI Chatbot (100 conversations/month)",
            "Basic Content Generator",
            "Email Support",
            "Standard Templates",
            "Basic Analytics"
          ],
          limitations: [
            "Limited customization",
            "Basic integrations only"
          ],
          cta: "Start Free",
          popular: false
        },
        {
          name: "Professional",
          description: "Best for growing businesses",
          monthlyPrice: 49,
          yearlyPrice: 39,
          features: [
            "AI Chatbot (1,000 conversations/month)",
            "Advanced Content Generator",
            "Priority Email Support",
            "Premium Templates",
            "Advanced Analytics",
            "Custom Branding",
            "API Access",
            "A/B Testing"
          ],
          limitations: [],
          cta: "Start Trial",
          popular: true
        },
        {
          name: "Enterprise",
          description: "For large organizations with custom needs",
          monthlyPrice: 199,
          yearlyPrice: 159,
          features: [
            "Unlimited AI Conversations",
            "Full Content Suite",
            "24/7 Phone & Chat Support",
            "Custom Templates",
            "Enterprise Analytics",
            "White-label Solution",
            "Full API Access",
            "Advanced Integrations",
            "Dedicated Account Manager",
            "Custom Training"
          ],
          limitations: [],
          cta: "Contact Sales",
          popular: false
        }
      ]
    },
    es: {
      title: "Precios Simples y Transparentes",
      subtitle: "Elige el plan perfecto para tu negocio",
      description: "Comienza gratis, actualiza cuando estés listo. Todos los planes incluyen nuestras funciones principales de IA.",
      monthly: "Mensual",
      yearly: "Anual",
      yearlyDiscount: "Ahorra 20%",
      mostPopular: "Más Popular",
      getStarted: "Comenzar",
      choosePlan: "Elegir Plan",
      contactSales: "Contactar Ventas",
      features: "Todo en",
      unlimited: "Ilimitado",
      support: "Soporte Prioritario",
      analytics: "Análisis Avanzado",
      customization: "Marca Personalizada",
      integration: "Integración API",
      training: "Entrenamiento del Equipo",
      plans: [
        {
          name: "Inicial",
          description: "Perfecto para pequeñas empresas que comienzan",
          monthlyPrice: 0,
          yearlyPrice: 0,
          features: [
            "Chatbot IA (100 conversaciones/mes)",
            "Generador de Contenido Básico",
            "Soporte por Email",
            "Plantillas Estándar",
            "Análisis Básico"
          ],
          limitations: [
            "Personalización limitada",
            "Solo integraciones básicas"
          ],
          cta: "Comenzar Gratis",
          popular: false
        },
        {
          name: "Profesional",
          description: "Mejor para empresas en crecimiento",
          monthlyPrice: 49,
          yearlyPrice: 39,
          features: [
            "Chatbot IA (1,000 conversaciones/mes)",
            "Generador de Contenido Avanzado",
            "Soporte Prioritario por Email",
            "Plantillas Premium",
            "Análisis Avanzado",
            "Marca Personalizada",
            "Acceso API",
            "Pruebas A/B"
          ],
          limitations: [],
          cta: "Iniciar Prueba",
          popular: true
        },
        {
          name: "Empresarial",
          description: "Para grandes organizaciones con necesidades personalizadas",
          monthlyPrice: 199,
          yearlyPrice: 159,
          features: [
            "Conversaciones IA Ilimitadas",
            "Suite Completa de Contenido",
            "Soporte 24/7 por Teléfono y Chat",
            "Plantillas Personalizadas",
            "Análisis Empresarial",
            "Solución de Marca Blanca",
            "Acceso Completo API",
            "Integraciones Avanzadas",
            "Gerente de Cuenta Dedicado",
            "Entrenamiento Personalizado"
          ],
          limitations: [],
          cta: "Contactar Ventas",
          popular: false
        }
      ]
    },
    pap: {
      title: "Preis Simpel y Transparente",
      subtitle: "Skoge e plan perfekto pa bo negoshi",
      description: "Kuminsá gratis, aktualisa ora bo ta kla. Tur plannan tin nos funshonnan prinsipal di AI.",
      monthly: "Pa Luna",
      yearly: "Pa Aña",
      yearlyDiscount: "Spaar 20%",
      mostPopular: "Mas Popular",
      getStarted: "Kuminsá",
      choosePlan: "Skoge Plan",
      contactSales: "Kontakta Venta",
      features: "Tur kos den",
      unlimited: "Sin Límite",
      support: "Soporte Prioritario",
      analytics: "Analítika Avansá",
      customization: "Marka Personalisa",
      integration: "Integrashon API",
      training: "Entrenamento di Ekipo",
      plans: [
        {
          name: "Kuminsa",
          description: "Perfekto pa negoshi chikí ku ta kuminsá",
          monthlyPrice: 0,
          yearlyPrice: 0,
          features: [
            "Chatbot AI (100 konversashon/luna)",
            "Generador di Kontenido Básiko",
            "Soporte pa Email",
            "Template Estándar",
            "Analítika Básiko"
          ],
          limitations: [
            "Personalisashon limitá",
            "Solo integrashonnan básiko"
          ],
          cta: "Kuminsá Gratis",
          popular: false
        },
        {
          name: "Profesional",
          description: "Miho pa negoshinan ku ta krece",
          monthlyPrice: 49,
          yearlyPrice: 39,
          features: [
            "Chatbot AI (1,000 konversashon/luna)",
            "Generador di Kontenido Avansá",
            "Soporte Prioritario pa Email",
            "Template Premium",
            "Analítika Avansá",
            "Marka Personalisa",
            "Akeso API",
            "Prueba A/B"
          ],
          limitations: [],
          cta: "Kuminsá Prueba",
          popular: true
        },
        {
          name: "Empresarial",
          description: "Pa organisashonnan grandi ku nesesidat personalisa",
          monthlyPrice: 199,
          yearlyPrice: 159,
          features: [
            "Konversashonnan AI Sin Límite",
            "Suite Kompleto di Kontenido",
            "Soporte 24/7 pa Telefon y Chat",
            "Template Personalisa",
            "Analítika Empresarial",
            "Solushon di Marka Blanku",
            "Akeso Kompleto API",
            "Integrashonnan Avansá",
            "Gerente di Kuenta Dediká",
            "Entrenamento Personalisa"
          ],
          limitations: [],
          cta: "Kontakta Venta",
          popular: false
        }
      ]
    },
    nl: {
      title: "Eenvoudige, Transparante Prijzen",
      subtitle: "Kies het perfecte plan voor je bedrijf",
      description: "Begin gratis, upgrade wanneer je er klaar voor bent. Alle plannen bevatten onze kern AI-functies.",
      monthly: "Maandelijks",
      yearly: "Jaarlijks",
      yearlyDiscount: "Bespaar 20%",
      mostPopular: "Meest Populair",
      getStarted: "Begin",
      choosePlan: "Kies Plan",
      contactSales: "Contact Verkoop",
      features: "Alles in",
      unlimited: "Onbeperkt",
      support: "Prioriteit Ondersteuning",
      analytics: "Geavanceerde Analytics",
      customization: "Aangepaste Branding",
      integration: "API Integratie",
      training: "Team Training",
      plans: [
        {
          name: "Starter",
          description: "Perfect voor kleine bedrijven die beginnen",
          monthlyPrice: 0,
          yearlyPrice: 0,
          features: [
            "AI Chatbot (100 gesprekken/maand)",
            "Basis Content Generator",
            "Email Ondersteuning",
            "Standaard Templates",
            "Basis Analytics"
          ],
          limitations: [
            "Beperkte aanpassing",
            "Alleen basis integraties"
          ],
          cta: "Start Gratis",
          popular: false
        },
        {
          name: "Professioneel",
          description: "Best voor groeiende bedrijven",
          monthlyPrice: 49,
          yearlyPrice: 39,
          features: [
            "AI Chatbot (1,000 gesprekken/maand)",
            "Geavanceerde Content Generator",
            "Prioriteit Email Ondersteuning",
            "Premium Templates",
            "Geavanceerde Analytics",
            "Aangepaste Branding",
            "API Toegang",
            "A/B Testing"
          ],
          limitations: [],
          cta: "Start Proefperiode",
          popular: true
        },
        {
          name: "Enterprise",
          description: "Voor grote organisaties met aangepaste behoeften",
          monthlyPrice: 199,
          yearlyPrice: 159,
          features: [
            "Onbeperkte AI Gesprekken",
            "Volledige Content Suite",
            "24/7 Telefoon & Chat Ondersteuning",
            "Aangepaste Templates",
            "Enterprise Analytics",
            "White-label Oplossing",
            "Volledige API Toegang",
            "Geavanceerde Integraties",
            "Toegewijde Account Manager",
            "Aangepaste Training"
          ],
          limitations: [],
          cta: "Contact Verkoop",
          popular: false
        }
      ]
    }
  };

  const t = translations[language] || translations.en;

  const handlePlanSelect = (plan) => {
    // This would integrate with payment processing
    console.log(`Selected plan: ${plan.name}`);
    // For demo purposes, we'll just show an alert
    alert(`${language === 'es' ? 'Plan seleccionado' : language === 'pap' ? 'Plan skohe' : language === 'nl' ? 'Plan geselecteerd' : 'Plan selected'}: ${plan.name}`);
  };

  return (
    <section id="pricing" className="py-20 relative overflow-hidden">
      {/* Background Elements */}
      <div className="absolute inset-0 bg-gradient-to-br from-secondary/10 via-transparent to-primary/10"></div>
      
      <div className="container mx-auto px-4 relative z-10">
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="flex items-center justify-center space-x-2 text-primary mb-4">
            <CreditCard className="w-5 h-5" />
            <span className="text-sm font-medium uppercase tracking-wider">
              Pricing Plans
            </span>
          </div>
          <h2 className="text-3xl md:text-5xl font-bold mb-6">
            <span className="tropical-text-gradient">{t.title}</span>
          </h2>
          <p className="text-xl text-muted-foreground mb-4">{t.subtitle}</p>
          <p className="text-muted-foreground">{t.description}</p>
        </div>

        {/* Billing Toggle */}
        <div className="flex items-center justify-center mb-12">
          <div className="bg-muted rounded-lg p-1 flex">
            <button
              onClick={() => setBillingCycle('monthly')}
              className={`px-6 py-2 rounded-md text-sm font-medium transition-all ${
                billingCycle === 'monthly'
                  ? 'bg-card text-foreground shadow-sm'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              {t.monthly}
            </button>
            <button
              onClick={() => setBillingCycle('yearly')}
              className={`px-6 py-2 rounded-md text-sm font-medium transition-all flex items-center space-x-2 ${
                billingCycle === 'yearly'
                  ? 'bg-card text-foreground shadow-sm'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              <span>{t.yearly}</span>
              <Badge variant="secondary" className="text-xs bg-accent text-accent-foreground">
                {t.yearlyDiscount}
              </Badge>
            </button>
          </div>
        </div>

        {/* Pricing Cards */}
        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {t.plans.map((plan, index) => {
            const price = billingCycle === 'yearly' ? plan.yearlyPrice : plan.monthlyPrice;
            const isEnterprise = index === 2;
            
            return (
              <Card 
                key={index} 
                className={`relative hover-lift transition-all duration-300 ${
                  plan.popular 
                    ? 'ring-2 ring-primary shadow-2xl scale-105' 
                    : ''
                } ${isEnterprise ? 'bg-gradient-to-br from-card to-muted/50' : ''}`}
              >
                {plan.popular && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                    <Badge className="tropical-gradient text-white px-4 py-1">
                      <Star className="w-3 h-3 mr-1" />
                      {t.mostPopular}
                    </Badge>
                  </div>
                )}

                <CardHeader className="text-center pb-8">
                  <div className="flex items-center justify-center mb-4">
                    <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
                      index === 0 ? 'bg-muted' :
                      index === 1 ? 'tropical-gradient' :
                      'bg-gradient-to-br from-primary to-accent'
                    }`}>
                      {index === 0 ? <Zap className="w-6 h-6 text-muted-foreground" /> :
                       index === 1 ? <Sparkles className="w-6 h-6 text-white" /> :
                       <Crown className="w-6 h-6 text-white" />}
                    </div>
                  </div>
                  <CardTitle className="text-2xl">{plan.name}</CardTitle>
                  <CardDescription className="text-base">{plan.description}</CardDescription>
                  
                  <div className="mt-6">
                    <div className="flex items-baseline justify-center">
                      <span className="text-4xl font-bold">
                        ${price}
                      </span>
                      <span className="text-muted-foreground ml-1">
                        /{billingCycle === 'yearly' ? 'year' : 'month'}
                      </span>
                    </div>
                    {billingCycle === 'yearly' && plan.monthlyPrice > 0 && (
                      <p className="text-sm text-muted-foreground mt-1">
                        ${plan.monthlyPrice}/month billed annually
                      </p>
                    )}
                  </div>
                </CardHeader>

                <CardContent className="space-y-6">
                  {/* Features */}
                  <div className="space-y-3">
                    {plan.features.map((feature, featureIndex) => (
                      <div key={featureIndex} className="flex items-start space-x-3">
                        <Check className="w-5 h-5 text-primary mt-0.5 flex-shrink-0" />
                        <span className="text-sm">{feature}</span>
                      </div>
                    ))}
                    {plan.limitations.map((limitation, limitIndex) => (
                      <div key={limitIndex} className="flex items-start space-x-3 opacity-60">
                        <X className="w-5 h-5 text-muted-foreground mt-0.5 flex-shrink-0" />
                        <span className="text-sm text-muted-foreground">{limitation}</span>
                      </div>
                    ))}
                  </div>

                  {/* CTA Button */}
                  <Button
                    onClick={() => handlePlanSelect(plan)}
                    className={`w-full ${
                      plan.popular 
                        ? 'tropical-gradient text-white hover:opacity-90 pulse-glow' 
                        : isEnterprise
                        ? 'bg-gradient-to-r from-primary to-accent text-white hover:opacity-90'
                        : ''
                    }`}
                    variant={plan.popular || isEnterprise ? 'default' : 'outline'}
                    size="lg"
                  >
                    {plan.cta}
                    <ArrowRight className="w-4 h-4 ml-2" />
                  </Button>

                  {/* Security Badge */}
                  {index > 0 && (
                    <div className="flex items-center justify-center space-x-2 text-xs text-muted-foreground pt-4">
                      <Shield className="w-4 h-4" />
                      <span>
                        {language === 'es' ? 'Pago seguro con SSL' :
                         language === 'pap' ? 'Pago sigur ku SSL' :
                         language === 'nl' ? 'Veilige betaling met SSL' :
                         'Secure payment with SSL'}
                      </span>
                    </div>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </div>

        {/* Bottom CTA */}
        <div className="text-center mt-16">
          <div className="bg-card border rounded-3xl p-8 max-w-2xl mx-auto glass-effect">
            <h3 className="text-2xl font-bold mb-4">
              {language === 'es' ? '¿Necesitas algo personalizado?' :
               language === 'pap' ? 'Bo mester algu personalisa?' :
               language === 'nl' ? 'Heb je iets aangepasts nodig?' :
               'Need something custom?'}
            </h3>
            <p className="text-muted-foreground mb-6">
              {language === 'es' ? 'Hablemos sobre una solución empresarial personalizada para tu organización.' :
               language === 'pap' ? 'Laga nos papia tokante un solushon empresarial personalisa pa bo organisashon.' :
               language === 'nl' ? 'Laten we praten over een aangepaste enterprise oplossing voor je organisatie.' :
               'Let\'s talk about a custom enterprise solution for your organization.'}
            </p>
            <Button size="lg" variant="outline" className="hover-lift">
              {language === 'es' ? 'Contactar Ventas' :
               language === 'pap' ? 'Kontakta Venta' :
               language === 'nl' ? 'Contact Verkoop' :
               'Contact Sales'}
              <ArrowRight className="w-5 h-5 ml-2" />
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default PricingSection;

