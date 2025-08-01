import { useState } from 'react';
import { Button } from '@/components/ui/button.jsx';
import { Menu, X, Globe, MessageCircle } from 'lucide-react';

const Header = ({ language, setLanguage, openChatbot }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const languages = [
    { code: 'en', name: 'English', flag: '🇺🇸' },
    { code: 'es', name: 'Español', flag: '🇪🇸' },
    { code: 'pap', name: 'Papiamentu', flag: '🇨🇼' },
    { code: 'nl', name: 'Nederlands', flag: '🇳🇱' }
  ];

  const translations = {
    en: {
      home: 'Home',
      tools: 'AI Tools',
      pricing: 'Pricing',
      about: 'About',
      contact: 'Contact',
      getStarted: 'Get Started',
      chat: 'Chat with AI'
    },
    es: {
      home: 'Inicio',
      tools: 'Herramientas IA',
      pricing: 'Precios',
      about: 'Acerca de',
      contact: 'Contacto',
      getStarted: 'Comenzar',
      chat: 'Chat con IA'
    },
    pap: {
      home: 'Kas',
      tools: 'Hermentnan AI',
      pricing: 'Preis',
      about: 'Tokante',
      contact: 'Kontakto',
      getStarted: 'Kuminsá',
      chat: 'Chat ku AI'
    },
    nl: {
      home: 'Home',
      tools: 'AI Tools',
      pricing: 'Prijzen',
      about: 'Over ons',
      contact: 'Contact',
      getStarted: 'Begin',
      chat: 'Chat met AI'
    }
  };

  const t = translations[language] || translations.en;

  return (
    <header className="fixed top-0 left-0 right-0 z-50 glass-effect">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <div className="flex items-center space-x-2">
            <div className="w-10 h-10 tropical-gradient rounded-lg flex items-center justify-center">
              <MessageCircle className="w-6 h-6 text-white" />
            </div>
            <span className="text-xl font-bold tropical-text-gradient">
              AI Marketing Tools
            </span>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <a href="#home" className="text-foreground hover:text-primary transition-colors">
              {t.home}
            </a>
            <a href="#tools" className="text-foreground hover:text-primary transition-colors">
              {t.tools}
            </a>
            <a href="#pricing" className="text-foreground hover:text-primary transition-colors">
              {t.pricing}
            </a>
            <a href="#about" className="text-foreground hover:text-primary transition-colors">
              {t.about}
            </a>
            <a href="#contact" className="text-foreground hover:text-primary transition-colors">
              {t.contact}
            </a>
          </nav>

          {/* Language Switcher & CTA */}
          <div className="hidden md:flex items-center space-x-4">
            <div className="relative group">
              <Button variant="outline" size="sm" className="flex items-center space-x-2">
                <Globe className="w-4 h-4" />
                <span>{languages.find(l => l.code === language)?.flag}</span>
              </Button>
              <div className="absolute top-full right-0 mt-2 w-48 bg-card border rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                {languages.map((lang) => (
                  <button
                    key={lang.code}
                    onClick={() => setLanguage(lang.code)}
                    className="w-full px-4 py-2 text-left hover:bg-muted flex items-center space-x-2 first:rounded-t-lg last:rounded-b-lg"
                  >
                    <span>{lang.flag}</span>
                    <span>{lang.name}</span>
                  </button>
                ))}
              </div>
            </div>
            <Button onClick={openChatbot} className="tropical-gradient text-white hover:opacity-90">
              {t.chat}
            </Button>
            <Button className="tropical-gradient text-white hover:opacity-90 pulse-glow">
              {t.getStarted}
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <Button
            variant="ghost"
            size="sm"
            className="md:hidden"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </Button>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden mt-4 pb-4 border-t border-border">
            <nav className="flex flex-col space-y-4 mt-4">
              <a href="#home" className="text-foreground hover:text-primary transition-colors">
                {t.home}
              </a>
              <a href="#tools" className="text-foreground hover:text-primary transition-colors">
                {t.tools}
              </a>
              <a href="#pricing" className="text-foreground hover:text-primary transition-colors">
                {t.pricing}
              </a>
              <a href="#about" className="text-foreground hover:text-primary transition-colors">
                {t.about}
              </a>
              <a href="#contact" className="text-foreground hover:text-primary transition-colors">
                {t.contact}
              </a>
              <div className="flex flex-col space-y-2 pt-4">
                <div className="flex items-center space-x-2">
                  <Globe className="w-4 h-4" />
                  <span className="text-sm font-medium">Language:</span>
                </div>
                <div className="flex flex-wrap gap-2">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => setLanguage(lang.code)}
                      className={`px-3 py-1 rounded-md text-sm flex items-center space-x-1 ${
                        language === lang.code 
                          ? 'bg-primary text-primary-foreground' 
                          : 'bg-muted hover:bg-muted/80'
                      }`}
                    >
                      <span>{lang.flag}</span>
                      <span>{lang.name}</span>
                    </button>
                  ))}
                </div>
                <Button onClick={openChatbot} className="tropical-gradient text-white hover:opacity-90 mt-2">
                  {t.chat}
                </Button>
                <Button className="tropical-gradient text-white hover:opacity-90 pulse-glow">
                  {t.getStarted}
                </Button>
              </div>
            </nav>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;

