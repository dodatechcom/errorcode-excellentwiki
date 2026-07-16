---
title: "Session error: session is missing"
description: "Flask raises an error when accessing or modifying a session that is not properly initialized or has expired"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["session", "cookie", "cookie-session", "signed-cookie"]
weight: 5
---

This error occurs when Flask cannot read or write session data because the session cookie is missing, invalid, or the session backend is unavailable.

## Common Causes

- `SECRET_KEY` is not set, preventing signed cookie sessions from working
- Session cookie domain or path does not match the request
- Using server-side sessions without a proper backend (Redis, database)
- Client blocks cookies or session cookie expired

## How to Fix

1. Set a strong `SECRET_KEY`:

```python
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(32)
```

2. Configure session cookie settings:

```python
app.config['SESSION_COOKIE_NAME'] = 'session'
app.config['SESSION_COOKIE_DOMAIN'] = '.example.com'
app.config['SESSION_COOKIE_PATH'] = '/'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
```

3. Use server-side sessions for larger data:

```python
from flask_session import Session

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379)
Session(app)
```

4. Handle missing session gracefully:

```python
@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    return f"Welcome, {user_id}"
```

## Examples

```python
from flask import session

app.secret_key = None  # No secret key

@app.route('/set')
def set_session():
    session['user'] = 'alice'  # Error: cannot sign session without secret
```

```text
RuntimeError: Session backend did not open a session. Check the configuration.
```

## Related Errors

- [SQLAlchemy error]({{< relref "/frameworks/flask/sqlalchemy-error" >}})
