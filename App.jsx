import { useState } from 'react';
import Header from './components/Header.jsx';
import Hero from './components/Hero.jsx';
import AIToolsShowcase from './components/AIToolsShowcase.jsx';
import PricingSection from './components/PricingSection.jsx';
import Footer from './components/Footer.jsx';
import Chatbot from './components/Chatbot.jsx';
import './App.css';

function App() {
  const [language, setLanguage] = useState('en');
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  const toggleChatbot = () => {
    setIsChatbotOpen(!isChatbotOpen);
  };

  return (
    <div className="min-h-screen bg-background">
      <Header 
        language={language} 
        setLanguage={setLanguage}
        openChatbot={toggleChatbot}
      />
      
      <main>
        <Hero language={language} />
        <AIToolsShowcase language={language} />
        <PricingSection language={language} />
      </main>
      
      <Footer language={language} />
      
      <Chatbot 
        isOpen={isChatbotOpen}
        onToggle={toggleChatbot}
        language={language}
      />
    </div>
  );
}

export default App;
