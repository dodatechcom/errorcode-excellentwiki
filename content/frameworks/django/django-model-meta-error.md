---
title: "[Solution] Django Model Meta Error"
description: "Model meta not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Model meta not working.

## Common Causes

Wrong meta class.

## How to Fix

Define Meta.

## Example

```python
class User(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
```
