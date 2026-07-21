---
title: "[Solution] FastAPI Request Header Error"
description: "Header not reading."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Header not reading.

## Common Causes

Wrong parameter.

## How to Fix

Use Header.

## Example

```python
from fastapi import Header
@app.get('/h')
async def h(x_token: str = Header(...)):
    return {'token': x_token}
```
