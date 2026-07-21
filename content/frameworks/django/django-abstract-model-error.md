---
title: "[Solution] Django Abstract Model Error"
description: "Abstract model not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Abstract model not working.

## Common Causes

Not abstract.

## How to Fix

Set abstract.

## Example

```python
class BaseModel(models.Model):
    class Meta:
        abstract = True
```
