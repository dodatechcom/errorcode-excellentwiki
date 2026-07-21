---
title: "[Solution] Django REST Ordering Error"
description: "Ordering not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Ordering not working.

## Common Causes

Not configured.

## How to Fix

Configure ordering.

## Example

```python
class V(viewSets.ModelViewSet):
    ordering_fields = ['created_at']
```
