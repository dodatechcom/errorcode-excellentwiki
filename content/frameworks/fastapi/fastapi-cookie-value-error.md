---
title: "[Solution] FastAPI Cookie Value Error"
description: "Cookie not reading."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Cookie not reading.

## Common Causes

Wrong parameter.

## How to Fix

Use Cookie.

## Example

```python
from fastapi import Cookie
@app.get('/c')
async def c(session: str = Cookie(...)):
    return {'session': session}
```
