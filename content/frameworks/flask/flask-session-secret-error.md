---
title: "[Solution] Flask Session Secret Key Error"
description: "Fix Flask session secret key errors when SECRET_KEY is missing, weak, or changes between restarts."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
---

Session secret key errors occur when `SECRET_KEY` is not configured, is too weak, or changes between server restarts, invalidating all sessions.

## Common Causes

- `SECRET_KEY` not set or empty
- Secret key changes on every restart (using `os.urandom`)
- Secret key is predictable or hardcoded in source code
- Secret key does not match across multiple instances
- Secret key too short for cryptographic security

## How to Fix

### Generate Strong Secret Key

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Configure Secret Key Properly

```python
import os
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if not app.config["SECRET_KEY"]:
    raise RuntimeError("SECRET_KEY environment variable not set")
```

### Use Environment Variables

```bash
export SECRET_KEY="your-generated-secret-key-here"
```

### Avoid Common Mistakes

```python
# Bug -- different key every restart
app.config["SECRET_KEY"] = os.urandom(24)

# Bug -- hardcoded key
app.config["SECRET_KEY"] = "my-secret-key"

# Fix -- use environment variable
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
```

## Examples

```python
import os
from flask import Flask, session

app = Flask(__name__)

# Bug -- no secret key
# app.config["SECRET_KEY"] not set

# Fix -- set from environment
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")

@app.route("/set")
def set_value():
    session["key"] = "value"
    return "OK"
```
