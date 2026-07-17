---
title: "[Solution] Python ImportError: django not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: django not found or ModuleNotFoundError: No module named 'django'. Install Django properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: django not found — ModuleNotFoundError Fix

An `ImportError: django not found` or `ModuleNotFoundError: No module named 'django'` means Python cannot locate the Django package.

## What This Error Means

Django is a high-level web framework. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: Django not installed
import django  # ModuleNotFoundError: No module named 'django'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install django

# For a specific version
pip install django==4.2.8
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install django
python -c "import django; print(django.get_version())"
```

## Related Errors

- {{< relref "importerror-celery" >}} — ImportError: celery
- {{< relref "importerror-django2" >}} — ImportError: django
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
