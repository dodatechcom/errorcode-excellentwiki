---
title: "[Solution] Flask CORS Preflight Failed Error — How to Fix"
description: "Fix Flask CORS preflight errors. Resolve Cross-Origin Resource Sharing configuration and header issues."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask CORS preflight failed error occurs when the browser's OPTIONS preflight request is rejected or missing required headers. CORS is essential for frontend-backend communication across different domains.

## Why It Happens

CORS (Cross-Origin Resource Sharing) restricts web pages from making requests to a different domain. The browser sends a preflight OPTIONS request for complex requests that include custom headers, PUT/DELETE methods, or credentials. Errors occur when the server does not respond to OPTIONS, when `Access-Control-Allow-Origin` is missing, when required headers are absent from the response, or when credentials are not properly configured.

## Common Error Messages

```
Access to XMLHttpRequest at 'http://api.example.com' from origin 'http://localhost:3000' has been blocked by CORS policy
```

```
Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present
```

```
The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'
```

```
Method PUT is not allowed by Access-Control-Allow-Methods in preflight response
```

## How to Fix It

### 1. Install and Configure Flask-CORS

Use the Flask-CORS extension for proper CORS handling:

```python
# app.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "https://example.com"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True,
        "max_age": 600,
    }
})
```

### 2. Handle Preflight Requests Manually

If not using Flask-CORS, handle OPTIONS explicitly:

```python
from flask import make_response, request

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Max-Age'] = '600'
        return response

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    if origin in ['http://localhost:3000', 'https://example.com']:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
```

### 3. Configure for Credentials

When sending cookies or authorization headers:

```python
from flask_cors import CORS

# Must specify exact origin, not wildcard *
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://example.com"],
        "supports_credentials": True,
        "allow_headers": ["Content-Type", "Authorization"],
    }
})
```

### 4. Debug CORS Headers

Use curl to verify CORS headers in the response:

```bash
# Check preflight response
curl -v -X OPTIONS \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type, Authorization" \
  http://localhost:5000/api/data

# Check actual request
curl -v \
  -H "Origin: http://localhost:3000" \
  -H "Authorization: Bearer token123" \
  http://localhost:5000/api/data
```

## Common Scenarios

**Scenario 1: CORS works in browser but fails in curl.**
Browsers send preflight OPTIONS requests automatically, but curl does not. Test with `-X OPTIONS` to simulate the preflight.

**Scenario 2: CORS error after deploying to production.**
The production domain must be added to `origins`. Environment-specific CORS configuration is essential.

**Scenario 3: Wildcard origin with credentials.**
The CORS spec forbids `Access-Control-Allow-Origin: *` when `Access-Control-Allow-Credentials: true`. Always use explicit origins.

## Prevent It

1. **Use Flask-CORS instead of manual headers.** It handles edge cases and preflight caching automatically.

2. **Never use wildcard `*` with credentials.** Always specify explicit origins.

3. **Set `max_age` for preflight caching.** This reduces the number of OPTIONS requests the browser sends.
