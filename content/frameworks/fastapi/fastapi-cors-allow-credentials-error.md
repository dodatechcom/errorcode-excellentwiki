---
title: "[Solution] FastAPI CORS Allow Credentials Error"
description: "Fix FastAPI CORS allow credentials errors when browsers reject cross-origin requests with authentication."
frameworks: ["fastapi"]
error-types: ["security-error"]
severities: ["error"]
---

When using `CORSMiddleware` with `allow_credentials=True`, the browser rejects requests if `allow_origins` includes `"*"`.

## Common Causes

- Using `allow_origins=["*"]` with `allow_credentials=True`
- Missing `Access-Control-Allow-Credentials` header in response
- Origin in request does not match any entry in `allow_origins`
- Preflight request fails because allowed methods do not include the request method
- Browser blocks cookies due to SameSite policy

## How to Fix

### Set Explicit Origins

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com", "https://admin.myapp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Examples

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Bug -- star origin with credentials is rejected by browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
)
```

Replace `"*"` with specific allowed origins to fix the CORS policy error.
