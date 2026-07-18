---
title: "[Solution] FastAPI Authentication Error — How to Fix"
description: "Fix FastAPI authentication errors. Resolve OAuth2, API key, and token-based authentication failures."
frameworks: ["fastapi"]
error-types: ["authentication-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI authentication error occurs when users cannot authenticate, tokens are invalid, or auth middleware fails.

## Why It Happens

Authentication errors happen due to incorrect OAuth2 configuration, invalid tokens, missing headers, or incorrect password hashing.

## Common Error Messages

```
HTTPException: 401 Not authenticated
```

```
OAuth2Error: invalid_client
```

```
JWTError: Not enough segments
```

```
HTTPException: 403 Forbidden
```

## How to Fix It

### 1. Implement OAuth2 Password Flow

Set up OAuth2 with password-based auth.

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect credentials')
    return {'access_token': create_access_token(data={'sub': user.email}), 'token_type': 'bearer'}
```

### 2. Use API Key Authentication

Implement API key auth.

```python
from fastapi import Security
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name='X-API-Key')

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != 'valid-api-key':
        raise HTTPException(status_code=403, detail='Invalid API key')
    return api_key

@app.get('/api/data')
async def get_data(api_key: str = Depends(verify_api_key)):
    return {'data': 'secret'}
```

### 3. Handle Token Refresh

Implement token refresh for long sessions.

```python
@app.post('/refresh')
async def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        new_token = create_access_token(data={'sub': payload['sub']})
        return {'access_token': new_token, 'token_type': 'bearer'}
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid refresh token')
```

### 4. Add Role-Based Access Control

Implement role-based permissions.

```python
from enum import Enum

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

def require_role(allowed_roles: list[Role]):
    async def role_checker(current_user = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail='Insufficient permissions')
        return current_user
    return role_checker
```

## Common Scenarios

**Scenario 1: Login returns 401 for valid credentials.**
Check password hashing logic.

**Scenario 2: Token expired error.**
Implement token refresh.

**Scenario 3: API key rejected.**
Verify header name matches exactly.

## Prevent It

1. **Use HTTPS in production.**
Never transmit tokens over plain HTTP.

2. **Store secrets in environment variables.**
Never hardcode keys.

3. **Implement token expiration.**
Set reasonable lifetimes.

