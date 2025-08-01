import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, TouchableOpacity, SafeAreaView } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

// Mock components for the mobile app
const Header = ({ language, setLanguage, openChatbot }) => {
  const languages = [
    { code: 'en', name: 'English', flag: '🇺🇸' },
    { code: 'es', name: 'Español', flag: '🇪🇸' },
    { code: 'pap', name: 'Papiamentu', flag: '🇨🇼' },
    { code: 'nl', name: 'Nederlands', flag: '🇳🇱' }
  ];

  const translations = {
    en: { title: 'AI Marketing Tools', chat: 'Chat with AI' },
    es: { title: 'Herramientas IA', chat: 'Chat con IA' },
    pap: { title: 'Hermentnan AI', chat: 'Chat ku AI' },
    nl: { title: 'AI Marketing Tools', chat: 'Chat met AI' }
  };

  const t = translations[language] || translations.en;

  return (
    <LinearGradient
      colors={['rgba(255,255,255,0.9)', 'rgba(255,255,255,0.7)']}
      style={styles.header}
    >
      <View style={styles.headerContent}>
        <View style={styles.logoContainer}>
          <LinearGradient
            colors={['#4ECDC4', '#FF6B6B']}
            style={styles.logo}
          >
            <Text style={styles.logoIcon}>💬</Text>
          </LinearGradient>
          <Text style={styles.logoText}>{t.title}</Text>
        </View>
        
        <View style={styles.headerActions}>
          <TouchableOpacity style={styles.languageButton}>
            <Text style={styles.languageFlag}>
              {languages.find(l => l.code === language)?.flag}
            </Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={openChatbot} style={styles.chatButton}>
            <LinearGradient
              colors={['#4ECDC4', '#FF6B6B']}
              style={styles.chatButtonGradient}
            >
              <Text style={styles.chatButtonText}>{t.chat}</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </View>
    </LinearGradient>
  );
};

const Hero = ({ language }) => {
  const translations = {
    en: {
      title: 'Boost Your Business with',
      titleHighlight: 'AI Marketing Tools',
      subtitle: 'Professional AI-powered marketing solutions for mobile',
      cta: 'Get Started'
    },
    es: {
      title: 'Impulsa Tu Negocio con',
      titleHighlight: 'Herramientas IA',
      subtitle: 'Soluciones profesionales de marketing con IA para móvil',
      cta: 'Comenzar'
    },
    pap: {
      title: 'Mehora Bo Negoshi ku',
      titleHighlight: 'Hermentnan AI',
      subtitle: 'Solushonnan profesional di marketing ku AI pa móvil',
      cta: 'Kuminsá'
    },
    nl: {
      title: 'Versterk Je Bedrijf met',
      titleHighlight: 'AI Marketing Tools',
      subtitle: 'Professionele AI-marketing oplossingen voor mobiel',
      cta: 'Begin'
    }
  };

  const t = translations[language] || translations.en;

  return (
    <View style={styles.hero}>
      <LinearGradient
        colors={['rgba(78, 205, 196, 0.1)', 'rgba(255, 107, 107, 0.1)']}
        style={styles.heroBackground}
      >
        <View style={styles.heroContent}>
          <Text style={styles.heroTitle}>{t.title}</Text>
          <LinearGradient
            colors={['#4ECDC4', '#FF6B6B']}
            style={styles.titleHighlight}
          >
            <Text style={styles.heroTitleHighlight}>{t.titleHighlight}</Text>
          </LinearGradient>
          <Text style={styles.heroSubtitle}>{t.subtitle}</Text>
          
          <TouchableOpacity style={styles.ctaButton}>
            <LinearGradient
              colors={['#4ECDC4', '#FF6B6B']}
              style={styles.ctaButtonGradient}
            >
              <Text style={styles.ctaButtonText}>{t.cta}</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </LinearGradient>
    </View>
  );
};

const ToolsSection = ({ language }) => {
  const translations = {
    en: {
      title: 'AI Tools',
      tools: [
        { name: 'AI Chatbot', desc: 'Smart customer support', icon: '🤖' },
        { name: 'Content Generator', desc: 'Create engaging content', icon: '✍️' },
        { name: 'Analytics', desc: 'Deep insights', icon: '📊' },
        { name: 'Email Marketing', desc: 'Automated campaigns', icon: '📧' }
      ]
    },
    es: {
      title: 'Herramientas IA',
      tools: [
        { name: 'Chatbot IA', desc: 'Soporte inteligente', icon: '🤖' },
        { name: 'Generador Contenido', desc: 'Crea contenido atractivo', icon: '✍️' },
        { name: 'Análisis', desc: 'Insights profundos', icon: '📊' },
        { name: 'Email Marketing', desc: 'Campañas automatizadas', icon: '📧' }
      ]
    },
    pap: {
      title: 'Hermentnan AI',
      tools: [
        { name: 'Chatbot AI', desc: 'Soporte inteligente', icon: '🤖' },
        { name: 'Generador Kontenido', desc: 'Krea kontenido atraktivo', icon: '✍️' },
        { name: 'Analítika', desc: 'Insight profundo', icon: '📊' },
        { name: 'Email Marketing', desc: 'Kampañanan automatisa', icon: '📧' }
      ]
    },
    nl: {
      title: 'AI Tools',
      tools: [
        { name: 'AI Chatbot', desc: 'Slimme klantenservice', icon: '🤖' },
        { name: 'Content Generator', desc: 'Maak boeiende content', icon: '✍️' },
        { name: 'Analytics', desc: 'Diepgaande inzichten', icon: '📊' },
        { name: 'Email Marketing', desc: 'Geautomatiseerde campagnes', icon: '📧' }
      ]
    }
  };

  const t = translations[language] || translations.en;

  return (
    <View style={styles.toolsSection}>
      <Text style={styles.sectionTitle}>{t.title}</Text>
      <View style={styles.toolsGrid}>
        {t.tools.map((tool, index) => (
          <TouchableOpacity key={index} style={styles.toolCard}>
            <View style={styles.toolIcon}>
              <Text style={styles.toolIconText}>{tool.icon}</Text>
            </View>
            <Text style={styles.toolName}>{tool.name}</Text>
            <Text style={styles.toolDesc}>{tool.desc}</Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );
};

const Chatbot = ({ isOpen, onToggle, language }) => {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');

  const translations = {
    en: { title: 'AI Assistant', placeholder: 'Type message...', welcome: 'Hello! How can I help?' },
    es: { title: 'Asistente IA', placeholder: 'Escribe mensaje...', welcome: '¡Hola! ¿Cómo puedo ayudar?' },
    pap: { title: 'Asistente AI', placeholder: 'Tipa mensahe...', welcome: 'Bon dia! Kon mi por yuda?' },
    nl: { title: 'AI Assistent', placeholder: 'Typ bericht...', welcome: 'Hallo! Hoe kan ik helpen?' }
  };

  const t = translations[language] || translations.en;

  if (!isOpen) {
    return (
      <TouchableOpacity onPress={onToggle} style={styles.chatbotBubble}>
        <LinearGradient
          colors={['#4ECDC4', '#FF6B6B']}
          style={styles.chatbotBubbleGradient}
        >
          <Text style={styles.chatbotBubbleText}>💬</Text>
        </LinearGradient>
      </TouchableOpacity>
    );
  }

  return (
    <View style={styles.chatbotWindow}>
      <LinearGradient
        colors={['#4ECDC4', '#FF6B6B']}
        style={styles.chatbotHeader}
      >
        <Text style={styles.chatbotTitle}>{t.title}</Text>
        <TouchableOpacity onPress={onToggle}>
          <Text style={styles.chatbotClose}>✕</Text>
        </TouchableOpacity>
      </LinearGradient>
      
      <View style={styles.chatbotMessages}>
        <View style={styles.welcomeMessage}>
          <Text style={styles.welcomeText}>{t.welcome}</Text>
        </View>
      </View>
      
      <View style={styles.chatbotInput}>
        <Text style={styles.inputPlaceholder}>{t.placeholder}</Text>
      </View>
    </View>
  );
};

export default function App() {
  const [language, setLanguage] = useState('en');
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  const toggleChatbot = () => {
    setIsChatbotOpen(!isChatbotOpen);
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="auto" />
      
      <Header 
        language={language} 
        setLanguage={setLanguage}
        openChatbot={toggleChatbot}
      />
      
      <ScrollView style={styles.content}>
        <Hero language={language} />
        <ToolsSection language={language} />
      </ScrollView>
      
      <Chatbot 
        isOpen={isChatbotOpen}
        onToggle={toggleChatbot}
        language={language}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8FFFE',
  },
  header: {
    paddingTop: 10,
    paddingBottom: 15,
    paddingHorizontal: 20,
  },
  headerContent: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  logoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  logo: {
    width: 40,
    height: 40,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  logoIcon: {
    fontSize: 20,
  },
  logoText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2C3E50',
  },
  headerActions: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  languageButton: {
    marginRight: 10,
    padding: 8,
  },
  languageFlag: {
    fontSize: 20,
  },
  chatButton: {
    borderRadius: 20,
  },
  chatButtonGradient: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
  },
  chatButtonText: {
    color: 'white',
    fontWeight: '600',
    fontSize: 14,
  },
  content: {
    flex: 1,
  },
  hero: {
    padding: 20,
    minHeight: 300,
  },
  heroBackground: {
    borderRadius: 20,
    padding: 30,
    alignItems: 'center',
  },
  heroContent: {
    alignItems: 'center',
  },
  heroTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2C3E50',
    textAlign: 'center',
    marginBottom: 10,
  },
  titleHighlight: {
    borderRadius: 10,
    paddingHorizontal: 15,
    paddingVertical: 5,
    marginBottom: 20,
  },
  heroTitleHighlight: {
    fontSize: 28,
    fontWeight: 'bold',
    color: 'white',
    textAlign: 'center',
  },
  heroSubtitle: {
    fontSize: 16,
    color: '#7F8C8D',
    textAlign: 'center',
    marginBottom: 30,
    lineHeight: 24,
  },
  ctaButton: {
    borderRadius: 25,
  },
  ctaButtonGradient: {
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 25,
  },
  ctaButtonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  toolsSection: {
    padding: 20,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2C3E50',
    textAlign: 'center',
    marginBottom: 20,
  },
  toolsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  toolCard: {
    width: '48%',
    backgroundColor: 'white',
    borderRadius: 15,
    padding: 20,
    marginBottom: 15,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  toolIcon: {
    marginBottom: 10,
  },
  toolIconText: {
    fontSize: 30,
  },
  toolName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2C3E50',
    textAlign: 'center',
    marginBottom: 5,
  },
  toolDesc: {
    fontSize: 12,
    color: '#7F8C8D',
    textAlign: 'center',
  },
  chatbotBubble: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  chatbotBubbleGradient: {
    width: 60,
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 8,
  },
  chatbotBubbleText: {
    fontSize: 24,
  },
  chatbotWindow: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    left: 20,
    height: 400,
    backgroundColor: 'white',
    borderRadius: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 8,
  },
  chatbotHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 15,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
  },
  chatbotTitle: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  chatbotClose: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  chatbotMessages: {
    flex: 1,
    padding: 15,
  },
  welcomeMessage: {
    backgroundColor: '#F8F9FA',
    padding: 12,
    borderRadius: 15,
    marginBottom: 10,
  },
  welcomeText: {
    color: '#2C3E50',
    fontSize: 14,
  },
  chatbotInput: {
    padding: 15,
    borderTopWidth: 1,
    borderTopColor: '#E9ECEF',
  },
  inputPlaceholder: {
    color: '#7F8C8D',
    fontSize: 14,
  },
});
