---
title: "[Solution] FastAPI CORS Error -- How to Fix"
description: "Fix FastAPI CORS errors. Resolve cross-origin resource sharing and preflight request issues."
frameworks: ["fastapi"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI CORS error occurs when cross-origin requests are blocked by the browser's same-origin policy.

## Why It Happens

CORS errors happen when the API does not include proper `Access-Control-Allow-Origin` headers, when preflight requests fail, or when credentials lack proper configuration.

## Common Error Messages

```
Access to XMLHttpRequest has been blocked by CORS policy
```

```
No 'Access-Control-Allow-Origin' header is present
```

```
Method PUT is not allowed by Access-Control-Allow-Methods
```

```
Access-Control-Allow-Origin must not be the wildcard
```

## How to Fix It

### 1. Configure CORS Middleware

Add CORSMiddleware with proper settings.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://example.com'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
```

### 2. Handle Preflight Requests

Ensure OPTIONS requests are handled.

```python
@app.options('/api/data')
async def options_handler():
    return JSONResponse(
        status_code=200,
        headers={
            'Access-Control-Allow-Origin': 'https://example.com',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        }
    )
```

### 3. Use Environment-Based Origins

Configure origins from environment.

```python
import os
allowed_origins = os.getenv('ALLOWED_ORIGINS', '').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
```

### 4. Handle Credentials Correctly

Configure credentials with specific origins.

```python
# Cannot use allow_origins=['*'] with credentials=True
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://example.com', 'https://www.example.com'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
```

## Common Scenarios

**Scenario 1: Browser blocks with CORS error.**
Add `Access-Control-Allow-Origin` header.

**Scenario 2: Preflight request fails.**
Ensure OPTIONS returns correct headers.

**Scenario 3: Credentials not sent.**
Set `allow_credentials=True` with specific origins.

## Prevent It

1. **List specific origins.**
Never use `*` with credentials.

2. **Test CORS in browser.**
Use dev tools to verify headers.

3. **Use env vars for origins.**
Don't hardcode origins.

