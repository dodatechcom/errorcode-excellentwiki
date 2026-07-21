---
title: "[Solution] Django URL Include Error"
description: "URL include not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

URL include not working.

## Common Causes

Wrong include.

## How to Fix

Use include.

## Example

```python
from django.urls import include, path
urlpatterns = [path('api/', include('api.urls'))]
```
