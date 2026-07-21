---
title: "[Solution] Django F Expression Update Error"
description: "F expression update failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

F expression update failing.

## Common Causes

Wrong usage.

## How to Fix

Use F for field.

## Example

```python
from django.db.models import F
Product.objects.update(price=F('price') * 1.1)
```
