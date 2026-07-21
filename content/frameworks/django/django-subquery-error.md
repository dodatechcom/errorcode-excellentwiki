---
title: "[Solution] Django Subquery Error"
description: "Subquery not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Subquery not working.

## Common Causes

Wrong usage.

## How to Fix

Use Subquery.

## Example

```python
from django.db.models import Subquery
User.objects.annotate(last_post=Subquery(Post.objects.filter(author=OuterRef('pk')).values('title')[:1]))
```
