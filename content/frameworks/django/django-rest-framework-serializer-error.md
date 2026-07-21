---
title: "[Solution] Django REST Framework Serializer Error"
description: "Serializer failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Serializer failing.

## Common Causes

Wrong definition.

## How to Fix

Define correctly.

## Example

```python
from rest_framework import serializers
class US(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']
```
