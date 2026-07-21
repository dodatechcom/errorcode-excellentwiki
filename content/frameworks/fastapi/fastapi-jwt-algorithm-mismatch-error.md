---
title: "[Solution] FastAPI JWT Algorithm Mismatch Error"
description: "Fix FastAPI JWT algorithm mismatch errors when token signing and verification use different algorithms."
frameworks: ["fastapi"]
error-types: ["authentication-error"]
severities: ["error"]
---

When the JWT token is signed with one algorithm but verified with another, FastAPI raises an `AlgorithmMismatch` error.

## Common Causes

- Token signed with `HS256` but verified with `RS256` or vice versa
- Library default algorithm changed between versions
- Token issued by a third-party provider uses a different algorithm
- Configuration file has inconsistent algorithm settings
- Algorithm specified as string instead of constant

## How to Fix

### Use Consistent Algorithm Configuration

```python
from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_token(data: dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
```

### Support Multiple Algorithms

```python
from jose import jwt, JWTError
from fastapi import HTTPException

ALLOWED_ALGORITHMS = ["HS256", "RS256"]

def verify_token_multi(token: str) -> dict:
    try:
        unverified = jwt.get_unverified_header(token)
        alg = unverified.get("alg")
        if alg not in ALLOWED_ALGORITHMS:
            raise JWTError(f"Unsupported algorithm: {alg}")
        return jwt.decode(token, SECRET_KEY, algorithms=ALLOWED_ALGORITHMS)
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))
```

## Examples

```python
from jose import jwt

token = jwt.encode({"sub": "user1"}, "secret", algorithm="HS256")

try:
    payload = jwt.decode(token, "secret", algorithms=["RS256"])
except jwt.AlgorithmMismatchError as e:
    print(f"Algorithm mismatch: {e}")
```

Ensure the same algorithm is used for both signing and verification.
