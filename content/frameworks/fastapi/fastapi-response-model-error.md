---
title: "[Solution] FastAPI Response Model Error"
description: "Response validation failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Response validation failing.

## Common Causes

Fields don't match.

## How to Fix

Match response_model.

## Example

```python
@app.get('/users/{id}', response_model=UserOut)
async def get_user(id: int): return d
```
