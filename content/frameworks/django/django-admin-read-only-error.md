---
title: "[Solution] Django Admin Read Only Error"
description: "Read-only fields not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Read-only fields not working.

## Common Causes

Not configured.

## How to Fix

Add readonly_fields.

## Example

```python
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
```
