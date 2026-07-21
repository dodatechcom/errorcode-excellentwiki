---
title: "[Solution] Django Exists Error"
description: "exists() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

exists() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on queryset.

## Example

```python
if User.objects.filter(email=e).exists(): pass
```
