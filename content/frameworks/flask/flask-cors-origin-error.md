---
title: "[Solution] Flask CORS Origin Error"
description: "Fix Flask CORS origin errors when specific origins are not properly configured for cross-origin requests."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
---

CORS origin errors occur when the allowed origins list does not include the requesting origin, or when wildcard origins are used with credentials.

## Common Causes

- Requesting origin not in allowed origins list
- Using `*` with `supports_credentials=True`
- Origin header not sent by the client
- Dynamic origins not handled correctly
- Preflight response missing origin header

## How to Fix

### Configure Specific Origins

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://myapp.com", "https://admin.myapp.com"],
        "supports_credentials": True,
    }
})
```

### Handle Dynamic Origins

```python
from flask_cors import CORS

def allowed_origins():
    return ["https://myapp.com", "https://staging.myapp.com"]

CORS(app, resources={r"/api/*": {"origins": allowed_origins}})
```

### Use Environment Variables

```python
import os

ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "").split(",")

CORS(app, resources={
    r"/api/*": {
        "origins": ALLOWED_ORIGINS,
        "supports_credentials": True,
    }
})
```

## Examples

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Bug -- wildcard with credentials
CORS(app, resources={r"/api/*": {"origins": "*", "supports_credentials": True}})

# Fix -- use specific origins
CORS(app, resources={r"/api/*": {"origins": ["https://myapp.com"]}})
```
