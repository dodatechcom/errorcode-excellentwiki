---
title: "[Solution] Flask Static Files Error"
description: "Fix Flask static files errors when serving static CSS, JavaScript, or image files fails."
frameworks: ["flask"]
error-types: ["deployment-error"]
severities: ["error"]
---

Static file errors occur when Flask cannot serve static assets due to incorrect folder configuration or missing files.

## Common Causes

- Static folder does not exist
- Static folder path is incorrect
- File permissions prevent reading
- Blueprint static folder not configured
- Static URL path conflicts with routes

## How to Fix

### Configure Static Folder

```python
from flask import Flask

app = Flask(
    __name__,
    static_folder="assets",
    static_url_path="/assets",
)
```

### Serve Static Files in Templates

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/app.js') }}"></script>
```

### Use Blueprint Static Files

```python
from flask import Blueprint

admin_bp = Blueprint(
    "admin",
    __name__,
    static_folder="admin/static",
    static_url_path="/admin/static",
)
```

### Handle Static File Errors

```python
from flask import send_from_directory
from werkzeug.exceptions import NotFound

@app.route("/files/<path:filename>")
def serve_file(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except NotFound:
        return {"error": "File not found"}, 404
```

## Examples

```python
from flask import Flask

app = Flask(__name__)

# Bug -- static folder does not exist
app = Flask(__name__, static_folder="nonexistent")

# Fix -- use existing folder
app = Flask(__name__, static_folder="static")
```
