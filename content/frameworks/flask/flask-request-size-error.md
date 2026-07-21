---
title: "[Solution] Flask Request Size Error"
description: "Fix Flask request size errors when large uploads or request bodies exceed configured limits."
frameworks: ["flask"]
error-types: ["validation-error"]
severities: ["error"]
---

Request size errors occur when the incoming request body exceeds Flask's configured maximum content length.

## Common Causes

- `MAX_CONTENT_LENGTH` set too low
- Large file upload without streaming
- No size limit allows denial of service attacks
- Multipart form data larger than expected
- JSON request body too large

## How to Fix

### Configure Maximum Content Length

```python
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB
```

### Stream Large Uploads

```python
from flask import Flask, request
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100MB

@app.route("/upload", methods=["POST"])
def upload():
    chunk_size = 8192
    total_size = 0
    with open("upload.bin", "wb") as f:
        while True:
            chunk = request.stream.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            total_size += len(chunk)
    return {"size": total_size}
```

### Handle 413 Error

```python
from werkzeug.exceptions import RequestEntityTooLarge

@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large"}), 413
```

## Examples

```python
from flask import Flask

app = Flask(__name__)

# Bug -- no size limit
# app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

@app.route("/upload", methods=["POST"])
def upload():
    return {"status": "ok"}  # Accepts any size!

# Fix -- set limit
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
```
