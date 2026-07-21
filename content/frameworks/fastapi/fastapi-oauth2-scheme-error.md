---
title: "[Solution] FastAPI OAuth2 Scheme Error"
description: "OAuth2 token not extracted."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

OAuth2 token not extracted.

## Common Causes

Wrong config.

## How to Fix

Configure correctly.

## Example

```python
from fastapi.security import OAuth2PasswordBearer
oauth2 = OAuth2PasswordBearer(tokenUrl='token')
@app.get('/me')
async def me(token: str = Depends(oauth2)): return {'token': token}
```
