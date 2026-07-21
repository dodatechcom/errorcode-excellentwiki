---
title: "[Solution] Django get_object_or_404 Error"
description: "Object not found."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Object not found.

## Common Causes

Wrong query.

## How to Fix

Check parameters.

## Example

```python
from django.shortcuts import get_object_or_404
u = get_object_or_404(User, pk=user_id)
```
