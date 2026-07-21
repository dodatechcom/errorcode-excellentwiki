---
title: "[Solution] FastAPI HTTPException Error"
description: "HTTPException wrong status."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

HTTPException wrong status.

## Common Causes

Wrong code.

## How to Fix

Use correct code.

## Example

```python
from fastapi import HTTPException
@app.get('/items/{id}')
async def get(id: int):
    if id not in items: raise HTTPException(status_code=404, detail='Not found')
```
