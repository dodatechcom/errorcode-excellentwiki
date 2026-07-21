---
title: "[Solution] Django Q Expression Error Django"
description: "Q expression not filtering."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Q expression not filtering.

## Common Causes

Wrong syntax.

## How to Fix

Use Q.

## Example

```python
from django.db.models import Q
User.objects.filter(Q(name='J') | Q(email='j@e.com'))
```
