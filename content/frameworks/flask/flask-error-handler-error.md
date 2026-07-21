---
title: "[Solution] Flask Error Handler Error"
description: "Custom handler not catching."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom handler not catching.

## Common Causes

Wrong code.

## How to Fix

Register correctly.

## Example

```python
@app.errorhandler(404)
def h(e): return render_template('404.html'), 404
```
