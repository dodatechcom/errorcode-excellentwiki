---
title: "[Solution] Django Admin Inline Error"
description: "Inline admin not showing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Inline admin not showing.

## Common Causes

Not registered.

## How to Fix

Register inline.

## Example

```python
class PostInline(admin.TabularInline):
    model = Post
admin.site.register(User, UserAdmin)
```
