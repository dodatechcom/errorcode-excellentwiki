---
title: "[Solution] Django REST Router Error"
description: "Router not generating URLs."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Router not generating URLs.

## Common Causes

Not registered.

## How to Fix

Register ViewSet.

## Example

```python
from rest_framework.routers import DefaultRouter
r = DefaultRouter()
r.register('users', UV)
urlpatterns = r.urls
```
