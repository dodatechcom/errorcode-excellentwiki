---
title: "[Solution] Django Model Str Error"
description: "Model __str__ not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Model __str__ not working.

## Common Causes

Not defined.

## How to Fix

Define __str__.

## Example

```python
class User(models.Model):
    def __str__(self): return self.name
```
