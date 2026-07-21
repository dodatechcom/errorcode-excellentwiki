---
title: "[Solution] Django prefetch_related Error"
description: "N+1 queries."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

N+1 queries.

## Common Causes

Not using prefetch_related.

## How to Fix

Add it.

## Example

```python
Post.objects.prefetch_related('tags').all()
```
