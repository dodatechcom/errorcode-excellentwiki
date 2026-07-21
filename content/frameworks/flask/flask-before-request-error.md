---
title: "[Solution] Flask Before Request Error"
description: "before_request not running."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

before_request not running.

## Common Causes

Not returning to abort.

## How to Fix

Return response to abort.

## Example

```python
@app.before_request
def check():
    if not request.headers.get('Auth'): return 'Unauthorized', 401
```
