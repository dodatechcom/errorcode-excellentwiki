---
title: "[Solution] Django Model Field Default Error"
description: "Field default not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Field default not working.

## Common Causes

Wrong default.

## How to Fix

Set default.

## Example

```python
class User(models.Model):
    is_active = models.BooleanField(default=True)
```
