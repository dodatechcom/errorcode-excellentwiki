---
title: "[Solution] Flask Deploy Error"
description: "Fix Flask deployment errors when the application fails to start or behave correctly in production."
frameworks: ["flask"]
error-types: ["deployment-error"]
severities: ["error"]
---

Deployment errors occur when the Flask application is not properly configured for the production environment.

## Common Causes

- Debug mode enabled in production
- Development server used instead of WSGI server
- Static files not served efficiently
- Database connection pool not configured
- Logging not properly configured

## How to Fix

### Use Production WSGI Server

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn --bind 0.0.0.0:8000 --workers 4 app:app
```

### Configure for Production

```python
import os
from flask import Flask

app = Flask(__name__)

# Production settings
app.config["DEBUG"] = False
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_POOL_SIZE"] = 10
```

### Serve Static Files Efficiently

```python
from flask import Flask, send_from_directory

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)
```

## Examples

```python
import os
from flask import Flask

app = Flask(__name__)

# Bug -- using development server in production
app.run(debug=True)  # Never do this in production!

# Fix -- use gunicorn
# gunicorn --bind 0.0.0.0:8000 app:app
```
