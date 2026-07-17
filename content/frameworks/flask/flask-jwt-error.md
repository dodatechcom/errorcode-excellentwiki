---
title: "Flask-JWT Authentication Error"
description: "Flask-JWT raises authentication errors when JWT tokens are invalid, expired, or missing"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-JWT errors occur when JSON Web Token authentication fails due to invalid, expired, or missing tokens. These errors typically return `401 Unauthorized` responses and indicate issues with token generation, validation, or refresh mechanisms.

## Common Causes

- Expired JWT token
- Invalid or tampered JWT signature
- Missing `Authorization` header
- Incorrect `JWT_SECRET_KEY` configuration
- Token not refreshed before expiration

## How to Fix

Configure JWT properly:

```python
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

jwt = JWTManager(app)
```

Protect routes with JWT:

```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)
```

Handle JWT errors:

```python
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"msg": "Invalid token"}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"msg": "Missing authorization token"}), 401
```

Implement token refresh:

```python
from flask_jwt_extended import create_access_token, create_refresh_token

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = authenticate(username, password)
    if not user:
        return jsonify({"msg": "Bad credentials"}), 401
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify(access_token=access_token, refresh_token=refresh_token)

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
```

## Examples

```python
@app.route('/profile')
@jwt_required()
def profile():
    return jsonify(user=get_jwt_identity())
```

```text
flask_jwt_extended.exceptions.NoAuthorizationError: Missing Authorization Header
```

## Related Errors

- [Login error]({{< relref "/frameworks/flask/flask-login-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
