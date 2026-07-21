---
title: "[Solution] Flask CORS Methods Error"
description: "Fix Flask CORS methods errors when specific HTTP methods are not allowed in cross-origin requests."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
---

CORS methods errors occur when the `Access-Control-Allow-Methods` header does not include the HTTP method used by the client.

## Common Causes

- OPTIONS preflight not handled
- Custom methods not included in allowed list
- PATCH or DELETE methods not allowed
- Method list too restrictive for API needs
- Preflight response missing methods header

## How to Fix

### Allow All Common Methods

```python
from flask_cors import CORS

CORS(app, resources={
    r"/api/*": {
        "origins": ["https://myapp.com"],
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
    }
})
```

### Handle OPTIONS Explicitly

```python
@app.after_request
def after_request(response):
    if request.method == "OPTIONS":
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Max-Age"] = "3600"
    return response
```

### Configure Per-Route CORS

```python
from flask_cors import cross_origin

@app.route("/api/data", methods=["GET", "POST"])
@cross_origin(methods=["GET", "POST"])
def api_data():
    return {"data": "value"}
```

## Examples

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Bug -- only GET allowed
CORS(app, resources={r"/api/*": {"methods": ["GET"]}})

@app.route("/api/data", methods=["POST"])
def api_data():
    return {"status": "ok"}  # CORS blocks POST

# Fix -- allow POST
CORS(app, resources={r"/api/*": {"methods": ["GET", "POST"]}})
```
