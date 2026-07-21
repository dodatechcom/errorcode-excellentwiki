---
title: "[Solution] Flask Request Context Push Error"
description: "Fix Flask request context push errors when accessing request objects outside of request handlers."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Accessing `request`, `g`, or `session` outside of a request handler causes a `RuntimeError` because no request context is available.

## Common Causes

- Accessing `request` in a background thread
- Using `request` in Celery tasks without pushing context
- Calling route functions directly from other modules
- Accessing `request` in application startup code
- Using `request` in database event listeners

## How to Fix

### Push Request Context Manually

```python
from flask import Flask, request

app = Flask(__name__)

with app.app_context():
    with app.test_request_context("/api/data"):
        print(request.path)  # Works
```

### Use Application Context Instead

```python
from flask import Flask, g

app = Flask(__name__)

def get_current_user_id():
    try:
        return g.get("user_id")
    except RuntimeError:
        return None  # Outside request context
```

### Pass Data Through Function Parameters

```python
# Instead of accessing request directly
def process_data(request_path):
    print(f"Processing {request_path}")

@app.route("/api/data")
def api_data():
    process_data(request.path)
    return {"status": "ok"}
```

## Examples

```python
from flask import Flask, request

app = Flask(__name__)

# Bug -- accessing request outside handler
def background_job():
    print(request.method)  # RuntimeError

@app.route("/api")
def api():
    background_job()  # Fails when called
    return {"status": "ok"}

# Fix -- push context
with app.app_context():
    with app.test_request_context("/api"):
        background_job()  # Works
```
