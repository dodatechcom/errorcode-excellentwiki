---
title: "[Solution] Flask JWT Token Error — How to Fix"
description: "Fix Flask JWT token errors. Resolve JWT authentication, token validation, and authorization issues."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask JWT token error occurs when JSON Web Token authentication fails due to invalid, expired, or malformed tokens. JWT-based authentication is common in Flask APIs but requires careful implementation.

## Why It Happens

JWT tokens must be properly signed, validated, and refreshed. Errors occur when the signing secret is wrong, when tokens expire without refresh, when the token payload is malformed, when the `Authorization` header is missing, or when the token algorithm doesn't match the verification algorithm.

## Common Error Messages

```
jwt.exceptions.InvalidTokenError: Signature verification failed
```

```
jwt.exceptions.ExpiredSignatureError: Signature has expired
```

```
jwt.exceptions.DecodeError: Not enough segments
```

```
Unauthorized: Missing Authorization Header
```

## How to Fix It

### 1. Configure JWT Correctly

Set up JWT with proper settings:

```python
# extensions.py
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# app.py
from flask import Flask
from extensions import jwt

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Use env variable
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    jwt.init_app(app)
    return app
```

### 2. Implement Token Authentication

Create login endpoint and protected routes:

```python
from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
        }), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({'user': user.to_dict()})
```

### 3. Handle Token Refresh and Revocation

Implement token refresh and logout:

```python
from flask_jwt_extended import jwt_required, get_jwt

# Token blacklist (use Redis in production)
blacklisted_tokens = set()

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({'access_token': access_token}), 200

@app.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    blacklisted_tokens.add(jti)
    return jsonify({'message': 'Logged out'}), 200

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklisted_tokens
```

### 4. Validate Token Claims

Add custom claims and validation:

```python
from flask_jwt_extended import verify_jwt_in_request
from functools import wraps

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get('role') != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper

# Add claims when creating tokens
@app.route('/login', methods=['POST'])
def login():
    user = authenticate(request.json)
    if user:
        additional_claims = {'role': user.role}
        token = create_access_token(
            identity=user.id,
            additional_claims=additional_claims
        )
        return jsonify({'access_token': token})

# Protected admin route
@app.route('/admin/users', methods=['GET'])
@jwt_required()
@admin_required
def admin_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])
```

## Common Scenarios

**Scenario 1: Token works in one environment but not another.**
The `JWT_SECRET_KEY` must be the same across all environments. If it differs, tokens signed in one environment won't validate in another.

**Scenario 2: CORS blocks JWT header.**
Ensure CORS is configured to allow the `Authorization` header:

```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*", "headers": ["Authorization", "Content-Type"]}})
```

**Scenario 3: Token expires too quickly.**
Adjust `JWT_ACCESS_TOKEN_EXPIRES` for your use case. For long-running operations, consider using refresh tokens instead of extending access token lifetime.

## Prevent It

1. **Store `JWT_SECRET_KEY` in environment variables.** Never commit secrets to version control.

2. **Use short-lived access tokens** (15 minutes) and longer-lived refresh tokens (30 days).

3. **Implement token revocation** for logout and security incidents using a blacklist.
