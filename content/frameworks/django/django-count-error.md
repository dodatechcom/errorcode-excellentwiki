---
title: "[Solution] Django Count Error"
description: "count() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

count() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on queryset.

## Example

```python
c = User.objects.filter(active=True).count()
```
