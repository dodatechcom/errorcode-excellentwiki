---
title: "[Solution] Flask URL Not Found 404"
description: "Flask returns 404."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Flask returns 404.

## Common Causes

Wrong URL path.

## How to Fix

Verify routes.

## Example

```python
@app.route('/hello')
def hello(): return 'Hello'
```
