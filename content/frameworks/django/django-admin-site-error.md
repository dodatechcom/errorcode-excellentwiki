---
title: "[Solution] Django Admin Site Error"
description: "Admin site not showing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin site not showing.

## Common Causes

Not registered.

## How to Fix

Register models.

## Example

```python
from django.contrib import admin
admin.site.register(User)
```
