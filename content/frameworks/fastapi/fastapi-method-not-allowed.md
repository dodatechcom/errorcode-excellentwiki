---
title: "[Solution] FastAPI Method Not Allowed"
description: "FastAPI returns 405."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

FastAPI returns 405.

## Common Causes

Wrong HTTP method.

## How to Fix

Use correct method.

## Example

```python
@app.post('/users')
async def create(user: User): return user
```
