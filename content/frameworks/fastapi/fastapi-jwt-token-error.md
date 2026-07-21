---
title: "[Solution] FastAPI JWT Token Error"
description: "JWT failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

JWT failing.

## Common Causes

Wrong secret.

## How to Fix

Use correct secret.

## Example

```python
from jose import jwt
SECRET = 'secret'
ALG = 'HS256'
def create_token(d): return jwt.encode(d, SECRET, algorithm=ALG)
```
