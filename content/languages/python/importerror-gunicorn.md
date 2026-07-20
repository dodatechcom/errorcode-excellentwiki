---
title: "[Solution] Python ImportError: No module named 'gunicorn' — Fix"
description: "Fix Python ImportError: No module named 'gunicorn'. Install gunicorn with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 314
---

# Python ImportError: No module named 'gunicorn'

The `ModuleNotFoundError: No module named 'gunicorn'` error occurs when Python cannot locate the gunicorn package, which is a pre-fork WSGI HTTP server for serving Python web applications in production.

## Common Causes

```python
# Cause 1: gunicorn not installed
# Running: gunicorn myapp:app
# ModuleNotFoundError: No module named 'gunicorn'

# Cause 2: Installed for wrong Python version or virtual environment
import gunicorn  # ModuleNotFoundError

# Cause 3: Using in Docker but gunicorn only in dev requirements
# production Dockerfile missing gunicorn
```

```python
# Cause 4: gunicorn not compatible with Windows
# gunicorn only works on Unix-based systems

# Cause 5: Pre-installed WSGI server missing
# some PaaS platforms do not include gunicorn by default
```

## How to Fix

### Fix 1: Install gunicorn with pip

```bash
pip install gunicorn

# With eventlet worker
pip install gunicorn[eventlet]

# With gevent worker
pip install gunicorn[gevent]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install gunicorn
gunicorn --version
```

### Fix 3: Add to production requirements

```bash
# requirements-prod.txt
gunicorn

# Dockerfile
RUN pip install -r requirements-prod.txt
CMD ["gunicorn", "myapp:app", "--bind", "0.0.0.0:8000"]
```

## Examples

```bash
# Basic usage
gunicorn myapp:app

# With workers and bind
gunicorn myapp:app --workers 4 --bind 0.0.0.0:8000

# With access log
gunicorn myapp:app --access-logfile - --error-logfile -

# With timeout
gunicorn myapp:app --timeout 120
```

```python
# gunicorn.conf.py — configuration file
bind = "0.0.0.0:8000"
workers = 4
timeout = 120
accesslog = "-"
errorlog = "-"
loglevel = "info"
```

## Related Errors

- {{< relref "importerror-uvicorn" >}} — ImportError: uvicorn
- {{< relref "importerror-flask2" >}} — ImportError: flask
- {{< relref "importerror-starlette" >}} — ImportError: starlette
