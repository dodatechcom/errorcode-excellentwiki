---
title: "[Solution] Flask Session Permanent Error"
description: "Fix Flask session permanent errors when permanent sessions do not persist correctly or expire unexpectedly."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Permanent session errors occur when `session.permanent` is not set correctly, causing sessions to expire at browser close instead of a specified time.

## Common Causes

- `session.permanent` not set to True
- `PERMANENT_SESSION_LIFETIME` not configured
- Secret key changes, invalidating sessions
- Browser cookie settings block long-lived cookies
- Session cookie domain mismatch

## How to Fix

### Configure Permanent Sessions

```python
from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

@app.route("/login", methods=["POST"])
def login():
    user = authenticate(request.form)
    if user:
        session["user_id"] = user.id
        session.permanent = True  # Important!
        return redirect(url_for("dashboard"))
    return "Invalid credentials", 401
```

### Set Permanent Flag on Login

```python
@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(username=request.form["username"]).first()
    if user and user.check_password(request.form["password"]):
        session["user_id"] = user.id
        session.permanent = True
        return redirect(url_for("dashboard"))
    return "Invalid credentials", 401
```

### Handle Session Expiry

```python
@app.before_request
def check_session():
    if "user_id" not in session:
        return redirect(url_for("login"))
```

## Examples

```python
from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)

# Bug -- permanent not set
@app.route("/login-broken")
def login_broken():
    session["user_id"] = 1
    # Session expires when browser closes

# Fix -- set permanent flag
@app.route("/login-fixed")
def login_fixed():
    session["user_id"] = 1
    session.permanent = True  # Session persists for 7 days
```
