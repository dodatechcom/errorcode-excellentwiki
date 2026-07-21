---
title: "[Solution] Flask Session Cookie Error"
description: "Fix Flask session cookie errors when session cookies are not set, rejected, or expire incorrectly."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Session cookie errors occur when the browser rejects session cookies due to security settings, domain mismatches, or missing configuration.

## Common Causes

- `SESSION_COOKIE_SECURE` set but application uses HTTP
- `SESSION_COOKIE_DOMAIN` does not match request domain
- SameSite attribute blocks cross-origin cookies
- Secret key not set before session creation
- Cookie size exceeds browser limit

## How to Fix

### Configure Session Cookie Settings

```python
app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["SESSION_COOKIE_NAME"] = "session_id"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False  # True for HTTPS
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_DOMAIN"] = None  # Use default
```

### Handle Cookie Security

```python
# For development (HTTP)
app.config["SESSION_COOKIE_SECURE"] = False

# For production (HTTPS)
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
```

### Set Session Data

```python
from flask import session

@app.route("/login", methods=["POST"])
def login():
    user = authenticate(request.form)
    if user:
        session["user_id"] = user.id
        session.permanent = True
        return redirect(url_for("dashboard"))
    return "Invalid credentials", 401
```

## Examples

```python
from flask import Flask, session

app = Flask(__name__)

# Bug -- secure cookie on HTTP
app.config["SESSION_COOKIE_SECURE"] = True  # Cookie rejected on HTTP

# Fix -- disable secure for development
app.config["SESSION_COOKIE_SECURE"] = False
```
