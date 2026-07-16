---
title: "ImproperlyConfigured: setting X is not set"
description: "Django raises ImproperlyConfigured when a required setting is missing or misconfigured"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["settings", "configuration", "improperly-configured"]
weight: 5
---

This error occurs when Django encounters a required configuration setting that is missing, has an invalid value, or cannot be resolved during startup.

## Common Causes

- Missing environment variable that a setting depends on
- Required package not installed (e.g. `dj-database-url`)
- Wrong `INSTALLED_APPS` configuration
- Misconfigured database URL or secret key

## How to Fix

1. Use a defaults function or `os.environ.get` with fallbacks:

```python
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key-change-in-production")
```

2. Verify all required packages are installed:

```bash
pip install -r requirements.txt
```

3. Check `INSTALLED_APPS` includes all necessary apps:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # your apps here
]
```

4. Load settings from environment in production:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
```

## Examples

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],  # KeyError if not set
    }
}
```

```text
django.core.exceptions.ImproperlyConfigured: Set the DB_ENGINE environment variable
```

## Related Errors

- [TemplateSyntaxError: Invalid block tag]({{< relref "/frameworks/django/template-error" >}})
