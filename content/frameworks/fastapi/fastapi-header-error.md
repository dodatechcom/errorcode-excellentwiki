---
title: "[Solution] FastAPI Header Error -- How to Fix"
description: "Fix FastAPI header errors. Resolve missing headers, custom header parsing, and header validation issues."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI header error occurs when required headers are missing, have incorrect values, or cannot be parsed by the application.

## Why It Happens

Header errors happen due to missing required headers, incorrect header names, case sensitivity issues, or header value validation failures.

## Common Error Messages

```
fastapi.exceptions.MissingHeaderError: Missing required header
```

```
ValueError: Header 'Authorization' must be provided
```

```
fastapi.exceptions.HeaderError: Invalid header value
```

```
TypeError: Header parameter must be a string
```

## How to Fix It

### 1. Define Header Parameters

Use proper type annotations for headers.

```python
from fastapi import Header

@app.get('/items/')
async def get_items(
    authorization: str = Header(..., description='Bearer token'),
    x_request_id: str = Header(None, description='Request ID'),
    accept_language: str = Header('en', description='Preferred language')
):
    return {'token': authorization[:10] + '...'}
```

### 2. Validate Header Values

Add validation constraints.

```python
@app.post('/api/')
async def api_call(
    x_api_key: str = Header(..., min_length=32, max_length=64),
    content_type: str = Header('application/json'),
    x_timestamp: int = Header(..., description='Unix timestamp')
):
    if content_type != 'application/json':
        raise HTTPException(400, 'Content-Type must be application/json')
    return {'status': 'ok'}
```

### 3. Handle Missing Headers

Provide default values or error handling.

```python
@app.get('/api/')
async def api_call(
    authorization: str = Header(None),
    x_api_key: str = Header(None)
):
    if not authorization and not x_api_key:
        raise HTTPException(401, 'Either Authorization or X-API-Key required')
    return {'authenticated': True}
```

### 4. Use Header Dependency Pattern

Extract common header logic into dependencies.

```python
async def get_auth_headers(
    authorization: str = Header(None),
    x_api_key: str = Header(None)
):
    if authorization:
        return {'type': 'bearer', 'token': authorization}
    elif x_api_key:
        return {'type': 'api_key', 'key': x_api_key}
    raise HTTPException(401, 'Authentication required')

@app.get('/protected/')
async def protected(auth = Depends(get_auth_headers)):
    return {'auth_type': auth['type']}
```

## Common Scenarios

**Scenario 1: Header not found in request.**
Check exact header name and case.

**Scenario 2: Header validation fails.**
Check min_length, max_length constraints.

**Scenario 3: Custom header not accessible.**
Use `Header(..., convert_underscores=False)`.

## Prevent It

1. **Always validate required headers.**
Use `= Header(...)` for required.

2. **Document custom headers.**
Add descriptions for API consumers.

3. **Test header validation.**
Send requests without required headers.

