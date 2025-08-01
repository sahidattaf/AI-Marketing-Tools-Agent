# AI Marketing Tools - API Reference

![AI Marketing Tools Logo](../marketing-assets/brochures/ai_marketing_brochure_front.png)

This comprehensive API reference provides detailed information about all available endpoints, request/response formats, authentication, and examples for the AI Marketing Tools platform.

## Table of Contents

1. [API Overview](#api-overview)
2. [Authentication](#authentication)
3. [Response Format](#response-format)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [Versioning](#versioning)
7. [Endpoints](#endpoints)
   - [Authentication](#authentication-endpoints)
   - [Users](#user-endpoints)
   - [Chatbots](#chatbot-endpoints)
   - [Content](#content-endpoints)
   - [Campaigns](#campaign-endpoints)
   - [Analytics](#analytics-endpoints)
8. [Webhooks](#webhooks)
9. [SDKs & Libraries](#sdks--libraries)
10. [Best Practices](#best-practices)

## API Overview

The AI Marketing Tools API is a RESTful API that allows you to interact with all aspects of the platform programmatically. The API uses standard HTTP methods and returns JSON responses.

### Base URL

```
https://api.ai-marketing-tools.com/v1
```

### API Keys

All API requests require authentication using either:
- JWT tokens (for user-based authentication)
- API keys (for service-to-service communication)

### Content Types

- Request Content-Type: `application/json`
- Response Content-Type: `application/json`

## Authentication

### JWT Authentication

For user-based authentication, the API uses JSON Web Tokens (JWT).

1. Obtain an access token by authenticating with email and password:

```
POST /auth/login
```

2. Include the access token in the Authorization header for subsequent requests:

```
Authorization: Bearer {access_token}
```

3. Refresh the access token when it expires:

```
POST /auth/refresh
```

### API Key Authentication

For service-to-service communication, use API keys.

1. Generate an API key in the dashboard
2. Include the API key in the header:

```
X-API-Key: {your_api_key}
```

## Response Format

All API responses follow a consistent format:

### Success Response

```json
{
  "data": {
    // Response data
  },
  "meta": {
    // Metadata (pagination, etc.)
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable error message",
    "details": {
      // Additional error details
    }
  }
}
```

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests.

### Common Status Codes

- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation error
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

### Error Codes

| Code | Description |
|------|-------------|
| `invalid_request` | The request is malformed or missing required parameters |
| `authentication_required` | Authentication is required for this endpoint |
| `invalid_credentials` | The provided credentials are invalid |
| `access_denied` | The authenticated user does not have sufficient permissions |
| `resource_not_found` | The requested resource does not exist |
| `validation_error` | The request contains invalid data |
| `rate_limit_exceeded` | The rate limit for this endpoint has been exceeded |
| `server_error` | An unexpected error occurred on the server |

## Rate Limiting

The API implements rate limiting to prevent abuse and ensure fair usage.

### Rate Limit Headers

Rate limit information is included in the response headers:

```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1625097600
```

### Rate Limit Tiers

| Plan | Rate Limit |
|------|------------|
| Free | 60 requests per minute |
| Starter | 120 requests per minute |
| Professional | 300 requests per minute |
| Enterprise | Custom |

### Exceeding Rate Limits

When rate limits are exceeded, the API returns a `429 Too Many Requests` response with a `Retry-After` header indicating when to retry.

## Versioning

The API uses URL versioning to ensure backward compatibility.

### Current Version

The current API version is `v1`.

### Version Format

```
https://api.ai-marketing-tools.com/{version}/{endpoint}
```

### Version Lifecycle

- New versions are announced at least 6 months before release
- Old versions are supported for at least 12 months after a new version is released
- Deprecation notices are provided in response headers

## Endpoints

### Authentication Endpoints

#### Register a new user

```
POST /auth/register
```

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "first_name": "John",
  "last_name": "Doe",
  "company_name": "Example Inc."
}
```

**Response:**

```json
{
  "data": {
    "user": {
      "id": 123,
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "company_name": "Example Inc.",
      "created_at": "2025-01-15T12:00:00Z"
    },
    "tokens": {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "expires_in": 3600
    }
  }
}
```

#### Login

```
POST /auth/login
```

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response:**

```json
{
  "data": {
    "user": {
      "id": 123,
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "company_name": "Example Inc."
    },
    "tokens": {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "expires_in": 3600
    }
  }
}
```

#### Refresh Token

```
POST /auth/refresh
```

**Request Body:**

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:**

```json
{
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expires_in": 3600
  }
}
```

#### Logout

```
POST /auth/logout
```

**Request Body:**

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:**

```json
{
  "data": {
    "message": "Successfully logged out"
  }
}
```

### User Endpoints

#### Get Current User

```
GET /users/me
```

**Response:**

```json
{
  "data": {
    "id": 123,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Example Inc.",
    "role": "user",
    "language": "en",
    "created_at": "2025-01-15T12:00:00Z",
    "subscription": {
      "plan": "professional",
      "status": "active",
      "expires_at": "2026-01-15T12:00:00Z"
    }
  }
}
```

#### Update User Profile

```
PUT /users/me
```

**Request Body:**

```json
{
  "first_name": "John",
  "last_name": "Smith",
  "company_name": "New Company Inc.",
  "language": "es"
}
```

**Response:**

```json
{
  "data": {
    "id": 123,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Smith",
    "company_name": "New Company Inc.",
    "language": "es",
    "updated_at": "2025-01-20T14:30:00Z"
  }
}
```

#### Change Password

```
PUT /users/me/password
```

**Request Body:**

```json
{
  "current_password": "securePassword123",
  "new_password": "evenMoreSecure456"
}
```

**Response:**

```json
{
  "data": {
    "message": "Password updated successfully"
  }
}
```

#### Get Subscription Details

```
GET /users/me/subscription
```

**Response:**

```json
{
  "data": {
    "plan": "professional",
    "status": "active",
    "started_at": "2025-01-15T12:00:00Z",
    "expires_at": "2026-01-15T12:00:00Z",
    "auto_renew": true,
    "payment_method": "credit_card",
    "features": {
      "chatbots": {
        "limit": 10,
        "used": 3
      },
      "content_generation": {
        "limit": -1,
        "used": 47
      },
      "campaigns": {
        "limit": 20,
        "used": 5
      }
    }
  }
}
```

### Chatbot Endpoints

#### List Chatbots

```
GET /chatbots
```

**Query Parameters:**

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10)
- `status`: Filter by status (active, inactive, all)

**Response:**

```json
{
  "data": [
    {
      "id": 1,
      "name": "Sales Assistant",
      "description": "AI assistant for sales inquiries",
      "personality": "professional",
      "language": "en",
      "created_at": "2025-01-15T12:00:00Z",
      "is_active": true,
      "stats": {
        "conversations": 156,
        "messages": 1243,
        "avg_satisfaction": 4.7
      }
    },
    {
      "id": 2,
      "name": "Support Bot",
      "description": "Customer support chatbot",
      "personality": "helpful",
      "language": "en",
      "created_at": "2025-01-20T15:30:00Z",
      "is_active": true,
      "stats": {
        "conversations": 89,
        "messages": 567,
        "avg_satisfaction": 4.2
      }
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 2,
    "pages": 1
  }
}
```

#### Create Chatbot

```
POST /chatbots
```

**Request Body:**

```json
{
  "name": "Marketing Assistant",
  "description": "AI assistant for marketing inquiries",
  "personality": "friendly",
  "language": "en",
  "configuration": {
    "welcome_message": "Hello! I'm your marketing assistant. How can I help you today?",
    "fallback_message": "I'm sorry, I didn't understand that. Could you rephrase your question?",
    "working_hours": {
      "enabled": true,
      "timezone": "America/New_York",
      "hours": [
        {"day": "monday", "start": "09:00", "end": "17:00"},
        {"day": "tuesday", "start": "09:00", "end": "17:00"},
        {"day": "wednesday", "start": "09:00", "end": "17:00"},
        {"day": "thursday", "start": "09:00", "end": "17:00"},
        {"day": "friday", "start": "09:00", "end": "17:00"}
      ],
      "outside_hours_message": "I'm currently offline. I'll be back during business hours."
    }
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 3,
    "name": "Marketing Assistant",
    "description": "AI assistant for marketing inquiries",
    "personality": "friendly",
    "language": "en",
    "created_at": "2025-01-25T10:15:00Z",
    "is_active": true,
    "configuration": {
      "welcome_message": "Hello! I'm your marketing assistant. How can I help you today?",
      "fallback_message": "I'm sorry, I didn't understand that. Could you rephrase your question?",
      "working_hours": {
        "enabled": true,
        "timezone": "America/New_York",
        "hours": [
          {"day": "monday", "start": "09:00", "end": "17:00"},
          {"day": "tuesday", "start": "09:00", "end": "17:00"},
          {"day": "wednesday", "start": "09:00", "end": "17:00"},
          {"day": "thursday", "start": "09:00", "end": "17:00"},
          {"day": "friday", "start": "09:00", "end": "17:00"}
        ],
        "outside_hours_message": "I'm currently offline. I'll be back during business hours."
      }
    }
  }
}
```

#### Get Chatbot

```
GET /chatbots/{id}
```

**Response:**

```json
{
  "data": {
    "id": 3,
    "name": "Marketing Assistant",
    "description": "AI assistant for marketing inquiries",
    "personality": "friendly",
    "language": "en",
    "created_at": "2025-01-25T10:15:00Z",
    "updated_at": "2025-01-25T10:15:00Z",
    "is_active": true,
    "configuration": {
      "welcome_message": "Hello! I'm your marketing assistant. How can I help you today?",
      "fallback_message": "I'm sorry, I didn't understand that. Could you rephrase your question?",
      "working_hours": {
        "enabled": true,
        "timezone": "America/New_York",
        "hours": [
          {"day": "monday", "start": "09:00", "end": "17:00"},
          {"day": "tuesday", "start": "09:00", "end": "17:00"},
          {"day": "wednesday", "start": "09:00", "end": "17:00"},
          {"day": "thursday", "start": "09:00", "end": "17:00"},
          {"day": "friday", "start": "09:00", "end": "17:00"}
        ],
        "outside_hours_message": "I'm currently offline. I'll be back during business hours."
      }
    },
    "stats": {
      "conversations": 0,
      "messages": 0,
      "avg_satisfaction": null
    },
    "integration": {
      "widget_code": "<script src=\"https://cdn.ai-marketing-tools.com/chatbot.js\" data-chatbot-id=\"3\"></script>",
      "api_endpoint": "https://api.ai-marketing-tools.com/v1/chatbots/3/message"
    }
  }
}
```

#### Update Chatbot

```
PUT /chatbots/{id}
```

**Request Body:**

```json
{
  "name": "Marketing Pro Assistant",
  "description": "Advanced AI assistant for marketing inquiries",
  "is_active": true,
  "configuration": {
    "welcome_message": "Hello! I'm your marketing pro assistant. How can I help you today?"
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 3,
    "name": "Marketing Pro Assistant",
    "description": "Advanced AI assistant for marketing inquiries",
    "personality": "friendly",
    "language": "en",
    "created_at": "2025-01-25T10:15:00Z",
    "updated_at": "2025-01-26T11:30:00Z",
    "is_active": true,
    "configuration": {
      "welcome_message": "Hello! I'm your marketing pro assistant. How can I help you today?",
      "fallback_message": "I'm sorry, I didn't understand that. Could you rephrase your question?",
      "working_hours": {
        "enabled": true,
        "timezone": "America/New_York",
        "hours": [
          {"day": "monday", "start": "09:00", "end": "17:00"},
          {"day": "tuesday", "start": "09:00", "end": "17:00"},
          {"day": "wednesday", "start": "09:00", "end": "17:00"},
          {"day": "thursday", "start": "09:00", "end": "17:00"},
          {"day": "friday", "start": "09:00", "end": "17:00"}
        ],
        "outside_hours_message": "I'm currently offline. I'll be back during business hours."
      }
    }
  }
}
```

#### Delete Chatbot

```
DELETE /chatbots/{id}
```

**Response:**

```json
{
  "data": {
    "message": "Chatbot deleted successfully"
  }
}
```

#### Send Message to Chatbot

```
POST /chatbots/{id}/message
```

**Request Body:**

```json
{
  "message": "What marketing strategies do you recommend for a small business?",
  "session_id": "user_session_123",
  "user_info": {
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
}
```

**Response:**

```json
{
  "data": {
    "message": "For small businesses, I recommend focusing on these key strategies:\n\n1. Content marketing: Create valuable blog posts, videos, or podcasts that address your audience's needs.\n\n2. Social media marketing: Build a presence on platforms where your customers spend time.\n\n3. Email marketing: Develop a newsletter to nurture leads and maintain customer relationships.\n\n4. Local SEO: Optimize your online presence for local searches if you have a physical location.\n\n5. Partnerships: Collaborate with complementary businesses to expand your reach.\n\nWhich of these areas would you like to explore further?",
    "session_id": "user_session_123",
    "timestamp": "2025-01-26T14:22:15Z",
    "suggestions": [
      "Tell me more about content marketing",
      "How can I improve my social media presence?",
      "What makes a good email newsletter?"
    ]
  }
}
```

#### Get Chatbot Conversations

```
GET /chatbots/{id}/conversations
```

**Query Parameters:**

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10)
- `start_date`: Filter by start date (ISO format)
- `end_date`: Filter by end date (ISO format)

**Response:**

```json
{
  "data": [
    {
      "id": 101,
      "session_id": "user_session_123",
      "started_at": "2025-01-26T14:20:00Z",
      "ended_at": "2025-01-26T14:35:00Z",
      "message_count": 8,
      "user_info": {
        "name": "Jane Smith",
        "email": "jane@example.com"
      },
      "satisfaction": 5,
      "summary": "Discussion about marketing strategies for small businesses, focusing on content marketing and social media."
    },
    {
      "id": 102,
      "session_id": "user_session_456",
      "started_at": "2025-01-26T15:10:00Z",
      "ended_at": "2025-01-26T15:18:00Z",
      "message_count": 5,
      "user_info": {
        "name": "Bob Johnson",
        "email": "bob@example.com"
      },
      "satisfaction": 4,
      "summary": "Inquiry about email marketing best practices and newsletter templates."
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 2,
    "pages": 1
  }
}
```

#### Get Conversation Messages

```
GET /chatbots/{id}/conversations/{conversation_id}/messages
```

**Response:**

```json
{
  "data": [
    {
      "id": 501,
      "sender": "user",
      "content": "What marketing strategies do you recommend for a small business?",
      "timestamp": "2025-01-26T14:20:15Z"
    },
    {
      "id": 502,
      "sender": "bot",
      "content": "For small businesses, I recommend focusing on these key strategies:\n\n1. Content marketing: Create valuable blog posts, videos, or podcasts that address your audience's needs.\n\n2. Social media marketing: Build a presence on platforms where your customers spend time.\n\n3. Email marketing: Develop a newsletter to nurture leads and maintain customer relationships.\n\n4. Local SEO: Optimize your online presence for local searches if you have a physical location.\n\n5. Partnerships: Collaborate with complementary businesses to expand your reach.\n\nWhich of these areas would you like to explore further?",
      "timestamp": "2025-01-26T14:20:30Z",
      "suggestions": [
        "Tell me more about content marketing",
        "How can I improve my social media presence?",
        "What makes a good email newsletter?"
      ]
    },
    {
      "id": 503,
      "sender": "user",
      "content": "Tell me more about content marketing",
      "timestamp": "2025-01-26T14:21:15Z"
    },
    {
      "id": 504,
      "sender": "bot",
      "content": "Content marketing is all about creating valuable, relevant content that attracts and engages your target audience. Here's how to get started:\n\n1. Identify your audience's pain points and questions\n2. Create content that addresses these needs (blog posts, videos, infographics, etc.)\n3. Optimize content for search engines (SEO)\n4. Distribute content across appropriate channels\n5. Analyze performance and refine your strategy\n\nConsistent, high-quality content helps establish your expertise, build trust, and drive conversions without hard selling. What specific type of content would work best for your business?",
      "timestamp": "2025-01-26T14:21:45Z"
    }
  ],
  "meta": {
    "conversation_id": 101,
    "session_id": "user_session_123",
    "started_at": "2025-01-26T14:20:00Z",
    "ended_at": "2025-01-26T14:35:00Z",
    "total_messages": 8
  }
}
```

### Content Endpoints

#### List Content

```
GET /content
```

**Query Parameters:**

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10)
- `content_type`: Filter by content type (blog, social, email, ad)
- `status`: Filter by status (draft, published, archived)

**Response:**

```json
{
  "data": [
    {
      "id": 201,
      "title": "10 Effective Marketing Strategies for 2025",
      "content_type": "blog",
      "status": "published",
      "created_at": "2025-01-15T10:00:00Z",
      "updated_at": "2025-01-15T14:30:00Z",
      "published_at": "2025-01-16T09:00:00Z",
      "excerpt": "Discover the top marketing strategies that will drive growth for your business in 2025.",
      "word_count": 1250,
      "read_time": 6
    },
    {
      "id": 202,
      "title": "Introducing Our New Product Line",
      "content_type": "email",
      "status": "draft",
      "created_at": "2025-01-20T11:15:00Z",
      "updated_at": "2025-01-20T11:15:00Z",
      "published_at": null,
      "excerpt": "Email announcement for our upcoming product launch.",
      "word_count": 350,
      "read_time": 2
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 2,
    "pages": 1
  }
}
```

#### Create Content

```
POST /content
```

**Request Body:**

```json
{
  "title": "How AI is Transforming Digital Marketing",
  "content_type": "blog",
  "content": "# How AI is Transforming Digital Marketing\n\nArtificial intelligence is revolutionizing the way businesses approach digital marketing...",
  "status": "draft",
  "metadata": {
    "categories": ["AI", "Digital Marketing", "Technology"],
    "tags": ["artificial intelligence", "marketing automation", "personalization"],
    "featured_image": "https://example.com/images/ai-marketing.jpg",
    "seo": {
      "meta_title": "How AI is Revolutionizing Digital Marketing in 2025",
      "meta_description": "Discover how artificial intelligence is transforming digital marketing strategies and driving better results for businesses.",
      "focus_keyword": "AI in digital marketing"
    }
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 203,
    "title": "How AI is Transforming Digital Marketing",
    "content_type": "blog",
    "content": "# How AI is Transforming Digital Marketing\n\nArtificial intelligence is revolutionizing the way businesses approach digital marketing...",
    "status": "draft",
    "created_at": "2025-01-26T15:30:00Z",
    "updated_at": "2025-01-26T15:30:00Z",
    "published_at": null,
    "metadata": {
      "categories": ["AI", "Digital Marketing", "Technology"],
      "tags": ["artificial intelligence", "marketing automation", "personalization"],
      "featured_image": "https://example.com/images/ai-marketing.jpg",
      "seo": {
        "meta_title": "How AI is Revolutionizing Digital Marketing in 2025",
        "meta_description": "Discover how artificial intelligence is transforming digital marketing strategies and driving better results for businesses.",
        "focus_keyword": "AI in digital marketing"
      }
    },
    "word_count": 850,
    "read_time": 4
  }
}
```

#### Get Content

```
GET /content/{id}
```

**Response:**

```json
{
  "data": {
    "id": 203,
    "title": "How AI is Transforming Digital Marketing",
    "content_type": "blog",
    "content": "# How AI is Transforming Digital Marketing\n\nArtificial intelligence is revolutionizing the way businesses approach digital marketing...",
    "status": "draft",
    "created_at": "2025-01-26T15:30:00Z",
    "updated_at": "2025-01-26T15:30:00Z",
    "published_at": null,
    "metadata": {
      "categories": ["AI", "Digital Marketing", "Technology"],
      "tags": ["artificial intelligence", "marketing automation", "personalization"],
      "featured_image": "https://example.com/images/ai-marketing.jpg",
      "seo": {
        "meta_title": "How AI is Revolutionizing Digital Marketing in 2025",
        "meta_description": "Discover how artificial intelligence is transforming digital marketing strategies and driving better results for businesses.",
        "focus_keyword": "AI in digital marketing"
      }
    },
    "word_count": 850,
    "read_time": 4,
    "analytics": {
      "views": 0,
      "shares": 0,
      "comments": 0,
      "avg_time_on_page": null
    }
  }
}
```

#### Update Content

```
PUT /content/{id}
```

**Request Body:**

```json
{
  "title": "How AI is Revolutionizing Digital Marketing in 2025",
  "content": "# How AI is Revolutionizing Digital Marketing in 2025\n\nArtificial intelligence is transforming the way businesses approach digital marketing...",
  "status": "published",
  "metadata": {
    "categories": ["AI", "Digital Marketing", "Technology", "Trends"],
    "seo": {
      "meta_description": "Learn how AI is revolutionizing digital marketing with personalization, automation, and predictive analytics in 2025."
    }
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 203,
    "title": "How AI is Revolutionizing Digital Marketing in 2025",
    "content_type": "blog",
    "content": "# How AI is Revolutionizing Digital Marketing in 2025\n\nArtificial intelligence is transforming the way businesses approach digital marketing...",
    "status": "published",
    "created_at": "2025-01-26T15:30:00Z",
    "updated_at": "2025-01-26T16:45:00Z",
    "published_at": "2025-01-26T16:45:00Z",
    "metadata": {
      "categories": ["AI", "Digital Marketing", "Technology", "Trends"],
      "tags": ["artificial intelligence", "marketing automation", "personalization"],
      "featured_image": "https://example.com/images/ai-marketing.jpg",
      "seo": {
        "meta_title": "How AI is Revolutionizing Digital Marketing in 2025",
        "meta_description": "Learn how AI is revolutionizing digital marketing with personalization, automation, and predictive analytics in 2025.",
        "focus_keyword": "AI in digital marketing"
      }
    },
    "word_count": 850,
    "read_time": 4
  }
}
```

#### Delete Content

```
DELETE /content/{id}
```

**Response:**

```json
{
  "data": {
    "message": "Content deleted successfully"
  }
}
```

#### Generate Content

```
POST /content/generate
```

**Request Body:**

```json
{
  "content_type": "blog",
  "title": "Email Marketing Best Practices",
  "topics": ["email open rates", "subject line optimization", "personalization", "automation"],
  "tone": "professional",
  "length": "medium",
  "target_audience": "small business owners",
  "include_sections": ["introduction", "best practices", "examples", "conclusion"]
}
```

**Response:**

```json
{
  "data": {
    "title": "Email Marketing Best Practices: Boosting Engagement for Small Businesses",
    "content": "# Email Marketing Best Practices: Boosting Engagement for Small Businesses\n\n## Introduction\n\nEmail marketing remains one of the most effective channels for small businesses, offering an impressive ROI of $36 for every $1 spent...\n\n## Best Practices for Email Marketing Success\n\n### 1. Craft Compelling Subject Lines\n\nYour subject line is the gateway to your email content...\n\n### 2. Personalize Your Messages\n\nPersonalization goes beyond using a recipient's name...\n\n### 3. Optimize for Mobile Devices\n\nWith over 60% of emails opened on mobile devices...\n\n### 4. Implement Automation Workflows\n\nEmail automation allows you to send the right message at the right time...\n\n## Real-World Examples\n\n### Example 1: Welcome Series\n\nCompany XYZ implemented a 3-part welcome series that...\n\n### Example 2: Re-engagement Campaign\n\nA local boutique recovered 15% of inactive subscribers by...\n\n## Conclusion\n\nImplementing these email marketing best practices can significantly improve your engagement metrics and drive better results for your small business...",
    "metadata": {
      "word_count": 1200,
      "read_time": 6,
      "suggested_categories": ["Email Marketing", "Digital Marketing", "Small Business"],
      "suggested_tags": ["email marketing", "open rates", "subject lines", "personalization", "automation"]
    }
  }
}
```

### Campaign Endpoints

#### List Campaigns

```
GET /campaigns
```

**Query Parameters:**

- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10)
- `campaign_type`: Filter by campaign type (email, social, ad)
- `status`: Filter by status (draft, active, completed, paused)

**Response:**

```json
{
  "data": [
    {
      "id": 301,
      "name": "Spring Sale Email Campaign",
      "description": "Promotional campaign for our spring sale",
      "campaign_type": "email",
      "status": "active",
      "start_date": "2025-03-01T00:00:00Z",
      "end_date": "2025-03-15T23:59:59Z",
      "created_at": "2025-02-15T10:00:00Z",
      "updated_at": "2025-02-20T14:30:00Z",
      "metrics": {
        "sent": 1250,
        "opened": 437,
        "clicked": 189,
        "converted": 28
      }
    },
    {
      "id": 302,
      "name": "Product Launch Social Campaign",
      "description": "Social media campaign for new product launch",
      "campaign_type": "social",
      "status": "draft",
      "start_date": "2025-04-01T00:00:00Z",
      "end_date": "2025-04-30T23:59:59Z",
      "created_at": "2025-02-25T11:15:00Z",
      "updated_at": "2025-02-25T11:15:00Z",
      "metrics": null
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 2,
    "pages": 1
  }
}
```

#### Create Campaign

```
POST /campaigns
```

**Request Body:**

```json
{
  "name": "Summer Promotion Email Series",
  "description": "Three-part email series promoting summer products",
  "campaign_type": "email",
  "status": "draft",
  "start_date": "2025-06-01T00:00:00Z",
  "end_date": "2025-06-30T23:59:59Z",
  "configuration": {
    "audience": {
      "segments": ["active_customers", "summer_buyers_last_year"],
      "exclusions": ["unsubscribed"]
    },
    "content": {
      "emails": [
        {
          "subject": "Summer is here! Discover our new collection",
          "content_id": 205,
          "schedule": "2025-06-01T10:00:00Z"
        },
        {
          "subject": "20% off summer essentials - This week only!",
          "content_id": 206,
          "schedule": "2025-06-15T10:00:00Z"
        },
        {
          "subject": "Last chance: Summer promotion ends soon",
          "content_id": 207,
          "schedule": "2025-06-28T10:00:00Z"
        }
      ]
    },
    "settings": {
      "sender_name": "Your Brand",
      "sender_email": "marketing@yourbrand.com",
      "reply_to": "support@yourbrand.com",
      "tracking": {
        "opens": true,
        "clicks": true,
        "utm_parameters": {
          "source": "email",
          "medium": "campaign",
          "campaign": "summer_2025"
        }
      }
    }
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 303,
    "name": "Summer Promotion Email Series",
    "description": "Three-part email series promoting summer products",
    "campaign_type": "email",
    "status": "draft",
    "start_date": "2025-06-01T00:00:00Z",
    "end_date": "2025-06-30T23:59:59Z",
    "created_at": "2025-02-26T15:30:00Z",
    "updated_at": "2025-02-26T15:30:00Z",
    "configuration": {
      "audience": {
        "segments": ["active_customers", "summer_buyers_last_year"],
        "exclusions": ["unsubscribed"]
      },
      "content": {
        "emails": [
          {
            "subject": "Summer is here! Discover our new collection",
            "content_id": 205,
            "schedule": "2025-06-01T10:00:00Z"
          },
          {
            "subject": "20% off summer essentials - This week only!",
            "content_id": 206,
            "schedule": "2025-06-15T10:00:00Z"
          },
          {
            "subject": "Last chance: Summer promotion ends soon",
            "content_id": 207,
            "schedule": "2025-06-28T10:00:00Z"
          }
        ]
      },
      "settings": {
        "sender_name": "Your Brand",
        "sender_email": "marketing@yourbrand.com",
        "reply_to": "support@yourbrand.com",
        "tracking": {
          "opens": true,
          "clicks": true,
          "utm_parameters": {
            "source": "email",
            "medium": "campaign",
            "campaign": "summer_2025"
          }
        }
      }
    },
    "metrics": null
  }
}
```

#### Get Campaign

```
GET /campaigns/{id}
```

**Response:**

```json
{
  "data": {
    "id": 303,
    "name": "Summer Promotion Email Series",
    "description": "Three-part email series promoting summer products",
    "campaign_type": "email",
    "status": "draft",
    "start_date": "2025-06-01T00:00:00Z",
    "end_date": "2025-06-30T23:59:59Z",
    "created_at": "2025-02-26T15:30:00Z",
    "updated_at": "2025-02-26T15:30:00Z",
    "configuration": {
      "audience": {
        "segments": ["active_customers", "summer_buyers_last_year"],
        "exclusions": ["unsubscribed"]
      },
      "content": {
        "emails": [
          {
            "subject": "Summer is here! Discover our new collection",
            "content_id": 205,
            "schedule": "2025-06-01T10:00:00Z"
          },
          {
            "subject": "20% off summer essentials - This week only!",
            "content_id": 206,
            "schedule": "2025-06-15T10:00:00Z"
          },
          {
            "subject": "Last chance: Summer promotion ends soon",
            "content_id": 207,
            "schedule": "2025-06-28T10:00:00Z"
          }
        ]
      },
      "settings": {
        "sender_name": "Your Brand",
        "sender_email": "marketing@yourbrand.com",
        "reply_to": "support@yourbrand.com",
        "tracking": {
          "opens": true,
          "clicks": true,
          "utm_parameters": {
            "source": "email",
            "medium": "campaign",
            "campaign": "summer_2025"
          }
        }
      }
    },
    "metrics": null,
    "audience_size": 1250
  }
}
```

#### Update Campaign

```
PUT /campaigns/{id}
```

**Request Body:**

```json
{
  "name": "Summer Promotion Email Series 2025",
  "status": "active",
  "configuration": {
    "audience": {
      "segments": ["active_customers", "summer_buyers_last_year", "new_subscribers"],
      "exclusions": ["unsubscribed", "inactive_6months"]
    }
  }
}
```

**Response:**

```json
{
  "data": {
    "id": 303,
    "name": "Summer Promotion Email Series 2025",
    "description": "Three-part email series promoting summer products",
    "campaign_type": "email",
    "status": "active",
    "start_date": "2025-06-01T00:00:00Z",
    "end_date": "2025-06-30T23:59:59Z",
    "created_at": "2025-02-26T15:30:00Z",
    "updated_at": "2025-02-26T16:45:00Z",
    "configuration": {
      "audience": {
        "segments": ["active_customers", "summer_buyers_last_year", "new_subscribers"],
        "exclusions": ["unsubscribed", "inactive_6months"]
      },
      "content": {
        "emails": [
          {
            "subject": "Summer is here! Discover our new collection",
            "content_id": 205,
            "schedule": "2025-06-01T10:00:00Z"
          },
          {
            "subject": "20% off summer essentials - This week only!",
            "content_id": 206,
            "schedule": "2025-06-15T10:00:00Z"
          },
          {
            "subject": "Last chance: Summer promotion ends soon",
            "content_id": 207,
            "schedule": "2025-06-28T10:00:00Z"
          }
        ]
      },
      "settings": {
        "sender_name": "Your Brand",
        "sender_email": "marketing@yourbrand.com",
        "reply_to": "support@yourbrand.com",
        "tracking": {
          "opens": true,
          "clicks": true,
          "utm_parameters": {
            "source": "email",
            "medium": "campaign",
            "campaign": "summer_2025"
          }
        }
      }
    },
    "metrics": null,
    "audience_size": 1850
  }
}
```

#### Delete Campaign

```
DELETE /campaigns/{id}
```

**Response:**

```json
{
  "data": {
    "message": "Campaign deleted successfully"
  }
}
```

#### Get Campaign Metrics

```
GET /campaigns/{id}/metrics
```

**Query Parameters:**

- `start_date`: Start date for metrics (ISO format)
- `end_date`: End date for metrics (ISO format)
- `granularity`: Data granularity (hourly, daily, weekly, monthly)

**Response:**

```json
{
  "data": {
    "summary": {
      "sent": 1250,
      "delivered": 1230,
      "opened": 437,
      "clicked": 189,
      "converted": 28,
      "unsubscribed": 5,
      "bounced": 20,
      "revenue": 3450.75,
      "roi": 345.08
    },
    "timeline": [
      {
        "date": "2025-06-01",
        "metrics": {
          "sent": 1250,
          "delivered": 1230,
          "opened": 320,
          "clicked": 110,
          "converted": 15,
          "revenue": 1850.25
        }
      },
      {
        "date": "2025-06-15",
        "metrics": {
          "sent": 1245,
          "delivered": 1225,
          "opened": 380,
          "clicked": 145,
          "converted": 22,
          "revenue": 2750.50
        }
      },
      {
        "date": "2025-06-28",
        "metrics": {
          "sent": 1240,
          "delivered": 1220,
          "opened": 290,
          "clicked": 95,
          "converted": 18,
          "revenue": 1950.75
        }
      }
    ],
    "content_performance": [
      {
        "content_id": 205,
        "subject": "Summer is here! Discover our new collection",
        "sent": 1250,
        "opened": 320,
        "open_rate": 25.6,
        "clicked": 110,
        "click_rate": 8.8,
        "click_to_open_rate": 34.4
      },
      {
        "content_id": 206,
        "subject": "20% off summer essentials - This week only!",
        "sent": 1245,
        "opened": 380,
        "open_rate": 30.5,
        "clicked": 145,
        "click_rate": 11.6,
        "click_to_open_rate": 38.2
      },
      {
        "content_id": 207,
        "subject": "Last chance: Summer promotion ends soon",
        "sent": 1240,
        "opened": 290,
        "open_rate": 23.4,
        "clicked": 95,
        "click_rate": 7.7,
        "click_to_open_rate": 32.8
      }
    ],
    "audience_insights": {
      "demographics": {
        "age_groups": [
          {"range": "18-24", "percentage": 15},
          {"range": "25-34", "percentage": 35},
          {"range": "35-44", "percentage": 25},
          {"range": "45-54", "percentage": 15},
          {"range": "55+", "percentage": 10}
        ],
        "genders": [
          {"gender": "male", "percentage": 45},
          {"gender": "female", "percentage": 55}
        ],
        "locations": [
          {"country": "United States", "percentage": 65},
          {"country": "Canada", "percentage": 15},
          {"country": "United Kingdom", "percentage": 10},
          {"country": "Other", "percentage": 10}
        ]
      },
      "devices": [
        {"device": "mobile", "percentage": 65},
        {"device": "desktop", "percentage": 30},
        {"device": "tablet", "percentage": 5}
      ],
      "engagement_times": [
        {"hour": "8-10", "percentage": 15},
        {"hour": "10-12", "percentage": 25},
        {"hour": "12-14", "percentage": 20},
        {"hour": "14-16", "percentage": 15},
        {"hour": "16-18", "percentage": 15},
        {"hour": "18-20", "percentage": 10}
      ]
    }
  },
  "meta": {
    "campaign_id": 303,
    "campaign_name": "Summer Promotion Email Series 2025",
    "start_date": "2025-06-01T00:00:00Z",
    "end_date": "2025-06-30T23:59:59Z",
    "granularity": "daily"
  }
}
```

### Analytics Endpoints

#### Dashboard Analytics

```
GET /analytics/dashboard
```

**Query Parameters:**

- `start_date`: Start date for analytics (ISO format)
- `end_date`: End date for analytics (ISO format)
- `timezone`: Timezone for date calculations (default: UTC)

**Response:**

```json
{
  "data": {
    "summary": {
      "total_users": 1429,
      "active_users": 856,
      "conversion_rate": 3.89,
      "revenue": {
        "mrr": 11241,
        "arr": 134892,
        "growth": 12.5
      },
      "engagement": {
        "avg_session_duration": 325,
        "pages_per_session": 4.2,
        "bounce_rate": 32.5
      }
    },
    "trends": {
      "users": [
        {"date": "2025-01-01", "value": 1250},
        {"date": "2025-01-08", "value": 1280},
        {"date": "2025-01-15", "value": 1320},
        {"date": "2025-01-22", "value": 1375},
        {"date": "2025-01-29", "value": 1429}
      ],
      "revenue": [
        {"date": "2025-01-01", "value": 9850},
        {"date": "2025-01-08", "value": 10125},
        {"date": "2025-01-15", "value": 10450},
        {"date": "2025-01-22", "value": 10875},
        {"date": "2025-01-29", "value": 11241}
      ],
      "conversion_rate": [
        {"date": "2025-01-01", "value": 3.45},
        {"date": "2025-01-08", "value": 3.52},
        {"date": "2025-01-15", "value": 3.68},
        {"date": "2025-01-22", "value": 3.75},
        {"date": "2025-01-29", "value": 3.89}
      ]
    },
    "chatbot": {
      "conversations": 79,
      "messages": 542,
      "avg_conversation_length": 6.9,
      "satisfaction_score": 4.4,
      "resolution_rate": 87.5,
      "popular_topics": [
        {"topic": "pricing", "count": 24},
        {"topic": "features", "count": 18},
        {"topic": "technical support", "count": 15},
        {"topic": "account issues", "count": 12},
        {"topic": "other", "count": 10}
      ]
    },
    "content": {
      "total_views": 12450,
      "avg_engagement": 65.8,
      "top_performing": [
        {
          "id": 201,
          "title": "10 Effective Marketing Strategies for 2025",
          "views": 2450,
          "engagement": 78.5,
          "conversion_rate": 4.2
        },
        {
          "id": 203,
          "title": "How AI is Revolutionizing Digital Marketing in 2025",
          "views": 1850,
          "engagement": 72.3,
          "conversion_rate": 3.8
        }
      ]
    },
    "campaigns": {
      "active": 3,
      "completed": 5,
      "total_sent": 15250,
      "avg_open_rate": 28.5,
      "avg_click_rate": 12.3,
      "avg_conversion_rate": 2.4,
      "top_performing": [
        {
          "id": 301,
          "name": "Spring Sale Email Campaign",
          "type": "email",
          "open_rate": 35.0,
          "click_rate": 15.1,
          "conversion_rate": 2.2
        }
      ]
    },
    "subscription": {
      "distribution": [
        {"plan": "free", "count": 950, "percentage": 66.5},
        {"plan": "starter", "count": 320, "percentage": 22.4},
        {"plan": "professional", "count": 145, "percentage": 10.1},
        {"plan": "enterprise", "count": 14, "percentage": 1.0}
      ],
      "churn_rate": 3.88,
      "retention_rate": 96.12,
      "avg_lifetime_value": 850
    }
  },
  "meta": {
    "start_date": "2025-01-01T00:00:00Z",
    "end_date": "2025-01-31T23:59:59Z",
    "timezone": "UTC"
  }
}
```

#### User Analytics

```
GET /analytics/users
```

**Query Parameters:**

- `start_date`: Start date for analytics (ISO format)
- `end_date`: End date for analytics (ISO format)
- `segment`: User segment (all, free, paid, new, churned)
- `granularity`: Data granularity (daily, weekly, monthly)

**Response:**

```json
{
  "data": {
    "summary": {
      "total_users": 1429,
      "new_users": 179,
      "churned_users": 35,
      "growth_rate": 10.1,
      "churn_rate": 2.5,
      "active_users": {
        "daily": 325,
        "weekly": 856,
        "monthly": 1250
      }
    },
    "trends": {
      "total_users": [
        {"date": "2025-01-01", "value": 1250},
        {"date": "2025-01-08", "value": 1280},
        {"date": "2025-01-15", "value": 1320},
        {"date": "2025-01-22", "value": 1375},
        {"date": "2025-01-29", "value": 1429}
      ],
      "new_users": [
        {"date": "2025-01-01", "value": 0},
        {"date": "2025-01-08", "value": 45},
        {"date": "2025-01-15", "value": 52},
        {"date": "2025-01-22", "value": 65},
        {"date": "2025-01-29", "value": 17}
      ],
      "churned_users": [
        {"date": "2025-01-01", "value": 0},
        {"date": "2025-01-08", "value": 15},
        {"date": "2025-01-15", "value": 12},
        {"date": "2025-01-22", "value": 10},
        {"date": "2025-01-29", "value": 8}
      ]
    },
    "demographics": {
      "countries": [
        {"country": "United States", "count": 750, "percentage": 52.5},
        {"country": "Canada", "count": 180, "percentage": 12.6},
        {"country": "United Kingdom", "count": 145, "percentage": 10.1},
        {"country": "Australia", "count": 95, "percentage": 6.6},
        {"country": "Germany", "count": 75, "percentage": 5.2},
        {"country": "Other", "count": 184, "percentage": 12.9}
      ],
      "industries": [
        {"industry": "Retail", "count": 320, "percentage": 22.4},
        {"industry": "Technology", "count": 285, "percentage": 19.9},
        {"industry": "Marketing", "count": 245, "percentage": 17.1},
        {"industry": "Finance", "count": 180, "percentage": 12.6},
        {"industry": "Healthcare", "count": 150, "percentage": 10.5},
        {"industry": "Other", "count": 249, "percentage": 17.4}
      ],
      "company_sizes": [
        {"size": "1-10", "count": 450, "percentage": 31.5},
        {"size": "11-50", "count": 380, "percentage": 26.6},
        {"size": "51-200", "count": 250, "percentage": 17.5},
        {"size": "201-500", "count": 180, "percentage": 12.6},
        {"size": "501+", "count": 169, "percentage": 11.8}
      ]
    },
    "behavior": {
      "avg_session_duration": 325,
      "avg_sessions_per_user": 8.5,
      "feature_usage": [
        {"feature": "Chatbot", "usage_percentage": 78.5},
        {"feature": "Content Generation", "usage_percentage": 65.2},
        {"feature": "Analytics", "usage_percentage": 58.7},
        {"feature": "Campaigns", "usage_percentage": 45.3},
        {"feature": "Social Media", "usage_percentage": 38.9}
      ],
      "user_journey": {
        "activation_rate": 68.5,
        "adoption_rate": 42.3,
        "retention_rate": 85.7
      }
    },
    "subscription": {
      "distribution": [
        {"plan": "free", "count": 950, "percentage": 66.5},
        {"plan": "starter", "count": 320, "percentage": 22.4},
        {"plan": "professional", "count": 145, "percentage": 10.1},
        {"plan": "enterprise", "count": 14, "percentage": 1.0}
      ],
      "conversion_rate": {
        "free_to_paid": 3.89,
        "trial_to_paid": 32.5
      },
      "avg_lifetime_value": 850,
      "avg_revenue_per_user": 7.87
    }
  },
  "meta": {
    "start_date": "2025-01-01T00:00:00Z",
    "end_date": "2025-01-31T23:59:59Z",
    "segment": "all",
    "granularity": "weekly"
  }
}
```

## Webhooks

Webhooks allow you to receive real-time notifications when specific events occur in your account.

### Available Events

- `user.created`: A new user is created
- `user.updated`: A user's profile is updated
- `subscription.created`: A new subscription is created
- `subscription.updated`: A subscription is updated
- `subscription.canceled`: A subscription is canceled
- `chatbot.message`: A message is sent to a chatbot
- `campaign.started`: A campaign is started
- `campaign.completed`: A campaign is completed
- `content.published`: Content is published

### Webhook Configuration

To configure webhooks, use the dashboard or the API:

```
POST /webhooks
```

**Request Body:**

```json
{
  "url": "https://your-server.com/webhook",
  "events": ["chatbot.message", "campaign.started", "campaign.completed"],
  "secret": "your_webhook_secret"
}
```

**Response:**

```json
{
  "data": {
    "id": "wh_123456",
    "url": "https://your-server.com/webhook",
    "events": ["chatbot.message", "campaign.started", "campaign.completed"],
    "created_at": "2025-01-26T15:30:00Z"
  }
}
```

### Webhook Payload

Webhook payloads include the event type and relevant data:

```json
{
  "event": "chatbot.message",
  "created_at": "2025-01-26T15:30:00Z",
  "data": {
    "chatbot_id": 3,
    "conversation_id": 101,
    "message": {
      "id": 501,
      "sender": "user",
      "content": "What marketing strategies do you recommend for a small business?",
      "timestamp": "2025-01-26T15:30:00Z"
    }
  }
}
```

### Webhook Security

Webhooks include a signature header (`X-AI-Marketing-Signature`) that you can use to verify the payload:

```
X-AI-Marketing-Signature: t=1643214000,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e77a0e56ff536d0ce8e108d8bd
```

To verify the signature:

1. Extract the timestamp (`t`) and signature (`v1`) from the header
2. Create a string by concatenating the timestamp, a period, and the request body
3. Compute an HMAC with SHA-256 using your webhook secret
4. Compare the computed signature with the signature in the header

## SDKs & Libraries

We provide official SDKs for popular programming languages:

### JavaScript/TypeScript

```bash
npm install ai-marketing-tools-sdk
```

```javascript
import { AIMarketingTools } from 'ai-marketing-tools-sdk';

const client = new AIMarketingTools({
  apiKey: 'your_api_key'
});

// Get chatbots
const chatbots = await client.chatbots.list();

// Send message to chatbot
const response = await client.chatbots.sendMessage(3, {
  message: 'What marketing strategies do you recommend?',
  session_id: 'user_session_123'
});
```

### Python

```bash
pip install ai-marketing-tools
```

```python
from ai_marketing_tools import AIMarketingTools

client = AIMarketingTools(api_key='your_api_key')

# Get chatbots
chatbots = client.chatbots.list()

# Send message to chatbot
response = client.chatbots.send_message(
    chatbot_id=3,
    message='What marketing strategies do you recommend?',
    session_id='user_session_123'
)
```

### PHP

```bash
composer require ai-marketing-tools/sdk
```

```php
<?php
require 'vendor/autoload.php';

use AIMarketingTools\Client;

$client = new Client('your_api_key');

// Get chatbots
$chatbots = $client->chatbots->list();

// Send message to chatbot
$response = $client->chatbots->sendMessage(3, [
    'message' => 'What marketing strategies do you recommend?',
    'session_id' => 'user_session_123'
]);
```

## Best Practices

### Authentication

- Store API keys securely and never expose them in client-side code
- Implement token refresh logic to handle expired access tokens
- Use short-lived access tokens and long-lived refresh tokens
- Revoke tokens when they are no longer needed

### Rate Limiting

- Implement exponential backoff for rate limit errors
- Cache responses when appropriate to reduce API calls
- Batch operations when possible to reduce the number of requests
- Monitor your API usage to avoid hitting rate limits

### Error Handling

- Implement proper error handling for all API requests
- Check HTTP status codes and error messages
- Log errors for debugging and monitoring
- Implement retry logic for transient errors

### Performance

- Use pagination for large result sets
- Request only the fields you need
- Implement caching for frequently accessed data
- Use webhooks for real-time updates instead of polling

### Security

- Use HTTPS for all API requests
- Validate webhook signatures
- Implement proper access controls
- Regularly rotate API keys and secrets

---

## Need More Help?

If you can't find the information you need in this reference:

- **API Explorer**: Try our interactive API explorer at [api.ai-marketing-tools.com/explorer](https://api.ai-marketing-tools.com/explorer)
- **Developer Forum**: Join discussions at [community.ai-marketing-tools.com/developers](https://community.ai-marketing-tools.com/developers)
- **GitHub**: Check our SDK repositories at [github.com/ai-marketing-tools](https://github.com/ai-marketing-tools)
- **Support**: Contact developer support at [dev-support@ai-marketing-tools.com](mailto:dev-support@ai-marketing-tools.com)

---

© 2025 AI Marketing Tools. All rights reserved.

