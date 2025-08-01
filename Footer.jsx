import { Button } from '@/components/ui/button.jsx';
import { 
  MessageCircle, 
  Mail, 
  Phone, 
  MapPin,
  Facebook,
  Twitter,
  Instagram,
  Linkedin,
  Youtube,
  ArrowRight,
  Heart
} from 'lucide-react';

const Footer = ({ language }) => {
  const translations = {
    en: {
      company: "AI Marketing Tools",
      tagline: "Empowering businesses with intelligent marketing solutions",
      quickLinks: "Quick Links",
      products: "Products",
      support: "Support",
      legal: "Legal",
      contact: "Contact Us",
      newsletter: "Newsletter",
      newsletterText: "Stay updated with our latest features and marketing tips",
      subscribe: "Subscribe",
      emailPlaceholder: "Enter your email",
      address: "123 Business Ave, Tech City, TC 12345",
      phone: "+1 (555) 123-4567",
      email: "hello@aimarketingtools.com",
      copyright: "All rights reserved.",
      madeWith: "Made with",
      links: {
        home: "Home",
        tools: "AI Tools",
        pricing: "Pricing",
        about: "About Us",
        blog: "Blog",
        careers: "Careers",
        helpCenter: "Help Center",
        documentation: "Documentation",
        community: "Community",
        status: "Status",
        privacy: "Privacy Policy",
        terms: "Terms of Service",
        cookies: "Cookie Policy",
        security: "Security"
      }
    },
    es: {
      company: "Herramientas de Marketing IA",
      tagline: "Empoderando empresas con soluciones de marketing inteligentes",
      quickLinks: "Enlaces Rápidos",
      products: "Productos",
      support: "Soporte",
      legal: "Legal",
      contact: "Contáctanos",
      newsletter: "Boletín",
      newsletterText: "Mantente actualizado con nuestras últimas funciones y consejos de marketing",
      subscribe: "Suscribirse",
      emailPlaceholder: "Ingresa tu email",
      address: "123 Avenida Empresarial, Ciudad Tech, TC 12345",
      phone: "+1 (555) 123-4567",
      email: "hola@herramientasmarketingia.com",
      copyright: "Todos los derechos reservados.",
      madeWith: "Hecho con",
      links: {
        home: "Inicio",
        tools: "Herramientas IA",
        pricing: "Precios",
        about: "Acerca de",
        blog: "Blog",
        careers: "Carreras",
        helpCenter: "Centro de Ayuda",
        documentation: "Documentación",
        community: "Comunidad",
        status: "Estado",
        privacy: "Política de Privacidad",
        terms: "Términos de Servicio",
        cookies: "Política de Cookies",
        security: "Seguridad"
      }
    },
    pap: {
      company: "Hermentnan di Marketing AI",
      tagline: "Empoderando negoshinan ku solushonnan di marketing inteligente",
      quickLinks: "Link Rápido",
      products: "Produktonan",
      support: "Soporte",
      legal: "Legal",
      contact: "Kontaktanos",
      newsletter: "Newsletter",
      newsletterText: "Keda aktualisa ku nos último funshonnan y konseho di marketing",
      subscribe: "Suskribí",
      emailPlaceholder: "Pone bo email",
      address: "123 Avenida Empresarial, Ciudad Tech, TC 12345",
      phone: "+1 (555) 123-4567",
      email: "hola@hermentnanmarketingai.com",
      copyright: "Tur derecho reservá.",
      madeWith: "Hasi ku",
      links: {
        home: "Kas",
        tools: "Hermentnan AI",
        pricing: "Preis",
        about: "Tokante Nos",
        blog: "Blog",
        careers: "Karera",
        helpCenter: "Sentro di Yudansa",
        documentation: "Dokumentashon",
        community: "Komunidat",
        status: "Estado",
        privacy: "Polítika di Privashon",
        terms: "Términonan di Servisio",
        cookies: "Polítika di Cookie",
        security: "Seguridat"
      }
    },
    nl: {
      company: "AI Marketing Tools",
      tagline: "Bedrijven versterken met intelligente marketingoplossingen",
      quickLinks: "Snelle Links",
      products: "Producten",
      support: "Ondersteuning",
      legal: "Juridisch",
      contact: "Contact",
      newsletter: "Nieuwsbrief",
      newsletterText: "Blijf op de hoogte van onze nieuwste functies en marketingtips",
      subscribe: "Abonneren",
      emailPlaceholder: "Voer je email in",
      address: "123 Business Ave, Tech City, TC 12345",
      phone: "+1 (555) 123-4567",
      email: "hallo@aimarketingtools.com",
      copyright: "Alle rechten voorbehouden.",
      madeWith: "Gemaakt met",
      links: {
        home: "Home",
        tools: "AI Tools",
        pricing: "Prijzen",
        about: "Over Ons",
        blog: "Blog",
        careers: "Carrières",
        helpCenter: "Helpcentrum",
        documentation: "Documentatie",
        community: "Gemeenschap",
        status: "Status",
        privacy: "Privacybeleid",
        terms: "Servicevoorwaarden",
        cookies: "Cookiebeleid",
        security: "Beveiliging"
      }
    }
  };

  const t = translations[language] || translations.en;

  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-card border-t">
      <div className="container mx-auto px-4 py-16">
        <div className="grid lg:grid-cols-5 md:grid-cols-3 gap-8">
          {/* Company Info */}
          <div className="lg:col-span-2 space-y-6">
            <div className="space-y-4">
              <div className="flex items-center space-x-2">
                <div className="w-10 h-10 tropical-gradient rounded-lg flex items-center justify-center">
                  <MessageCircle className="w-6 h-6 text-white" />
                </div>
                <span className="text-xl font-bold tropical-text-gradient">
                  {t.company}
                </span>
              </div>
              <p className="text-muted-foreground max-w-md">
                {t.tagline}
              </p>
            </div>

            {/* Contact Info */}
            <div className="space-y-3">
              <div className="flex items-center space-x-3 text-sm">
                <MapPin className="w-4 h-4 text-primary" />
                <span className="text-muted-foreground">{t.address}</span>
              </div>
              <div className="flex items-center space-x-3 text-sm">
                <Phone className="w-4 h-4 text-primary" />
                <span className="text-muted-foreground">{t.phone}</span>
              </div>
              <div className="flex items-center space-x-3 text-sm">
                <Mail className="w-4 h-4 text-primary" />
                <span className="text-muted-foreground">{t.email}</span>
              </div>
            </div>

            {/* Social Links */}
            <div className="flex space-x-4">
              {[Facebook, Twitter, Instagram, Linkedin, Youtube].map((Icon, index) => (
                <a
                  key={index}
                  href="#"
                  className="w-10 h-10 bg-muted hover:bg-primary hover:text-primary-foreground rounded-lg flex items-center justify-center transition-colors"
                >
                  <Icon className="w-5 h-5" />
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h3 className="font-semibold">{t.quickLinks}</h3>
            <div className="space-y-3">
              {Object.entries(t.links).slice(0, 5).map(([key, value]) => (
                <a
                  key={key}
                  href={`#${key === 'home' ? 'home' : key}`}
                  className="block text-sm text-muted-foreground hover:text-primary transition-colors"
                >
                  {value}
                </a>
              ))}
            </div>
          </div>

          {/* Products */}
          <div className="space-y-4">
            <h3 className="font-semibold">{t.products}</h3>
            <div className="space-y-3">
              {Object.entries(t.links).slice(5, 10).map(([key, value]) => (
                <a
                  key={key}
                  href="#"
                  className="block text-sm text-muted-foreground hover:text-primary transition-colors"
                >
                  {value}
                </a>
              ))}
            </div>
          </div>

          {/* Support & Legal */}
          <div className="space-y-6">
            <div className="space-y-4">
              <h3 className="font-semibold">{t.support}</h3>
              <div className="space-y-3">
                {Object.entries(t.links).slice(10, 14).map(([key, value]) => (
                  <a
                    key={key}
                    href="#"
                    className="block text-sm text-muted-foreground hover:text-primary transition-colors"
                  >
                    {value}
                  </a>
                ))}
              </div>
            </div>

            <div className="space-y-4">
              <h3 className="font-semibold">{t.legal}</h3>
              <div className="space-y-3">
                {Object.entries(t.links).slice(14).map(([key, value]) => (
                  <a
                    key={key}
                    href="#"
                    className="block text-sm text-muted-foreground hover:text-primary transition-colors"
                  >
                    {value}
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Newsletter Section */}
        <div className="mt-16 pt-8 border-t">
          <div className="max-w-2xl mx-auto text-center space-y-6">
            <div>
              <h3 className="text-2xl font-bold mb-2">{t.newsletter}</h3>
              <p className="text-muted-foreground">{t.newsletterText}</p>
            </div>
            
            <div className="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
              <input
                type="email"
                placeholder={t.emailPlaceholder}
                className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              />
              <Button className="tropical-gradient text-white hover:opacity-90">
                {t.subscribe}
                <ArrowRight className="w-4 h-4 ml-2" />
              </Button>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-16 pt-8 border-t flex flex-col md:flex-row items-center justify-between space-y-4 md:space-y-0">
          <div className="flex items-center space-x-2 text-sm text-muted-foreground">
            <span>© {currentYear} {t.company}. {t.copyright}</span>
          </div>
          
          <div className="flex items-center space-x-2 text-sm text-muted-foreground">
            <span>{t.madeWith}</span>
            <Heart className="w-4 h-4 text-red-500 fill-current" />
            <span>
              {language === 'es' ? 'en Curaçao' :
               language === 'pap' ? 'na Kòrsou' :
               language === 'nl' ? 'in Curaçao' :
               'in Curaçao'}
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

