---
title: "[Solution] Django Admin Register Error"
description: "Model not in admin."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Model not in admin.

## Common Causes

Not registered.

## How to Fix

Register.

## Example

```python
from django.contrib import admin
admin.site.register(User)
```
