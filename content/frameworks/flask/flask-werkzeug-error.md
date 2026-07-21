---
title: "[Solution] Flask Werkzeug Error"
description: "Fix Flask Werkzeug errors when the WSGI utility library raises unexpected exceptions."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Werkzeug errors occur when the underlying WSGI toolkit encounters invalid requests, encoding issues, or configuration problems.

## Common Causes

- Invalid URL encoding in request path
- Malformed HTTP headers
- Request body exceeds size limits
- Invalid Content-Type header
- URL routing rules conflict

## How to Fix

### Handle URL Encoding Issues

```python
from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400
```

### Set Request Size Limits

```python
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB
```

### Handle Encoding Errors

```python
@app.route("/upload", methods=["POST"])
def upload():
    try:
        data = request.get_data(as_text=True)
        return {"received": len(data)}
    except UnicodeDecodeError:
        return {"error": "Invalid encoding"}, 400
```

## Examples

```python
from flask import Flask

app = Flask(__name__)

# Bug -- no size limit
# Large uploads may crash the server

# Fix -- set size limit
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

@app.route("/upload", methods=["POST"])
def upload():
    return {"status": "ok"}
```
