---
title: "[Solution] Django Model Field Auto Now Error"
description: "auto_now not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

auto_now not working.

## Common Causes

Wrong usage.

## How to Fix

Use auto_now_add.

## Example

```python
class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
