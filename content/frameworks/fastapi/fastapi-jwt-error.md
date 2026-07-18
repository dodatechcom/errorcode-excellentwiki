---
title: "[Solution] FastAPI JWT Error — How to Fix"
description: "Fix FastAPI JWT errors. Resolve token encoding, decoding, expiration, and signature verification issues."
frameworks: ["fastapi"]
error-types: ["authentication-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI JWT error occurs when JSON Web Tokens fail to encode, decode, or verify correctly.

## Why It Happens

JWT errors happen due to incorrect signing keys, expired tokens, malformed format, or algorithm mismatches.

## Common Error Messages

```
JWTError: Not enough segments
```

```
JWTError: Signature verification failed
```

```
JWTError: Signature has expired
```

```
DecodeError: Invalid token format
```

## How to Fix It

### 1. Encode JWT Tokens Correctly

Use proper encoding with expiration.

```python
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-256-bit-secret'
ALGORITHM = 'HS256'

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({'exp': expire, 'iat': datetime.utcnow()})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

### 2. Decode and Verify JWT Tokens

Properly decode and handle errors.

```python
from jose import JWTError, jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=401, detail='Invalid token')
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f'Invalid token: {str(e)}')
```

### 3. Handle Token Expiration

Implement refresh tokens.

```python
def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({'exp': expire, 'type': 'refresh'})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_refresh_token(token: str):
    payload = verify_token(token)
    if payload.get('type') != 'refresh':
        raise HTTPException(status_code=401, detail='Invalid token type')
    return payload
```

### 4. Rotate JWT Keys

Implement key rotation.

```python
SIGNING_KEY = 'current-secret'
PREVIOUS_KEY = 'previous-secret'

def decode_with_rotation(token: str):
    try:
        return jwt.decode(token, SIGNING_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        try:
            return jwt.decode(token, PREVIOUS_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=401, detail='Token expired')
```

## Common Scenarios

**Scenario 1: JWT decode fails with 'not enough segments'.**
Ensure token is `header.payload.signature`.

**Scenario 2: Token verification fails after secret change.**
Use key rotation during transition.

**Scenario 3: Expired token not returning proper error.**
Catch `ExpiredSignatureError`.

## Prevent It

1. **Use strong secret keys.**
Generate 256-bit random keys.

2. **Implement token refresh.**
Use short-lived access tokens.

3. **Validate token claims.**
Check `exp`, `iat`, and `sub`.

