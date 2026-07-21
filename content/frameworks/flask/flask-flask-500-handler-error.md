---
title: "[Solution] Flask Flask 500 Handler Error"
description: "500 handler not catching."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

500 handler not catching.

## Common Causes

Not registered.

## How to Fix

Register.

## Example

```python
@app.errorhandler(500)
def h(e): return 'Server Error', 500
```
