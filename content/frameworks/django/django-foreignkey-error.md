---
title: "[Solution] Django ForeignKey Error"
description: "ForeignKey not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

ForeignKey not working.

## Common Causes

Wrong definition.

## How to Fix

Define correctly.

## Example

```python
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```
