---
title: "[Solution] FastAPI JWT Expired Token Error"
description: "Fix FastAPI JWT expired token errors when authentication fails because tokens have passed their expiration time."
frameworks: ["fastapi"]
error-types: ["authentication-error"]
severities: ["error"]
---

When a JWT token expires, FastAPI returns a 401 Unauthorized error. Clients must refresh the token or re-authenticate.

## Common Causes

- Token `exp` claim has passed
- Server clock is out of sync with the token issuer
- `ALGORITHM` or `SECRET_KEY` changed between creation and verification
- Refresh token flow not implemented on the client
- Token issued by a different server instance with a different key

## How to Fix

### Verify Token Expiration Handling

```python
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

### Implement Refresh Token Flow

```python
@app.post("/token/refresh")
def refresh_token(refresh_token: str):
    payload = verify_token(refresh_token)
    new_access_token = create_access_token(data={"sub": payload["sub"]})
    return {"access_token": new_access_token}
```

## Examples

```python
from jose import jwt

token = jwt.encode({"sub": "user1", "exp": 1000000000}, "secret")
try:
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
except jwt.ExpiredSignatureError:
    print("Token has expired")
```
