---
title: "[Solution] FastAPI OAuth2 Password Form Error"
description: "Password form not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Password form not working.

## Common Causes

Wrong form class.

## How to Fix

Use OAuth2PasswordRequestForm.

## Example

```python
from fastapi.security import OAuth2PasswordRequestForm
@app.post('/token')
async def token(form: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': 'token', 'token_type': 'bearer'}
```
