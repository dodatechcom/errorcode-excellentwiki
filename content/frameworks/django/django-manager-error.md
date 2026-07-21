---
title: "[Solution] Django Manager Error"
description: "Manager not defined."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Manager not defined.

## Common Causes

Wrong usage.

## How to Fix

Define manager.

## Example

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
```
