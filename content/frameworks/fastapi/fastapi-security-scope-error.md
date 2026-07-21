---
title: "[Solution] FastAPI Security Scope Error"
description: "Security scopes not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Security scopes not working.

## Common Causes

Wrong dependency.

## How to Fix

Use Security.

## Example

```python
from fastapi import Security
from fastapi.security import SecurityScopes
@app.get('/admin')
async def admin(s: SecurityScopes = Security(scopes=['admin'])):
    return {'admin': True}
```
