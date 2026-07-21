---
title: "[Solution] Flask Flask Permanent Session Error"
description: "Session not permanent."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Session not permanent.

## Common Causes

Not set.

## How to Fix

Set permanent.

## Example

```python
@app.before_request
def make_permanent():
    session.permanent = True
```
