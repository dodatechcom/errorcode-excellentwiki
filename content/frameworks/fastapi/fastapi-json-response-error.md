---
title: "[Solution] FastAPI JSON Response Error"
description: "JSONResponse failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

JSONResponse failing.

## Common Causes

Data not serializable.

## How to Fix

Ensure JSON safe.

## Example

```python
from fastapi.responses import JSONResponse
@app.get('/d')
async def d(): return JSONResponse(content={'k': 'v'})
```
