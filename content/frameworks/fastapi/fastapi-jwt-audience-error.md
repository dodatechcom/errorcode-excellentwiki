---
title: "[Solution] FastAPI JWT Audience Error"
description: "Fix FastAPI JWT audience validation errors when tokens are rejected due to incorrect audience claims."
frameworks: ["fastapi"]
error-types: ["authentication-error"]
severities: ["error"]
---

JWT audience (`aud`) claim validation fails when the token's audience does not match the expected audience.

## Common Causes

- Token issued with audience `service-a` but verified by `service-b`
- Missing audience claim in the token
- `audience` parameter in `jwt.decode` does not match the token
- Token issued by a third-party IdP with a different audience URI
- Case sensitivity mismatch in audience strings

## How to Fix

### Set Correct Audience During Verification

```python
from jose import jwt
from fastapi import HTTPException

SECRET_KEY = "secret"
ALGORITHM = "HS256"
EXPECTED_AUDIENCE = "https://api.myapp.com"

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            audience=EXPECTED_AUDIENCE,
        )
        return payload
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
```

### Create Tokens with Audience

```python
from datetime import datetime, timedelta, timezone

def create_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "aud": EXPECTED_AUDIENCE,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
```

## Examples

```python
from jose import jwt

token = jwt.encode(
    {"sub": "user1", "aud": "https://service-a.com"},
    "secret",
    algorithm="HS256",
)

try:
    payload = jwt.decode(token, "secret", algorithms=["HS256"], audience="https://service-b.com")
except jwt.JWTError as e:
    print(f"Error: {e}")

payload = jwt.decode(token, "secret", algorithms=["HS256"], audience="https://service-a.com")
```

Ensure all services agree on the audience URI for shared tokens.
