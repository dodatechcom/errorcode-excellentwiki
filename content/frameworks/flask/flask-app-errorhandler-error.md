---
title: "[Solution] Flask App Errorhandler Error"
description: "app.errorhandler not registering."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

app.errorhandler not registering.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
@app.errorhandler(500)
def h(e): return 'Error', 500
```
