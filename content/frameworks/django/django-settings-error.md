---
title: "[Solution] Django ImproperlyConfigured — setting error"
description: "Fix Django ImproperlyConfigured errors. Resolve settings configuration issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["settings", "improperlyconfigured", "configuration", "setup", "django"]
weight: 5
---

An ImproperlyConfigured error means Django cannot start because a required setting is missing, invalid, or misconfigured. This is raised during application startup.

## Common Causes

- Missing required settings (SECRET_KEY, DATABASES, etc.)
- Setting value has wrong type or format
- Required third-party package not installed
- Environment variable not set
- Circular import in settings module

## How to Fix

### Check Error Message

```bash
python manage.py runserver
# ImproperlyConfigured: The SECRET_KEY setting must not be empty.
```

### Verify Required Settings

```python
# Minimum required settings
SECRET_KEY = 'your-secret-key'
DEBUG = True
INSTALLED_APPS = ['django.contrib.contenttypes']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Use Environment Variables

```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key')
```

### Check Installed Apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # your apps
]
```

## Examples

```python
# Example 1: Missing SECRET_KEY
# ImproperlyConfigured: Set the SECRET_KEY setting
# Fix: add SECRET_KEY to settings.py or environment

# Example 2: Wrong database engine
# ImproperlyConfigured: Database engine not found
# Fix: use 'django.db.backends.postgresql' not 'postgres'
```

## Related Errors

- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — settings issues
- [Django WSGI Error]({{< relref "/frameworks/django/django-wsgi-error" >}}) — WSGI configuration error
