---
title: "[Solution] Django Delete Error"
description: "delete() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

delete() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on queryset.

## Example

```python
User.objects.filter(is_active=False).delete()
```
