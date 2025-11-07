# API Design Patterns

Best practices for designing RESTful APIs that are intuitive, scalable, and maintainable.

## Table of Contents

1. [REST Principles](#rest-principles)
2. [URL Structure](#url-structure)
3. [HTTP Methods](#http-methods)
4. [Status Codes](#status-codes)
5. [Request/Response Format](#requestresponse-format)
6. [Error Handling](#error-handling)
7. [Authentication & Authorization](#authentication--authorization)
8. [Versioning](#versioning)
9. [Pagination](#pagination)
10. [Filtering & Sorting](#filtering--sorting)
11. [Rate Limiting](#rate-limiting)
12. [Caching](#caching)
13. [Best Practices](#best-practices)

## REST Principles

### Core Concepts

1. **Stateless**: Each request contains all information needed
2. **Client-Server**: Separation of concerns
3. **Cacheable**: Responses can be cached
4. **Uniform Interface**: Consistent patterns
5. **Layered System**: Can use intermediaries (load balancers, proxies)

### Resource-Oriented Design

Think in terms of resources (nouns), not actions (verbs):

✅ Good:
```
GET    /users
POST   /users
GET    /users/:id
PATCH  /users/:id
DELETE /users/:id
```

❌ Bad:
```
GET    /getUsers
POST   /createUser
GET    /getUserById
POST   /updateUser
POST   /deleteUser
```

## URL Structure

### General Rules

1. **Use nouns, not verbs**
   ```
   ✅ GET /articles
   ❌ GET /getArticles
   ```

2. **Use plural nouns for collections**
   ```
   ✅ GET /users
   ❌ GET /user
   ```

3. **Use hyphens for readability**
   ```
   ✅ /user-preferences
   ❌ /user_preferences
   ❌ /userPreferences
   ```

4. **Use lowercase**
   ```
   ✅ /users/123/posts
   ❌ /Users/123/Posts
   ```

5. **Avoid trailing slashes**
   ```
   ✅ /users
   ❌ /users/
   ```

### Nested Resources

Use nesting to show relationships (limit to 2-3 levels):

```
GET /users/:userId/posts
GET /users/:userId/posts/:postId
GET /users/:userId/posts/:postId/comments
```

For deeper nesting, use query parameters:

```
✅ GET /comments?postId=123&userId=456
❌ GET /users/:userId/posts/:postId/comments/:commentId/replies
```

### Actions on Resources

For actions that don't fit CRUD:

```
POST /users/:id/activate
POST /posts/:id/publish
POST /orders/:id/cancel
POST /cart/:id/checkout
```

## HTTP Methods

### Standard CRUD Operations

| Method | Purpose | Idempotent | Safe | Request Body | Response Body |
|--------|---------|-----------|------|--------------|---------------|
| GET | Retrieve | Yes | Yes | No | Yes |
| POST | Create | No | No | Yes | Yes |
| PUT | Replace entire resource | Yes | No | Yes | Yes |
| PATCH | Partial update | No | No | Yes | Yes |
| DELETE | Remove | Yes | No | No | Optional |
| HEAD | Get headers only | Yes | Yes | No | No |
| OPTIONS | Get available methods | Yes | Yes | No | Yes |

### Examples

**GET - Retrieve resources**
```http
GET /api/v1/users
GET /api/v1/users/550e8400-e29b-41d4-a716-446655440000
```

**POST - Create resource**
```http
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securePassword123"
}
```

**PATCH - Partial update**
```http
PATCH /api/v1/users/550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
  "email": "newemail@example.com"
}
```

**PUT - Replace entire resource**
```http
PUT /api/v1/users/550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "fullName": "John Doe",
  "role": "user"
}
```

**DELETE - Remove resource**
```http
DELETE /api/v1/users/550e8400-e29b-41d4-a716-446655440000
```

## Status Codes

### Success (2xx)

| Code | Name | Usage |
|------|------|-------|
| 200 | OK | Successful GET, PATCH, PUT |
| 201 | Created | Successful POST (resource created) |
| 202 | Accepted | Request accepted for processing (async) |
| 204 | No Content | Successful DELETE or update with no response body |

### Client Errors (4xx)

| Code | Name | Usage |
|------|------|-------|
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Conflict with current state (e.g., duplicate) |
| 422 | Unprocessable Entity | Valid syntax but semantic errors |
| 429 | Too Many Requests | Rate limit exceeded |

### Server Errors (5xx)

| Code | Name | Usage |
|------|------|-------|
| 500 | Internal Server Error | Generic server error |
| 502 | Bad Gateway | Invalid response from upstream server |
| 503 | Service Unavailable | Server temporarily unavailable |
| 504 | Gateway Timeout | Upstream server timeout |

### Usage Examples

```javascript
// Success
res.status(200).json({ data: users });
res.status(201).json({ data: newUser });
res.status(204).send();

// Client errors
res.status(400).json({ error: 'INVALID_EMAIL', message: 'Email format is invalid' });
res.status(401).json({ error: 'UNAUTHORIZED', message: 'Authentication required' });
res.status(404).json({ error: 'NOT_FOUND', message: 'User not found' });

// Server errors
res.status(500).json({ error: 'INTERNAL_ERROR', message: 'An unexpected error occurred' });
```

## Request/Response Format

### JSON Structure

**Standard Success Response:**
```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "username": "johndoe",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

**Collection Response:**
```json
{
  "data": [
    { "id": "1", "name": "Item 1" },
    { "id": "2", "name": "Item 2" }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 42,
    "pages": 3
  }
}
```

**Error Response:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "email": ["Email is required", "Email format is invalid"],
      "username": ["Username must be at least 3 characters"]
    }
  }
}
```

### Naming Conventions

Use **camelCase** for JSON field names:

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "createdAt": "2024-01-15T10:30:00Z"
}
```

### Date/Time Format

Always use ISO 8601 format with timezone:

```json
{
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T14:25:00Z"
}
```

## Error Handling

### Standard Error Structure

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {},
    "timestamp": "2024-01-15T10:30:00Z",
    "path": "/api/v1/users",
    "requestId": "req-123456"
  }
}
```

### Error Code Patterns

Use consistent error codes:

```
VALIDATION_ERROR
AUTHENTICATION_REQUIRED
PERMISSION_DENIED
RESOURCE_NOT_FOUND
DUPLICATE_RESOURCE
RATE_LIMIT_EXCEEDED
INTERNAL_ERROR
SERVICE_UNAVAILABLE
```

### Validation Errors

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": {
      "email": [
        "Email is required",
        "Email must be valid"
      ],
      "password": [
        "Password must be at least 8 characters"
      ]
    }
  }
}
```

### Implementation Example

```javascript
class APIError extends Error {
  constructor(code, message, statusCode = 500, details = {}) {
    super(message);
    this.code = code;
    this.statusCode = statusCode;
    this.details = details;
  }

  toJSON() {
    return {
      error: {
        code: this.code,
        message: this.message,
        details: this.details,
        timestamp: new Date().toISOString()
      }
    };
  }
}

// Usage
throw new APIError(
  'VALIDATION_ERROR',
  'Invalid input data',
  400,
  { email: ['Email is required'] }
);
```

## Authentication & Authorization

### JWT (Recommended)

**Login Flow:**
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "refresh_token_here",
    "expiresIn": 3600,
    "user": {
      "id": "123",
      "email": "user@example.com"
    }
  }
}
```

**Using Token:**
```http
GET /api/v1/users/me
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### OAuth 2.0

For third-party integrations:

```http
GET /api/v1/auth/google
GET /api/v1/auth/google/callback
```

### API Keys

For server-to-server communication:

```http
GET /api/v1/data
X-API-Key: your_api_key_here
```

### Permission Patterns

**Role-Based Access Control (RBAC):**
```javascript
{
  "user": {
    "id": "123",
    "role": "admin" // admin, user, guest
  }
}
```

**Attribute-Based Access Control (ABAC):**
```javascript
{
  "user": {
    "id": "123",
    "permissions": ["users.read", "users.write", "posts.read"]
  }
}
```

## Versioning

### URI Versioning (Recommended)

```
https://api.example.com/v1/users
https://api.example.com/v2/users
```

**Pros:**
- Clear and explicit
- Easy to route
- Easy to deprecate old versions

### Header Versioning

```http
GET /api/users
Accept: application/vnd.api.v1+json
```

### Version Migration Strategy

1. **Deprecation period**: Announce deprecation 6-12 months in advance
2. **Support multiple versions**: Run v1 and v2 simultaneously
3. **Documentation**: Clear migration guides
4. **Monitoring**: Track usage of old versions

```json
{
  "deprecation": {
    "version": "v1",
    "sunset": "2025-12-31",
    "info": "https://api.example.com/docs/migration"
  }
}
```

## Pagination

### Offset-Based (Simple)

```http
GET /api/v1/users?page=2&limit=20
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 100,
    "pages": 5,
    "hasNext": true,
    "hasPrev": true
  }
}
```

### Cursor-Based (Scalable)

```http
GET /api/v1/users?cursor=eyJpZCI6MTAwfQ&limit=20
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "nextCursor": "eyJpZCI6MTIwfQ",
    "prevCursor": "eyJpZCI6ODAwfQ",
    "hasMore": true
  }
}
```

**Pros of Cursor:**
- Consistent results during pagination
- No performance degradation with deep pages
- Handles real-time data updates

## Filtering & Sorting

### Filtering

```http
GET /api/v1/users?role=admin&status=active
GET /api/v1/posts?published=true&authorId=123
GET /api/v1/products?minPrice=100&maxPrice=500
```

### Advanced Filtering

```http
GET /api/v1/users?filter[role]=admin&filter[status]=active
GET /api/v1/posts?search=javascript&tags=tutorial,api
```

### Sorting

```http
GET /api/v1/users?sort=createdAt:desc
GET /api/v1/posts?sort=title:asc,createdAt:desc
```

### Field Selection (Sparse Fieldsets)

```http
GET /api/v1/users?fields=id,email,username
```

**Response:**
```json
{
  "data": [
    { "id": "1", "email": "user1@example.com", "username": "user1" },
    { "id": "2", "email": "user2@example.com", "username": "user2" }
  ]
}
```

## Rate Limiting

### Response Headers

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640000000
Retry-After: 3600
```

### Rate Limit Exceeded Response

```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1640000000
Retry-After: 3600

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again in 1 hour.",
    "retryAfter": 3600
  }
}
```

### Rate Limit Strategies

1. **Per User**: 1000 requests per hour
2. **Per IP**: 100 requests per minute
3. **Per Endpoint**: Different limits for different endpoints
4. **Tiered**: Different limits for free vs paid users

```javascript
// Example rate limit configuration
{
  "/api/v1/users": { limit: 100, window: "15m" },
  "/api/v1/posts": { limit: 200, window: "15m" },
  "/api/v1/search": { limit: 10, window: "1m" }
}
```

## Caching

### Cache Headers

```http
Cache-Control: public, max-age=3600
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 15 Jan 2024 10:30:00 GMT
```

### Conditional Requests

```http
GET /api/v1/users/123
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"

Response:
HTTP/1.1 304 Not Modified
```

### Cache Strategies

1. **No Cache**: Frequently changing data
   ```http
   Cache-Control: no-cache, no-store, must-revalidate
   ```

2. **Short Cache**: User-specific data
   ```http
   Cache-Control: private, max-age=300
   ```

3. **Long Cache**: Public, static data
   ```http
   Cache-Control: public, max-age=86400
   ```

## Best Practices

### 1. Use HTTPS Everywhere

Always use HTTPS in production.

### 2. Accept and Return JSON

```http
Content-Type: application/json
Accept: application/json
```

### 3. Use Standard HTTP Methods Correctly

Don't use POST for everything.

### 4. Provide Comprehensive Documentation

Use OpenAPI/Swagger for API documentation.

### 5. Handle Errors Gracefully

Always return meaningful error messages.

### 6. Version Your API from Day One

Even if you think you won't need it.

### 7. Be Consistent

Use the same patterns across all endpoints.

### 8. Optimize for Common Use Cases

Design endpoints for actual client needs.

### 9. Log Everything

Log requests, responses, and errors for debugging.

### 10. Monitor Performance

Track response times, error rates, and usage patterns.

### 11. Implement Health Checks

```http
GET /health
Response: { "status": "ok", "timestamp": "2024-01-15T10:30:00Z" }

GET /health/db
Response: { "status": "ok", "latency": "5ms" }
```

### 12. Use Request IDs

Add unique IDs to track requests across services:

```http
X-Request-ID: 550e8400-e29b-41d4-a716-446655440000
```

### 13. Support CORS Properly

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PATCH, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
```

### 14. Handle Timeouts

Set reasonable timeouts and return 504 when exceeded.

### 15. Use Webhooks for Events

Instead of polling, push events to clients:

```http
POST https://client.com/webhooks
X-Webhook-Signature: sha256=...

{
  "event": "user.created",
  "data": { ... }
}
```

## Complete Example

```javascript
// Express.js API example
const express = require('express');
const app = express();

app.use(express.json());

// Middleware
app.use(requestLogger);
app.use(rateLimiter);
app.use(authenticate);

// Routes
app.get('/api/v1/users', async (req, res) => {
  try {
    const { page = 1, limit = 20, sort = 'createdAt:desc' } = req.query;

    const users = await User.find()
      .sort(parseSort(sort))
      .skip((page - 1) * limit)
      .limit(parseInt(limit));

    const total = await User.countDocuments();

    res.status(200).json({
      data: users,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total,
        pages: Math.ceil(total / limit)
      }
    });
  } catch (error) {
    next(error);
  }
});

// Error handler
app.use((error, req, res, next) => {
  res.status(error.statusCode || 500).json({
    error: {
      code: error.code || 'INTERNAL_ERROR',
      message: error.message,
      details: error.details || {},
      requestId: req.id
    }
  });
});
```

## Resources

- [REST API Tutorial](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Roy Fielding's Dissertation on REST](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
