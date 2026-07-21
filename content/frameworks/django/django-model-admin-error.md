---
title: "[Solution] Django Model Admin Error"
description: "ModelAdmin not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

ModelAdmin not working.

## Common Causes

Wrong configuration.

## How to Fix

Configure correctly.

## Example

```python
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['is_active']
admin.site.register(User, UserAdmin)
```
