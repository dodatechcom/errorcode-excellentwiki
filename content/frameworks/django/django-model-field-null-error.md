---
title: "[Solution] Django Model Field Null Error"
description: "Field null not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Field null not working.

## Common Causes

Wrong null setting.

## How to Fix

Set null.

## Example

```python
class User(models.Model):
    bio = models.TextField(null=True, blank=True)
```
