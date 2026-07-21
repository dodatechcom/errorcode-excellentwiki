---
title: "[Solution] Django Admin Action Error"
description: "Admin action not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin action not working.

## Common Causes

Not registered.

## How to Fix

Define action.

## Example

```python
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
```
