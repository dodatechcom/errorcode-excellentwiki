---
title: "[Solution] Flask Session Expired Error"
description: "Fix Flask session expired errors when user sessions are lost or invalidated unexpectedly."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Session expired errors occur when the session cookie has exceeded its lifetime or the secret key was changed.

## Common Causes

- `PERMANENT_SESSION_LIFETIME` too short
- Secret key changed between server restarts
- Session cookie domain mismatch
- Browser cleared cookies
- Server restarted with new secret key

## How to Fix

### Configure Session Lifetime

```python
from datetime import timedelta

app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)
app.config["SESSION_COOKIE_NAME"] = "session_id"
```

### Handle Session Expiry Gracefully

```python
from flask import session, redirect, url_for

@app.before_request
def check_session():
    if "user_id" not in session:
        return redirect(url_for("login"))
```

### Use Consistent Secret Key

```python
import os

# Set in environment variable, not in code
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
```

## Examples

```python
from flask import Flask, session

app = Flask(__name__)

# Bug -- secret key changes on restart
app.config["SECRET_KEY"] = os.urandom(24)  # Different every restart!

# Fix -- use fixed secret key
app.config["SECRET_KEY"] = "fixed-secret-key"
```

Changing the secret key invalidates all existing sessions.
