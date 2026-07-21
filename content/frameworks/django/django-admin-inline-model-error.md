---
title: "[Solution] Django Admin Inline Model Error"
description: "Inline model not showing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Inline model not showing.

## Common Causes

Not configured.

## How to Fix

Register inline.

## Example

```python
class PostInline(admin.TabularInline):
    model = Post
    extra = 1
```
