---
title: "[Solution] Django Exists Subquery Error"
description: "Exists subquery not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Exists subquery not working.

## Common Causes

Wrong usage.

## How to Fix

Use Exists.

## Example

```python
from django.db.models import Exists
User.objects.annotate(has_posts=Exists(Post.objects.filter(author=OuterRef('pk'))))
```
