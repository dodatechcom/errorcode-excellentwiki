---
title: "[Solution] Django Static File Not Found Error"
description: "Fix Django static file not found errors. Resolve static file serving issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["static", "files", "collectstatic", "css", "django"]
weight: 5
---

A Django static file not found error occurs when the application cannot locate or serve static files like CSS, JavaScript, or images.

## Common Causes

- `STATIC_URL` is not configured in settings.py
- `collectstatic` has not been run
- `STATICFILES_DIRS` does not include the correct path
- Template not using `{% static %}` tag
- WhiteNoise or other middleware not configured

## How to Fix

### Check Static Settings

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### Run collectstatic

```bash
python manage.py collectstatic
```

### Use Static Tag in Templates

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### Configure WhiteNoise (production)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Check Static Files Discovery

```bash
python manage.py findstatic css/style.css
```

## Examples

```bash
# Example 1: collectstatic not run
# GET /static/css/style.css -> 404
# Fix: python manage.py collectstatic

# Example 2: Missing static tag
<!-- Wrong -->
<link rel="stylesheet" href="/static/css/style.css">
<!-- Fix -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

## Related Errors

- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — ImproperlyConfigured
- [Django Template Error]({{< relref "/frameworks/django/django-template-error" >}}) — template rendering error
