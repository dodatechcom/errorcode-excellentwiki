---
title: "[Solution] Flask Middleware Error"
description: "Fix Flask middleware errors when before/after request handlers fail or interfere with request processing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware errors occur when `before_request` or `after_request` handlers raise exceptions, modify responses incorrectly, or are not properly registered.

## Common Causes

- `before_request` handler raises an exception
- `after_request` handler modifies response incorrectly
- Middleware not registered on the correct blueprint
- Circular middleware calls
- Middleware order causes unexpected behavior

## How to Fix

### Register Middleware Correctly

```python
from flask import Flask, request, g
import time

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(g, "start_time"):
        elapsed = time.time() - g.start_time
        response.headers["X-Response-Time"] = f"{elapsed:.4f}s"
    return response
```

### Handle Middleware Errors

```python
@app.before_request
def check_auth():
    if request.endpoint in ("login", "static"):
        return None  # Skip auth for these routes
    if "user_id" not in session:
        return redirect(url_for("login"))
```

### Use Blueprint Middleware

```python
api_bp = Blueprint("api", __name__)

@api_bp.before_request
def api_before_request():
    # API-specific middleware
    pass

@api_bp.after_request
def api_after_request(response):
    response.headers["X-API-Version"] = "1.0"
    return response
```

## Examples

```python
from flask import Flask, request

app = Flask(__name__)

# Bug -- middleware raises exception
@app.before_request
def broken_middleware():
    raise ValueError("Error")  # Breaks all requests

# Fix -- handle errors gracefully
@app.before_request
def safe_middleware():
    try:
        # Do something
        pass
    except Exception:
        pass  # Don't break the request
```
