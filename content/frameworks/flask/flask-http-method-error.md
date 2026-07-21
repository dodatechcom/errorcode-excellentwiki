---
title: "[Solution] Flask HTTP Method Error"
description: "Fix Flask HTTP method errors when routes do not handle the correct request methods."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

HTTP method errors occur when routes do not support the requested method or when method handling is incorrect.

## Common Causes

- Route only supports GET but POST is sent
- Missing methods parameter in route decorator
- OPTIONS method not handled for CORS
- PUT/PATCH used interchangeably
- DELETE method not implemented

## How to Fix

### Support Multiple Methods

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        # Create user
        return {"created": True}, 201
    # List users
    return {"users": []}
```

### Handle OPTIONS for CORS

```python
@app.after_request
def add_cors_headers(response):
    if request.method == "OPTIONS":
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response
```

### Use Correct Methods

```python
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    return {"item_id": item_id}

@app.route("/items", methods=["POST"])
def create_item():
    return {"created": True}, 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    return {"updated": item_id}

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    return "", 204
```

## Examples

```python
from flask import Flask, request

app = Flask(__name__)

# Bug -- only GET supported
@app.route("/data")
def data():
    return {"data": "value"}

# Sending POST returns 405 Method Not Allowed

# Fix -- support POST
@app.route("/data-fixed", methods=["GET", "POST"])
def data_fixed():
    if request.method == "POST":
        return {"received": request.json}
    return {"data": "value"}
```
