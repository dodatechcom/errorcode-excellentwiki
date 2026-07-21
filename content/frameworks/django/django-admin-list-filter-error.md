---
title: "[Solution] Django Admin List Filter Error"
description: "Admin list filter not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin list filter not working.

## Common Causes

Not configured.

## How to Fix

Add list_filter.

## Example

```python
class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_active', 'role']
```
