---
title: "[Solution] FastAPI Exception Handler Custom Error"
description: "Custom exception not caught."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom exception not caught.

## Common Causes

Not registered.

## How to Fix

Register handler.

## Example

```python
@app.exception_handler(MyException)
async def h(req, exc): return JSONResponse(status_code=500, content={'e': str(exc)})
```
