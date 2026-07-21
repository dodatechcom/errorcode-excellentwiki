---
title: "[Solution] FastAPI Route Not Found"
description: "FastAPI returns 404."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

FastAPI returns 404.

## Common Causes

Wrong URL path.

## How to Fix

Check routes.

## Example

```python
@app.get('/users/{user_id}')
async def get_user(user_id: int): return {'id': user_id}
```
