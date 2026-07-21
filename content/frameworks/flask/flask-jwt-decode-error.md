---
title: "[Solution] Flask JWT Decode Error"
description: "Fix Flask JWT decode errors when token verification fails or tokens are malformed."
frameworks: ["flask"]
error-types: ["authentication-error"]
severities: ["error"]
---

JWT decode errors in Flask occur when token verification fails due to incorrect secret key, expired tokens, or malformed token format.

## Common Causes

- Secret key used for decoding differs from encoding key
- Token has expired (exp claim exceeded)
- Token header contains unsupported algorithm
- Token is truncated or contains invalid characters
- Multiple secret keys used across services

## How to Fix

### Verify Token Correctly

```python
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            app.config["SECRET_KEY"],
            algorithms=["HS256"],
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError as e:
        return None  # Invalid token

@app.route("/protected")
def protected():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401
    token = auth_header.split(" ")[1]
    payload = verify_token(token)
    if not payload:
        return jsonify({"error": "Invalid token"}), 401
    return jsonify({"user": payload["sub"]})
```

### Use Consistent Secret Key

```python
import os

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-dev-key")
```

## Examples

```python
import jwt

token = jwt.encode({"sub": "user1", "exp": 1000000000}, "secret", algorithm="HS256")

# Bug -- wrong secret key
try:
    payload = jwt.decode(token, "wrong-secret", algorithms=["HS256"])
except jwt.InvalidSignatureError:
    print("Invalid signature")

# Fix -- use correct key
payload = jwt.decode(token, "secret", algorithms=["HS256"])
```
