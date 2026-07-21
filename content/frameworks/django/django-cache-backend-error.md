---
title: "[Solution] Django Cache Backend Error"
description: "Cache backend not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Cache backend not working.

## Common Causes

Not configured.

## How to Fix

Configure backend.

## Example

```python
CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
```
