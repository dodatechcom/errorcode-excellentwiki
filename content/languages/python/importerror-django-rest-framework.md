---
title: "[Solution] Python ImportError: No module named 'rest_framework' — Fix"
description: "Fix Python ImportError: No module named 'rest_framework'. Install djangorestframework with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 310
---

# Python ImportError: No module named 'rest_framework'

The `ModuleNotFoundError: No module named 'rest_framework'` error occurs when Python cannot locate the Django REST Framework package, which provides a toolkit for building Web APIs in Django.

## Common Causes

```python
# Cause 1: djangorestframework not installed
from rest_framework import serializers  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version or virtual environment
import rest_framework  # ModuleNotFoundError

# Cause 3: Package name vs import name mismatch
# pip install djangorestframework → import rest_framework
```

```python
# Cause 4: Django installed but DRF missing
# pip install django does not include djangorestframework

# Cause 5: Missing from INSTALLED_APPS
# rest_framework must be in Django settings INSTALLED_APPS
```

## How to Fix

### Fix 1: Install djangorestframework with pip

```bash
pip install djangorestframework

# Verify installation
python -c "import rest_framework; print(rest_framework.VERSION)"
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install djangorestframework
python -c "from rest_framework import serializers; print('OK')"
```

### Fix 3: Add to INSTALLED_APPS in settings.py

```python
# settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    # ...
    "rest_framework",
]
```

## Examples

```python
# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
```

```python
# views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

## Related Errors

- {{< relref "importerror-django2" >}} — ImportError: django
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
