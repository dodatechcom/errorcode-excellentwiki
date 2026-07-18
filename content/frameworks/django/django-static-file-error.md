---
title: "[Solution] Django Static File Not Found Error — How to Fix"
description: "Fix Django static file not found errors. Resolve CSS, JS, and media file serving issues in Django."
frameworks: ["django"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django static file not found error occurs when Django cannot locate or serve static files like CSS, JavaScript, images, or media files. This is common in both development and production environments with different root causes.

## Why It Happens

Django separates static files from templates and media files. The error occurs when `STATICFILES_DIRS` is not configured, `STATIC_ROOT` is missing for collectstatic, `STATIC_URL` doesn't match the served path, files are placed in the wrong directory, or when the `staticfiles` app is not in `INSTALLED_APPS`.

## Common Error Messages

```
raise ValueError("Missing staticfiles' finders configuration")
```

```
404 Not Found: /static/css/style.css
```

```
ImproperlyConfigured: You're using the static files app but haven't configured STATIC_ROOT
```

```
IOError: [Errno 2] No such file or directory: '/app/staticfiles'
```

## How to Fix It

### 1. Configure Static Files Settings

Set all required static file settings in `settings.py`:

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# URL prefix for static files
STATIC_URL = '/static/'

# Directory where collectstatic will collect static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional directories containing static files (project-level)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Finders that know how to find static files
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
```

### 2. Use the Static Template Tag

Always reference static files through Django's template tag:

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <script src="{% static 'js/main.js' %}"></script>
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
</body>
</html>
```

### 3. Organize Static Files Properly

Use the correct directory structure:

```
myproject/
├── static/                    # Project-level static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.png
├── myapp/
│   └── static/
│       └── myapp/            # App-specific static files (namespaced)
│           ├── css/
│           │   └── app.css
│           └── js/
│               └── app.js
└── templates/
```

### 4. Collect and Serve Static Files

Run collectstatic for production and configure web server:

```bash
# Collect all static files
python manage.py collectstatic --noinput

# Verify static files are found
python manage.py findstatic css/style.css
```

```nginx
# Nginx configuration for serving static files
location /static/ {
    alias /app/staticfiles/;
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

```python
# For development testing with whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Common Scenarios

**Scenario 1: Static files work in development but not in production.**
In development, Django's `runserver` serves static files automatically via `staticfiles`. In production, you must either use `whitenoise` middleware or configure your web server (Nginx/Apache) to serve the `STATIC_ROOT` directory.

**Scenario 2: CSS and JS load with wrong MIME type.**
This happens when the web server doesn't set correct `Content-Type` headers. For Nginx, ensure `include mime.types` is in the config. For whitenoise, this is handled automatically.

**Scenario 3: Static files not found after app migration.**
When moving apps or renaming them, the `static/` directory inside the app may no longer be discovered. Update `STATICFILES_DIRS` or ensure the app name in the static path matches the new app name.

## Prevent It

1. **Develop with `whitenoise` or `django.contrib.staticfiles`.** Never rely on manual file copying for development — let Django's static file finders locate files automatically.

2. **Always namespace app static files.** Place app static files under `static/<app_name>/` to prevent conflicts between apps.

3. **Run `python manage.py collectstatic` before every deployment.** This ensures all static files are gathered in `STATIC_ROOT` for the web server to serve.
