---
title: "[Solution] Flask Flask-Caching Error"
description: "Cache not storing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Cache not storing.

## Common Causes

Not initialized.

## How to Fix

Initialize.

## Example

```python
from flask_caching import Cache
c = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
```
