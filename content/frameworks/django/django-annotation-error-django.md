---
title: "[Solution] Django Annotation Error Django"
description: "Annotation not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Annotation not working.

## Common Causes

Wrong usage.

## How to Fix

Use annotate.

## Example

```python
from django.db.models import Count
Post.objects.annotate(comment_count=Count('comments'))
```
