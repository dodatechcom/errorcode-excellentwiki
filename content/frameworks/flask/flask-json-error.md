---
title: "[Solution] Flask JSON Error"
description: "Fix Flask JSON parsing errors when request.get_json() fails or returns None unexpectedly."
frameworks: ["flask"]
error-types: ["validation-error"]
severities: ["error"]
---

JSON parsing errors occur when `request.get_json()` fails because the request body is not valid JSON or the Content-Type header is incorrect.

## Common Causes

- Content-Type header not set to application/json
- Request body is not valid JSON
- `request.get_json()` called with `force=True` on malformed data
- Request body is empty
- JSON decoder error in malformed payload

## How to Fix

### Check Content Type First

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/data", methods=["POST"])
def api_data():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    return jsonify({"received": data})
```

### Handle JSON Parse Errors

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/api/data", methods=["POST"])
def api_data():
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data})
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 400
```

### Set Default Values

```python
@app.route("/api/data", methods=["POST"])
def api_data():
    data = request.get_json(silent=True)  # Returns None instead of raising
    if data is None:
        data = {}
    return jsonify({"received": data})
```

## Examples

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Bug -- not checking for None
@app.route("/data", methods=["POST"])
def data():
    info = request.get_json()  # May be None
    return jsonify(info["key"])  # TypeError if None

# Fix -- check for None
@app.route("/data-fixed", methods=["POST"])
def data_fixed():
    info = request.get_json()
    if info is None:
        return jsonify({"error": "Invalid JSON"}), 400
    return jsonify(info.get("key"))
```
