---
title: "[Solution] Django Last Error"
description: "last() returning None."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

last() returning None.

## Common Causes

No matching objects.

## How to Fix

Check query.

## Example

```python
u = User.objects.filter(name='John').last()
```
