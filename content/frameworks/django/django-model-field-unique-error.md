---
title: "[Solution] Django Model Field Unique Error"
description: "Field unique not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Field unique not working.

## Common Causes

Not unique.

## How to Fix

Set unique.

## Example

```python
class User(models.Model):
    email = models.EmailField(unique=True)
```
