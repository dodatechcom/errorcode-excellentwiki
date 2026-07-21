---
title: "[Solution] Django Prefetch Related Object Error"
description: "PrefetchRelatedObjectDoesNotExist."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

PrefetchRelatedObjectDoesNotExist.

## Common Causes

Prefetch not configured.

## How to Fix

Add prefetch_related.

## Example

```python
Post.objects.prefetch_related('comments').all()
```
