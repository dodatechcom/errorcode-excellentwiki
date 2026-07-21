---
title: "[Solution] Django Aggregate Error Django"
description: "Aggregate not returning."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Aggregate not returning.

## Common Causes

Wrong usage.

## How to Fix

Use aggregate.

## Example

```python
from django.db.models import Avg, Sum
result = Product.objects.aggregate(avg_price=Avg('price'))
```
