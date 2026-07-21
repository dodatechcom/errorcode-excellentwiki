---
title: "[Solution] Django Admin Form Error"
description: "Admin form not rendering."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin form not rendering.

## Common Causes

Wrong form class.

## How to Fix

Define form.

## Example

```python
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
```
