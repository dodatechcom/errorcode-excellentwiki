---
title: "[Solution] Django Select Related Deep Error"
description: "select_related deep."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

select_related deep.

## Common Causes

Wrong depth.

## How to Fix

Use prefetch_related for deep.

## Example

```python
Post.objects.select_related('author__profile')
```
