---
title: "[Solution] Python ImportError: No module named 'django' — Fix"
description: "Fix Python ImportError: No module named 'django'. Install Django with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 317
---

# Python ImportError: No module named 'django'

Django is a high-level Python web framework that is not part of the standard library. This error occurs when Python cannot find the `django` package in your environment.

## Common Causes

```python
# Cause 1: Django not installed
import django  # ImportError: No module named 'django'

# Cause 2: Wrong Python version or virtual environment activated
import django  # ImportError when using system Python instead of venv

# Cause 3: Django installed in a different environment
# pip install django ran under Python 3.11 but you run with Python 3.12

# Cause 4: Package name confusion
import Django  # ImportError — Python is case-sensitive

# Cause 5: requirements.txt not synced
# requirements.txt lists django==4.2 but pip install was never run
```

## How to Fix

### Fix 1: Install Django with pip

```bash
pip install django

# For a specific version
pip install django==4.2.11

# With extras
pip install django[argon2]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install django
python -c "import django; print(django.get_version())"
```

### Fix 3: Sync from requirements.txt

```bash
pip install -r requirements.txt
```

## Examples

```python
# Verify Django is available
import django
print(django.VERSION)

# Start a new project after install
# django-admin startproject myproject
```

## Related Errors

- {{< relref "importerror-django-rest-framework" >}} — ImportError: djangorestframework
- {{< relref "importerror-django2" >}} — ImportError: django (variant)
- {{< relref "importerror-celery" >}} — ImportError: celery
