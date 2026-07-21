---
title: "[Solution] Django Admin Search Fields Error"
description: "Admin search not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin search not working.

## Common Causes

Not configured.

## How to Fix

Add search_fields.

## Example

```python
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
```
