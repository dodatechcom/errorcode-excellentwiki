---
title: "[Solution] Flask After Request Error"
description: "after_request not modifying."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

after_request not modifying.

## Common Causes

Not returning response.

## How to Fix

Return modified response.

## Example

```python
@app.after_request
def add(r):
    r.headers['X-Frame'] = 'DENY'
    return r
```
