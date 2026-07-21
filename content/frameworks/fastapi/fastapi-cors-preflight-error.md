---
title: "[Solution] FastAPI CORS Preflight Error"
description: "Fix FastAPI CORS preflight errors when OPTIONS requests are blocked or return unexpected status codes."
frameworks: ["fastapi"]
error-types: ["security-error"]
severities: ["error"]
---

CORS preflight errors in FastAPI occur when the browser sends an OPTIONS request to check if cross-origin requests are allowed.

## Common Causes

- CORS middleware not configured to handle OPTIONS requests
- Custom middleware intercepts OPTIONS before CORS middleware
- `allow_methods` does not include the HTTP method being used
- `allow_headers` does not include custom headers in the request
- Middleware order prevents CORS headers from being added

## How to Fix

### Configure CORS Middleware Correctly

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
)
```

### Ensure Middleware Order

```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# CORS must be added first (outermost middleware)
app.add_middleware(CORSMiddleware, ...)
app.add_middleware(GZipMiddleware, ...)
```

## Examples

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Bug -- CORS middleware not configured
@app.post("/api/data")
def create_data():
    return {"created": True}

# Fix -- add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Without CORS middleware, the browser blocks the request with a CORS policy error.
