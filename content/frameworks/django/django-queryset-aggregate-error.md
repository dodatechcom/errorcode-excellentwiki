---
title: "[Solution] Django QuerySet Aggregate Error"
description: "Aggregate not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Aggregate not working.

## Common Causes

Wrong function.

## How to Fix

Use aggregate.

## Example

```python
from django.db.models import Count
result = User.objects.aggregate(count=Count('id'))
```
