---
title: "[Solution] Django Model Delete Error"
description: "delete() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

delete() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on instance.

## Example

```python
user.delete()
# or
User.objects.filter(is_active=False).delete()
```
