---
title: "[Solution] FastAPI Request Body Large Error"
description: "Request body too large."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Request body too large.

## Common Causes

Over limit.

## How to Fix

Increase limit.

## Example

```python
from starlette.requests import Request
@app.post('/upload')
async def upload(request: Request):
    body = await request.body()
```
