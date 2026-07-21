---
title: "[Solution] Django Model Field Blank Error"
description: "Field blank not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Field blank not working.

## Common Causes

Wrong blank setting.

## How to Fix

Set blank.

## Example

```python
class User(models.Model):
    bio = models.TextField(blank=True)
```
