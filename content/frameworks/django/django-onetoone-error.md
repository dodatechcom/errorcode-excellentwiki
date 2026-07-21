---
title: "[Solution] Django OneToOne Error"
description: "OneToOne not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

OneToOne not working.

## Common Causes

Wrong definition.

## How to Fix

Define correctly.

## Example

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```
