---
title: "[Solution] Django First Error"
description: "first() returning None."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

first() returning None.

## Common Causes

No matching objects.

## How to Fix

Check query.

## Example

```python
u = User.objects.filter(name='John').first()
```
