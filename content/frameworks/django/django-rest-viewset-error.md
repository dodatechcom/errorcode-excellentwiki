---
title: "[Solution] Django REST ViewSet Error"
description: "ViewSet not routing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

ViewSet not routing.

## Common Causes

Not registered.

## How to Fix

Register with router.

## Example

```python
from rest_framework import viewsets
class UV(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = US
```
