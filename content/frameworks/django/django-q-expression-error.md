---
title: "[Solution] Django Q Expression Error"
description: "Q expression wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Q expression wrong.

## Common Causes

Wrong syntax.

## How to Fix

Use Q objects.

## Example

```python
from django.db.models import Q
User.objects.filter(Q(name='J') | Q(email='j@e.com'))
```
