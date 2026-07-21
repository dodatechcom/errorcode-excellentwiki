---
title: "[Solution] Django Cache Framework Error"
description: "Cache not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Cache not working.

## Common Causes

Not configured.

## How to Fix

Configure backend.

## Example

```python
CACHES = {'default': {'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache', 'LOCATION': '127.0.0.1:11211'}}
```
