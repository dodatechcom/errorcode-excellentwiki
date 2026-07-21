---
title: "[Solution] Django Model Field Choices Error"
description: "Field choices not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Field choices not working.

## Common Causes

Wrong format.

## How to Fix

Use tuple.

## Example

```python
class User(models.Model):
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')])
```
