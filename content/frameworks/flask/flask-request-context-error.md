---
title: "[Solution] Flask Request Context Error"
description: "Request not available."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Request not available.

## Common Causes

Accessing outside handler.

## How to Fix

Only in route handlers.

## Example

```python
@app.route('/p')
def h(): data = request.json
```
