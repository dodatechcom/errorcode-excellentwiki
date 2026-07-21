---
title: "[Solution] Django Static File Not Found Django"
description: "Static file 404."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Static file 404.

## Common Causes

Not in STATICFILES_DIRS.

## How to Fix

Add directory.

## Example

```python
STATICFILES_DIRS = [BASE_DIR / 'static']
```
