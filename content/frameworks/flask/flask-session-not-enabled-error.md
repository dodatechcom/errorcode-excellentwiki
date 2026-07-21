---
title: "[Solution] Flask Session Not Enabled Error"
description: "Fix Flask session not enabled errors when trying to use session data without proper configuration."
frameworks: ["flask"]
error-types: ["configuration-error"]
severities: ["error"]
---

Flask session errors occur when `SECRET_KEY` is not configured or when sessions are accessed before the application is properly set up.

## Common Causes

- `SECRET_KEY` not set or is empty
- `SECRET_KEY` is not set before session usage
- Session cookie domain does not match the request domain
- Secure flag set but application uses HTTP
- SameSite attribute blocks cross-origin sessions

## How to Fix

### Configure Secret Key

```python
from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-in-production")
```

### Configure Session Parameters

```python
app.config["SESSION_COOKIE_NAME"] = "session_id"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False  # Set True for HTTPS
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["PERMANENT_SESSION_LIFETIME"] = 3600  # 1 hour
```

### Use Sessions in Views

```python
from flask import session

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    session["username"] = username
    session.permanent = True
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))
    return f"Welcome, {username}!"
```

## Examples

```python
from flask import Flask, session

app = Flask(__name__)

# Bug -- no SECRET_KEY
# app.config["SECRET_KEY"] not set

@app.route("/set")
def set_value():
    session["key"] = "value"  # RuntimeError: Session is not configured
    return "Set"

# Fix -- set SECRET_KEY
app.config["SECRET_KEY"] = "my-secret-key"

@app.route("/set-fixed")
def set_value_fixed():
    session["key"] = "value"
    return "Set"
```
