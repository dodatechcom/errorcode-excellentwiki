---
title: "[Solution] Django WSGI Configuration Error"
description: "Fix Django WSGI configuration errors. Resolve WSGI deployment issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["wsgi", "gunicorn", "deployment", "server", "django"]
weight: 5
---

A Django WSGI error occurs when the WSGI server cannot start or serve the Django application. This is common during deployment with Gunicorn, uWSGI, or Apache.

## Common Causes

- wsgi.py file is missing or misconfigured
- Python path not set correctly
- WSGI application module not found
- Virtual environment not activated
- Django settings module not configured

## How to Fix

### Check wsgi.py

```python
# myproject/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()
```

### Set Environment Variable

```bash
export DJANGO_SETTINGS_MODULE=myproject.settings
```

### Test with Gunicorn

```bash
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

### Check Python Path

```bash
cd /path/to/project
gunicorn myproject.wsgi:application
```

### Verify Django Settings

```bash
python -c "import django; django.setup(); print('OK')"
```

## Examples

```bash
# Example 1: Module not found
gunicorn myproject.wsgi:application
# ModuleNotFoundError: No module named 'myproject'
# Fix: cd to project directory first

# Example 2: Settings not configured
# ImproperlyConfigured: Set the SECRET_KEY setting
# Fix: export DJANGO_SETTINGS_MODULE=myproject.settings
```

## Related Errors

- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — ImproperlyConfigured
- [Django Static File]({{< relref "/frameworks/django/django-static-file" >}}) — static file not found
