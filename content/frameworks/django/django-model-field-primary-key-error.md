---
title: "[Solution] Django Model Field Primary Key Error"
description: "Primary key not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Primary key not working.

## Common Causes

Wrong pk.

## How to Fix

Set primary_key.

## Example

```python
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
```
