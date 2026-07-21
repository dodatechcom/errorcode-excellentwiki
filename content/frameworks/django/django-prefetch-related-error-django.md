---
title: "[Solution] Django Prefetch Related Error Django"
description: "prefetch_related wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

prefetch_related wrong.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
Post.objects.prefetch_related('comments', 'tags').all()
```
