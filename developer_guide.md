# AI Marketing Tools - Developer Guide

![AI Marketing Tools Logo](../marketing-assets/brochures/ai_marketing_brochure_front.png)

This comprehensive developer guide provides detailed information for developers working with the AI Marketing Tools platform, including architecture, setup, customization, and best practices.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Development Environment Setup](#development-environment-setup)
3. [Project Structure](#project-structure)
4. [Frontend Development](#frontend-development)
5. [Mobile Development](#mobile-development)
6. [Backend Development](#backend-development)
7. [Database Schema](#database-schema)
8. [API Reference](#api-reference)
9. [Authentication & Authorization](#authentication--authorization)
10. [Testing](#testing)
11. [Deployment](#deployment)
12. [Performance Optimization](#performance-optimization)
13. [Security Guidelines](#security-guidelines)
14. [Contributing Guidelines](#contributing-guidelines)
15. [Troubleshooting](#troubleshooting)

## Architecture Overview

The AI Marketing Tools platform follows a modern microservices architecture:

### System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   Mobile App    │    │   Admin Panel   │
│   (React)       │    │   (React Native)│    │   (React)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ↓
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway (Nginx)                    │
└─────────────────────────────────────────────────────────────┘
                                 ↓
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Backend API   │    │   Auth Service  │    │   AI Service    │
│   (Flask)       │    │   (JWT)         │    │   (OpenAI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ↓
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Database      │    │   Redis Cache   │    │   File Storage  │
│   (PostgreSQL)  │    │   (Redis)       │    │   (Local/S3)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                 ↓
┌─────────────────────────────────────────────────────────────┐
│                  Monitoring & Analytics                     │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

- **Frontend**: React-based web application with responsive design
- **Mobile**: React Native mobile application for iOS and Android
- **Backend**: Flask-based RESTful API services
- **Database**: PostgreSQL for relational data storage
- **Cache**: Redis for performance optimization
- **AI Services**: Integration with OpenAI and custom ML models
- **Monitoring**: Custom analytics and monitoring system

### Communication Flow

1. Clients (web, mobile) communicate with backend via RESTful API
2. Authentication handled via JWT tokens
3. Backend services process requests and interact with database
4. AI services provide intelligent features and recommendations
5. Real-time features use WebSockets for bidirectional communication
6. Monitoring system tracks performance and user behavior

## Development Environment Setup

### Prerequisites

- **Node.js**: v20.x or higher
- **Python**: v3.11 or higher
- **Docker**: Latest stable version
- **Git**: Latest stable version
- **PostgreSQL**: v15.x
- **Redis**: v7.x

### Initial Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-organization/ai-marketing-tools.git
cd ai-marketing-tools
```

2. **Set up environment variables**

Create a `.env` file in the root directory:

```
# Development Environment Variables
NODE_ENV=development
FLASK_ENV=development
DEBUG=true

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_marketing_dev
DB_USER=postgres
DB_PASSWORD=your_password

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379

# API Configuration
API_KEY=dev_api_key_123
JWT_SECRET=dev_jwt_secret_456

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
```

3. **Set up backend environment**

```bash
cd ai-marketing-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade
flask run
```

4. **Set up frontend environment**

```bash
cd ai-marketing-web
npm install
npm run dev
```

5. **Set up mobile environment**

```bash
cd ai-marketing-mobile
npm install
npx expo start
```

### Docker Development Environment

For a containerized development environment:

```bash
# Start all services
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Stop all services
docker-compose -f docker-compose.dev.yml down
```

## Project Structure

### Root Directory Structure

```
AI_Marketing_Tools_Workspace/
├── ai-marketing-web/           # React web application
├── ai-marketing-mobile/        # React Native mobile app
├── ai-marketing-backend/       # Flask backend API
├── analytics-monitoring/       # Analytics and monitoring tools
├── marketing-assets/           # Marketing materials and assets
├── deployment/                 # Deployment and hosting configuration
├── docs/                       # Documentation
├── .github/                    # GitHub workflows and templates
├── .gitignore                  # Git ignore file
├── docker-compose.yml          # Production Docker Compose
├── docker-compose.dev.yml      # Development Docker Compose
└── README.md                   # Project README
```

### Web Application Structure

```
ai-marketing-web/
├── public/                     # Static assets
├── src/                        # Source code
│   ├── components/             # Reusable UI components
│   ├── pages/                  # Page components
│   ├── hooks/                  # Custom React hooks
│   ├── context/                # React context providers
│   ├── services/               # API and service integrations
│   ├── utils/                  # Utility functions
│   ├── styles/                 # Global styles
│   ├── assets/                 # Images and other assets
│   ├── App.jsx                 # Main application component
│   └── main.jsx                # Application entry point
├── .eslintrc.js                # ESLint configuration
├── package.json                # NPM package configuration
├── vite.config.js              # Vite configuration
└── README.md                   # Frontend README
```

### Mobile Application Structure

```
ai-marketing-mobile/
├── assets/                     # Static assets
├── src/                        # Source code
│   ├── components/             # Reusable UI components
│   ├── screens/                # Screen components
│   ├── navigation/             # Navigation configuration
│   ├── hooks/                  # Custom React hooks
│   ├── context/                # React context providers
│   ├── services/               # API and service integrations
│   ├── utils/                  # Utility functions
│   ├── styles/                 # Global styles
│   └── App.js                  # Main application component
├── .eslintrc.js                # ESLint configuration
├── app.json                    # Expo configuration
├── package.json                # NPM package configuration
└── README.md                   # Mobile README
```

### Backend Application Structure

```
ai-marketing-backend/
├── src/                        # Source code
│   ├── routes/                 # API route definitions
│   ├── models/                 # Database models
│   ├── services/               # Business logic services
│   ├── middleware/             # Request middleware
│   ├── utils/                  # Utility functions
│   ├── config/                 # Configuration files
│   ├── ai/                     # AI integration modules
│   └── main.py                 # Application entry point
├── migrations/                 # Database migrations
├── tests/                      # Test suite
├── requirements.txt            # Python dependencies
└── README.md                   # Backend README
```

## Frontend Development

### Technology Stack

- **Framework**: React 18+
- **Build Tool**: Vite
- **State Management**: React Context API + React Query
- **Styling**: TailwindCSS
- **UI Components**: Custom components with Headless UI
- **Form Handling**: React Hook Form
- **API Client**: Axios
- **Testing**: Jest + React Testing Library
- **Linting**: ESLint + Prettier

### Key Concepts

#### Component Structure

We follow a component-based architecture with:
- **Atomic Design**: Atoms, molecules, organisms, templates, pages
- **Container/Presentational Pattern**: Separate logic from presentation
- **Custom Hooks**: Extract reusable logic into hooks

#### State Management

- **Local State**: React's `useState` for component-specific state
- **Context API**: For shared state across components
- **React Query**: For server state management and caching

#### Styling Approach

- **TailwindCSS**: Utility-first CSS framework
- **CSS Modules**: For component-specific styles
- **Theme Configuration**: Customizable theme with CSS variables

### Best Practices

1. **Component Organization**
   - One component per file
   - Group related components in directories
   - Include index.js files for cleaner imports

2. **Performance Optimization**
   - Use React.memo for expensive renders
   - Implement virtualization for long lists
   - Optimize images and assets
   - Lazy load components and routes

3. **Accessibility**
   - Use semantic HTML elements
   - Include proper ARIA attributes
   - Ensure keyboard navigation
   - Maintain sufficient color contrast

4. **Code Style**
   - Follow ESLint and Prettier configurations
   - Use TypeScript for type safety
   - Write meaningful component and function names
   - Document complex logic with comments

### Example Component

```jsx
// src/components/ChatbotWidget/ChatbotWidget.jsx
import { useState, useEffect } from 'react';
import { useChatbot } from '../../hooks/useChatbot';
import { ChatMessage } from './ChatMessage';
import { ChatInput } from './ChatInput';
import './ChatbotWidget.css';

export const ChatbotWidget = ({ initialMessage, theme = 'light' }) => {
  const [messages, setMessages] = useState([]);
  const { sendMessage, isLoading } = useChatbot();

  useEffect(() => {
    if (initialMessage) {
      setMessages([
        { id: 'welcome', text: initialMessage, sender: 'bot', timestamp: new Date() }
      ]);
    }
  }, [initialMessage]);

  const handleSendMessage = async (text) => {
    // Add user message
    const userMessage = { 
      id: `user-${Date.now()}`, 
      text, 
      sender: 'user', 
      timestamp: new Date() 
    };
    setMessages(prev => [...prev, userMessage]);
    
    // Get bot response
    try {
      const response = await sendMessage(text);
      const botMessage = { 
        id: `bot-${Date.now()}`, 
        text: response.text, 
        sender: 'bot', 
        timestamp: new Date() 
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      // Add error message
      setMessages(prev => [...prev, { 
        id: `error-${Date.now()}`, 
        text: 'Sorry, there was an error processing your message.', 
        sender: 'bot', 
        timestamp: new Date(),
        isError: true
      }]);
    }
  };

  return (
    <div className={`chatbot-widget ${theme}`}>
      <div className="chatbot-messages">
        {messages.map(message => (
          <ChatMessage key={message.id} message={message} />
        ))}
        {isLoading && <div className="typing-indicator">Bot is typing...</div>}
      </div>
      <ChatInput onSendMessage={handleSendMessage} disabled={isLoading} />
    </div>
  );
};
```

## Mobile Development

### Technology Stack

- **Framework**: React Native
- **Development Platform**: Expo
- **Navigation**: React Navigation
- **State Management**: React Context + React Query
- **Styling**: StyleSheet API + React Native Paper
- **API Client**: Axios
- **Testing**: Jest + React Native Testing Library
- **Linting**: ESLint + Prettier

### Key Concepts

#### App Structure

- **Screens**: Full-page components
- **Navigation**: Stack, Tab, and Drawer navigators
- **Components**: Reusable UI elements
- **Hooks**: Custom logic for screens and components

#### Native Features

- **Camera Access**: For QR code scanning and image capture
- **Push Notifications**: For alerts and updates
- **Geolocation**: For location-based features
- **Offline Support**: Local storage and sync

#### Platform-Specific Code

- Use platform-specific file extensions (.ios.js, .android.js)
- Conditional rendering based on Platform API
- Platform-specific styling

### Best Practices

1. **Performance Optimization**
   - Minimize re-renders with React.memo and useMemo
   - Use FlatList for long lists
   - Optimize images and assets
   - Implement proper memory management

2. **UI/UX Guidelines**
   - Follow platform-specific design guidelines
   - Ensure touch targets are at least 44x44 points
   - Implement proper loading states
   - Support both portrait and landscape orientations

3. **Offline Support**
   - Implement data persistence with AsyncStorage
   - Queue actions when offline
   - Sync when connection is restored
   - Provide clear offline indicators

4. **Testing**
   - Write unit tests for components and hooks
   - Implement integration tests for screens
   - Test on multiple device sizes
   - Use Expo's device testing features

### Example Screen

```jsx
// src/screens/DashboardScreen.js
import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, RefreshControl, ScrollView } from 'react-native';
import { useQuery } from 'react-query';
import { Card, Title, Paragraph, Button } from 'react-native-paper';
import { fetchDashboardData } from '../services/api';
import { PerformanceChart } from '../components/PerformanceChart';
import { LoadingIndicator } from '../components/LoadingIndicator';
import { ErrorView } from '../components/ErrorView';
import { useTheme } from '../context/ThemeContext';

export const DashboardScreen = ({ navigation }) => {
  const { theme } = useTheme();
  const [refreshing, setRefreshing] = useState(false);
  
  const { data, isLoading, error, refetch } = useQuery(
    'dashboardData', 
    fetchDashboardData
  );
  
  const onRefresh = async () => {
    setRefreshing(true);
    await refetch();
    setRefreshing(false);
  };
  
  if (isLoading && !refreshing) {
    return <LoadingIndicator />;
  }
  
  if (error) {
    return <ErrorView error={error} onRetry={refetch} />;
  }
  
  return (
    <ScrollView
      style={[styles.container, { backgroundColor: theme.colors.background }]}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
      }
    >
      <Card style={styles.summaryCard}>
        <Card.Content>
          <Title>Performance Summary</Title>
          <PerformanceChart data={data?.performanceData} />
          <View style={styles.metricsContainer}>
            <View style={styles.metric}>
              <Paragraph style={styles.metricValue}>{data?.metrics.visitors}</Paragraph>
              <Paragraph>Visitors</Paragraph>
            </View>
            <View style={styles.metric}>
              <Paragraph style={styles.metricValue}>{data?.metrics.conversion}%</Paragraph>
              <Paragraph>Conversion</Paragraph>
            </View>
            <View style={styles.metric}>
              <Paragraph style={styles.metricValue}>${data?.metrics.revenue}</Paragraph>
              <Paragraph>Revenue</Paragraph>
            </View>
          </View>
        </Card.Content>
      </Card>
      
      <Card style={styles.actionsCard}>
        <Card.Content>
          <Title>Quick Actions</Title>
        </Card.Content>
        <Card.Actions>
          <Button onPress={() => navigation.navigate('CreateCampaign')}>
            New Campaign
          </Button>
          <Button onPress={() => navigation.navigate('ChatbotManager')}>
            Manage Chatbot
          </Button>
        </Card.Actions>
      </Card>
      
      {/* Additional dashboard cards */}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  summaryCard: {
    marginBottom: 16,
  },
  metricsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 16,
  },
  metric: {
    alignItems: 'center',
  },
  metricValue: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  actionsCard: {
    marginBottom: 16,
  },
});
```

## Backend Development

### Technology Stack

- **Framework**: Flask
- **ORM**: SQLAlchemy
- **API**: Flask-RESTful
- **Authentication**: JWT (Flask-JWT-Extended)
- **Database**: PostgreSQL
- **Caching**: Redis (Flask-Caching)
- **Task Queue**: Celery
- **Testing**: Pytest
- **Documentation**: Swagger/OpenAPI

### Key Concepts

#### API Design

- **RESTful Principles**: Resource-based URLs, appropriate HTTP methods
- **Versioning**: API versioning via URL path (/api/v1/)
- **Response Format**: Consistent JSON structure
- **Error Handling**: Standardized error responses
- **Pagination**: Offset/limit for list endpoints

#### Authentication & Authorization

- **JWT Tokens**: Access and refresh tokens
- **Role-Based Access Control**: User roles and permissions
- **API Keys**: For service-to-service communication
- **Rate Limiting**: Prevent abuse and ensure fair usage

#### Database Interaction

- **Models**: SQLAlchemy ORM models
- **Migrations**: Alembic for schema changes
- **Transactions**: Ensure data integrity
- **Query Optimization**: Efficient database queries

### Best Practices

1. **Code Organization**
   - Follow the blueprint pattern
   - Separate business logic from routes
   - Use services for complex operations
   - Implement repository pattern for data access

2. **Error Handling**
   - Use custom exception classes
   - Implement global error handlers
   - Log errors with context
   - Return appropriate HTTP status codes

3. **Performance Optimization**
   - Implement caching for frequent queries
   - Use database indexes
   - Optimize database queries
   - Implement background processing for heavy tasks

4. **Security**
   - Validate and sanitize all inputs
   - Implement proper authentication and authorization
   - Use HTTPS for all communications
   - Follow OWASP security guidelines

### Example Route

```python
# src/routes/chatbot.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from src.models import Chatbot, Conversation
from src.schemas import ChatbotSchema, MessageSchema
from src.services.chatbot_service import ChatbotService
from src.middleware.rate_limiter import limiter
from src.utils.logging import logger

chatbot_bp = Blueprint('chatbot', __name__)
chatbot_service = ChatbotService()

@chatbot_bp.route('/', methods=['GET'])
@jwt_required()
def get_chatbots():
    """Get all chatbots for the current user"""
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    chatbots, total = chatbot_service.get_user_chatbots(user_id, page, per_page)
    
    return jsonify({
        'data': ChatbotSchema(many=True).dump(chatbots),
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'pages': (total + per_page - 1) // per_page
        }
    }), 200

@chatbot_bp.route('/', methods=['POST'])
@jwt_required()
def create_chatbot():
    """Create a new chatbot"""
    user_id = get_jwt_identity()
    
    try:
        data = ChatbotSchema().load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Validation error', 'details': err.messages}), 400
    
    try:
        chatbot = chatbot_service.create_chatbot(user_id, data)
        return jsonify({'data': ChatbotSchema().dump(chatbot)}), 201
    except Exception as e:
        logger.error(f"Error creating chatbot: {str(e)}")
        return jsonify({'error': 'Failed to create chatbot'}), 500

@chatbot_bp.route('/<int:chatbot_id>', methods=['GET'])
@jwt_required()
def get_chatbot(chatbot_id):
    """Get a specific chatbot"""
    user_id = get_jwt_identity()
    
    chatbot = chatbot_service.get_chatbot(chatbot_id, user_id)
    if not chatbot:
        return jsonify({'error': 'Chatbot not found'}), 404
    
    return jsonify({'data': ChatbotSchema().dump(chatbot)}), 200

@chatbot_bp.route('/<int:chatbot_id>/message', methods=['POST'])
@limiter.limit("30/minute")
def send_message(chatbot_id):
    """Send a message to a chatbot"""
    try:
        data = MessageSchema().load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Validation error', 'details': err.messages}), 400
    
    try:
        response = chatbot_service.process_message(chatbot_id, data['message'])
        return jsonify({'data': response}), 200
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return jsonify({'error': 'Failed to process message'}), 500
```

## Database Schema

### Core Tables

#### Users

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    company_name VARCHAR(255),
    role VARCHAR(50) DEFAULT 'user',
    language VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    subscription_plan VARCHAR(50) DEFAULT 'free',
    subscription_status VARCHAR(50) DEFAULT 'active',
    subscription_expires TIMESTAMP
);
```

#### Chatbots

```sql
CREATE TABLE chatbots (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    personality VARCHAR(50) DEFAULT 'professional',
    language VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    configuration JSONB
);
```

#### Conversations

```sql
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    chatbot_id INTEGER REFERENCES chatbots(id) ON DELETE CASCADE,
    session_id VARCHAR(100) NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    user_info JSONB,
    metadata JSONB
);
```

#### Messages

```sql
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    conversation_id INTEGER REFERENCES conversations(id) ON DELETE CASCADE,
    sender VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);
```

#### Content

```sql
CREATE TABLE content (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP,
    metadata JSONB
);
```

#### Campaigns

```sql
CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    campaign_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) DEFAULT 'draft',
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    configuration JSONB,
    metrics JSONB
);
```

### Relationships

- **Users** have many **Chatbots**, **Content**, and **Campaigns**
- **Chatbots** have many **Conversations**
- **Conversations** have many **Messages**
- **Campaigns** can have many **Content** items (many-to-many)

### Indexes

```sql
-- Users table indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_subscription_plan ON users(subscription_plan);

-- Chatbots table indexes
CREATE INDEX idx_chatbots_user_id ON chatbots(user_id);
CREATE INDEX idx_chatbots_is_active ON chatbots(is_active);

-- Conversations table indexes
CREATE INDEX idx_conversations_chatbot_id ON conversations(chatbot_id);
CREATE INDEX idx_conversations_session_id ON conversations(session_id);

-- Messages table indexes
CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX idx_messages_timestamp ON messages(timestamp);

-- Content table indexes
CREATE INDEX idx_content_user_id ON content(user_id);
CREATE INDEX idx_content_content_type ON content(content_type);
CREATE INDEX idx_content_status ON content(status);

-- Campaigns table indexes
CREATE INDEX idx_campaigns_user_id ON campaigns(user_id);
CREATE INDEX idx_campaigns_campaign_type ON campaigns(campaign_type);
CREATE INDEX idx_campaigns_status ON campaigns(status);
```

## API Reference

For detailed API documentation, refer to the [API Reference](api_reference.md) document.

### API Endpoints Overview

#### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get tokens
- `POST /api/auth/refresh` - Refresh access token
- `POST /api/auth/logout` - Logout and invalidate tokens

#### Users

- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update user profile
- `GET /api/users/me/subscription` - Get subscription details
- `PUT /api/users/me/password` - Change password

#### Chatbots

- `GET /api/chatbots` - List user's chatbots
- `POST /api/chatbots` - Create a new chatbot
- `GET /api/chatbots/:id` - Get chatbot details
- `PUT /api/chatbots/:id` - Update chatbot
- `DELETE /api/chatbots/:id` - Delete chatbot
- `POST /api/chatbots/:id/message` - Send message to chatbot

#### Content

- `GET /api/content` - List user's content
- `POST /api/content` - Create new content
- `GET /api/content/:id` - Get content details
- `PUT /api/content/:id` - Update content
- `DELETE /api/content/:id` - Delete content
- `POST /api/content/generate` - Generate content with AI

#### Campaigns

- `GET /api/campaigns` - List user's campaigns
- `POST /api/campaigns` - Create new campaign
- `GET /api/campaigns/:id` - Get campaign details
- `PUT /api/campaigns/:id` - Update campaign
- `DELETE /api/campaigns/:id` - Delete campaign
- `GET /api/campaigns/:id/metrics` - Get campaign metrics

#### Analytics

- `GET /api/analytics/dashboard` - Get dashboard analytics
- `GET /api/analytics/users` - Get user analytics
- `GET /api/analytics/content` - Get content performance
- `GET /api/analytics/campaigns` - Get campaign performance
- `GET /api/analytics/chatbots` - Get chatbot performance

## Authentication & Authorization

### Authentication Flow

1. **Registration**: User registers with email and password
2. **Login**: User logs in and receives access and refresh tokens
3. **API Access**: Access token is included in Authorization header
4. **Token Refresh**: Refresh token is used to get new access token
5. **Logout**: Tokens are invalidated

### JWT Implementation

```python
# src/auth/jwt.py
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
from datetime import timedelta
from src.models import User, TokenBlocklist
from src.config import Config

jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = TokenBlocklist.query.filter_by(jti=jti).first()
    return token is not None

def generate_tokens(user):
    """Generate access and refresh tokens for a user"""
    access_token = create_access_token(
        identity=user.id,
        additional_claims={
            "role": user.role,
            "plan": user.subscription_plan
        },
        expires_delta=timedelta(minutes=Config.JWT_ACCESS_TOKEN_EXPIRES)
    )
    
    refresh_token = create_refresh_token(
        identity=user.id,
        expires_delta=timedelta(days=Config.JWT_REFRESH_TOKEN_EXPIRES)
    )
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": Config.JWT_ACCESS_TOKEN_EXPIRES * 60
    }
```

### Role-Based Authorization

```python
# src/middleware/authorization.py
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

def role_required(role):
    """Decorator to require a specific role for access"""
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            
            if claims.get("role") == role or claims.get("role") == "admin":
                return fn(*args, **kwargs)
            else:
                return jsonify({"error": "Insufficient permissions"}), 403
        return decorator
    return wrapper

def subscription_required(plan_level):
    """Decorator to require a specific subscription plan"""
    plan_levels = {
        "free": 0,
        "starter": 1,
        "professional": 2,
        "enterprise": 3
    }
    
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            
            user_plan = claims.get("plan", "free")
            user_level = plan_levels.get(user_plan, 0)
            required_level = plan_levels.get(plan_level, 0)
            
            if user_level >= required_level:
                return fn(*args, **kwargs)
            else:
                return jsonify({
                    "error": "Subscription required",
                    "required_plan": plan_level
                }), 402
        return decorator
    return wrapper
```

## Testing

### Testing Strategy

- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test API endpoints and service interactions
- **End-to-End Tests**: Test complete user flows
- **Performance Tests**: Test system under load

### Test Directory Structure

```
tests/
├── unit/                       # Unit tests
│   ├── test_models.py          # Test database models
│   ├── test_services.py        # Test service functions
│   └── test_utils.py           # Test utility functions
├── integration/                # Integration tests
│   ├── test_auth_api.py        # Test authentication endpoints
│   ├── test_chatbot_api.py     # Test chatbot endpoints
│   └── test_content_api.py     # Test content endpoints
├── e2e/                        # End-to-end tests
│   ├── test_user_flows.py      # Test complete user journeys
│   └── test_admin_flows.py     # Test admin workflows
├── performance/                # Performance tests
│   ├── test_api_load.py        # API load testing
│   └── test_database.py        # Database performance
├── conftest.py                 # Test fixtures and configuration
└── .coveragerc                 # Coverage configuration
```

### Example Test

```python
# tests/integration/test_chatbot_api.py
import pytest
import json
from src.models import Chatbot

def test_create_chatbot(client, auth_headers):
    """Test creating a new chatbot"""
    # Arrange
    data = {
        "name": "Test Chatbot",
        "description": "A test chatbot",
        "personality": "friendly",
        "language": "en",
        "configuration": {
            "welcome_message": "Hello! How can I help you today?"
        }
    }
    
    # Act
    response = client.post(
        '/api/chatbots',
        data=json.dumps(data),
        headers=auth_headers,
        content_type='application/json'
    )
    
    # Assert
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert 'data' in response_data
    assert response_data['data']['name'] == "Test Chatbot"
    assert response_data['data']['personality'] == "friendly"
    
    # Verify database
    chatbot = Chatbot.query.filter_by(name="Test Chatbot").first()
    assert chatbot is not None
    assert chatbot.description == "A test chatbot"

def test_get_chatbots(client, auth_headers, create_test_chatbots):
    """Test retrieving user's chatbots"""
    # Arrange
    chatbots = create_test_chatbots(3)  # Create 3 test chatbots
    
    # Act
    response = client.get(
        '/api/chatbots',
        headers=auth_headers
    )
    
    # Assert
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert 'data' in response_data
    assert len(response_data['data']) == 3
    assert 'meta' in response_data
    assert response_data['meta']['total'] == 3

def test_send_message_to_chatbot(client, auth_headers, create_test_chatbots):
    """Test sending a message to a chatbot"""
    # Arrange
    chatbots = create_test_chatbots(1)
    chatbot_id = chatbots[0].id
    data = {
        "message": "Hello, how are you?"
    }
    
    # Act
    response = client.post(
        f'/api/chatbots/{chatbot_id}/message',
        data=json.dumps(data),
        headers=auth_headers,
        content_type='application/json'
    )
    
    # Assert
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert 'data' in response_data
    assert 'message' in response_data['data']
    assert 'timestamp' in response_data['data']
```

## Deployment

For detailed deployment instructions, refer to the [Deployment Guide](../deployment/README.md).

### Deployment Environments

- **Development**: Local development environment
- **Staging**: Pre-production testing environment
- **Production**: Live production environment

### Deployment Process

1. **Build**: Compile and package application
2. **Test**: Run automated tests
3. **Deploy**: Push to target environment
4. **Verify**: Confirm deployment success
5. **Monitor**: Track performance and errors

### CI/CD Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r ai-marketing-backend/requirements.txt
      - name: Run tests
        run: |
          cd ai-marketing-backend
          pytest

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker images
        run: |
          docker build -f deployment/docker/Dockerfile.backend -t ai-marketing-backend:latest ai-marketing-backend/
          docker build -f deployment/docker/Dockerfile.frontend -t ai-marketing-frontend:latest ai-marketing-web/
      - name: Push to registry
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker tag ai-marketing-backend:latest yourusername/ai-marketing-backend:latest
          docker tag ai-marketing-frontend:latest yourusername/ai-marketing-frontend:latest
          docker push yourusername/ai-marketing-backend:latest
          docker push yourusername/ai-marketing-frontend:latest

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USERNAME }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: |
            cd /opt/ai-marketing-tools
            docker-compose pull
            docker-compose up -d
```

## Performance Optimization

### Frontend Optimization

- **Code Splitting**: Load components on demand
- **Tree Shaking**: Eliminate unused code
- **Lazy Loading**: Defer loading of non-critical resources
- **Image Optimization**: Compress and use appropriate formats
- **Caching**: Implement effective caching strategies

### Backend Optimization

- **Database Indexing**: Create appropriate indexes
- **Query Optimization**: Optimize database queries
- **Caching**: Cache frequent queries and responses
- **Connection Pooling**: Reuse database connections
- **Asynchronous Processing**: Use background tasks for heavy operations

### API Optimization

- **Pagination**: Limit result sets
- **Field Selection**: Allow clients to request only needed fields
- **Compression**: Enable GZIP/Brotli compression
- **Rate Limiting**: Prevent abuse
- **Batch Operations**: Support batch requests

### Database Optimization

- **Indexing Strategy**: Create appropriate indexes
- **Query Optimization**: Use EXPLAIN to analyze queries
- **Connection Pooling**: Reuse database connections
- **Partitioning**: Split large tables
- **Regular Maintenance**: Update statistics and vacuum

## Security Guidelines

### Authentication & Authorization

- **Strong Password Policy**: Enforce password complexity
- **MFA**: Implement multi-factor authentication
- **JWT Best Practices**: Short-lived tokens, secure storage
- **Role-Based Access Control**: Limit access based on roles
- **API Keys**: Secure generation and storage

### Data Protection

- **Encryption**: Encrypt sensitive data at rest and in transit
- **Input Validation**: Validate and sanitize all inputs
- **Output Encoding**: Prevent XSS attacks
- **CSRF Protection**: Implement anti-CSRF tokens
- **Content Security Policy**: Restrict resource loading

### API Security

- **Rate Limiting**: Prevent abuse and DoS attacks
- **HTTPS**: Enforce secure connections
- **CORS**: Configure appropriate CORS policies
- **Security Headers**: Implement security headers
- **API Versioning**: Maintain backward compatibility

### Secure Coding Practices

- **Dependency Management**: Keep dependencies updated
- **Code Reviews**: Conduct security-focused code reviews
- **Static Analysis**: Use security linting tools
- **Vulnerability Scanning**: Regular security scans
- **Security Testing**: Include security tests in CI/CD

## Contributing Guidelines

### Code Contribution Process

1. **Fork the Repository**: Create your own fork
2. **Create a Branch**: Make changes in a new branch
3. **Follow Style Guidelines**: Adhere to project coding standards
4. **Write Tests**: Include tests for new features
5. **Submit Pull Request**: Create a PR with a clear description

### Coding Standards

- **JavaScript/TypeScript**: Follow Airbnb style guide
- **Python**: Follow PEP 8 style guide
- **Documentation**: Document all public APIs
- **Commit Messages**: Use conventional commits format
- **Testing**: Maintain high test coverage

### Pull Request Guidelines

- **Descriptive Title**: Clear and concise PR title
- **Detailed Description**: Explain changes and rationale
- **Reference Issues**: Link related issues
- **Keep Changes Focused**: One feature/fix per PR
- **CI Checks**: Ensure all checks pass

### Development Workflow

1. **Issue Discussion**: Discuss approach in GitHub issues
2. **Implementation**: Develop the feature or fix
3. **Testing**: Write and run tests
4. **Documentation**: Update relevant documentation
5. **Code Review**: Address review feedback
6. **Merge**: PR is merged after approval

## Troubleshooting

### Common Issues

#### Frontend Issues

- **Build Failures**: Check for syntax errors and dependencies
- **Rendering Issues**: Inspect component hierarchy and props
- **State Management**: Debug state updates and side effects
- **Performance Problems**: Profile rendering and identify bottlenecks
- **API Integration**: Verify request/response handling

#### Backend Issues

- **Server Errors**: Check logs for exceptions
- **Database Connectivity**: Verify connection parameters
- **Authentication Issues**: Debug token generation and validation
- **Performance Bottlenecks**: Profile API endpoints
- **Memory Leaks**: Monitor resource usage

#### Mobile Issues

- **Build Failures**: Check native dependencies
- **Rendering Issues**: Test on multiple devices
- **Performance Problems**: Use React Native performance tools
- **Native Integration**: Debug native module integration
- **Offline Support**: Test offline behavior

### Debugging Tools

- **Frontend**: React DevTools, Redux DevTools, Chrome DevTools
- **Backend**: pdb, Flask Debug Toolbar, logging
- **Mobile**: React Native Debugger, Flipper
- **API**: Postman, Insomnia, curl
- **Database**: pgAdmin, Redis CLI

### Logging

- **Frontend**: Console logging, error tracking services
- **Backend**: Structured logging with context
- **Mobile**: Device-specific logging
- **API**: Request/response logging
- **Database**: Query logging

### Support Resources

- **Documentation**: Refer to project documentation
- **Issue Tracker**: Search existing issues
- **Community Forums**: Discuss with community
- **Stack Overflow**: Search for similar problems
- **Support Email**: Contact support@ai-marketing-tools.com

---

## Need More Help?

If you can't find the information you need in this guide:

- **GitHub Issues**: Submit issues at [github.com/your-organization/ai-marketing-tools/issues](https://github.com/your-organization/ai-marketing-tools/issues)
- **Developer Forum**: Join discussions at [community.ai-marketing-tools.com/developers](https://community.ai-marketing-tools.com/developers)
- **API Documentation**: Browse API docs at [api.ai-marketing-tools.com/docs](https://api.ai-marketing-tools.com/docs)
- **Support**: Contact developer support at [dev-support@ai-marketing-tools.com](mailto:dev-support@ai-marketing-tools.com)

---

© 2025 AI Marketing Tools. All rights reserved.

