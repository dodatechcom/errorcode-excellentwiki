---
title: "[Solution] FastAPI Security API Key Error"
description: "API key not validated."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

API key not validated.

## Common Causes

Not checking.

## How to Fix

Validate in dependency.

## Example

```python
@app.get('/d')
async def d(key: str = Depends(verify_api_key)):
    return {'data': 'ok'}
```
