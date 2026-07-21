---
title: "[Solution] Flask 404 Handler Error"
description: "Custom 404 not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom 404 not working.

## Common Causes

Not registered.

## How to Fix

Register handler.

## Example

```python
@app.errorhandler(404)
def nf(e): return 'Not Found', 404
```
