---
title: "[Solution] FastAPI Response Cookie Error"
description: "Cookie not setting."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Cookie not setting.

## Common Causes

Wrong usage.

## How to Fix

Use Response.

## Example

```python
from fastapi import Response
@app.get('/login')
async def login(r: Response):
    r.set_cookie('session', 'abc')
    return {'ok': True}
```
