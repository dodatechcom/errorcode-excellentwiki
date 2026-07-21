---
title: "[Solution] Django select_related Error"
description: "N+1 queries."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

N+1 queries.

## Common Causes

Not using select_related.

## How to Fix

Add it.

## Example

```python
Post.objects.select_related('author').all()
```
