---
title: "[Solution] Django F Expression Error"
description: "F expression wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

F expression wrong.

## Common Causes

Wrong usage.

## How to Fix

Use for fields.

## Example

```python
from django.db.models import F
Product.objects.update(price=F('price') * 1.1)
```
