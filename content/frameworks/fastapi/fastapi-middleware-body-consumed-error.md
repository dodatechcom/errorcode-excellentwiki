---
title: "[Solution] FastAPI Middleware Body Consumed Error"
description: "Fix FastAPI middleware body consumed errors when request body is empty in route handlers after middleware reads it."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When middleware reads the request body, the body stream is consumed and the route handler receives an empty body.

## Common Causes

- Middleware calls `await request.body()` to log or validate the request
- Authentication middleware reads the body for signature verification
- Custom logging middleware inspects request content
- Request body is needed in multiple places
- Starlette `BaseHTTPMiddleware` consumes the body stream

## How to Fix

### Cache the Body in Request State

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

class BodyCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        request._body = body
        response = await call_next(request)
        return response

app = FastAPI()
app.add_middleware(BodyCacheMiddleware)

@app.post("/data")
async def handle_data(request: Request):
    body = await request.body()
    return {"received": len(body)}
```

## Examples

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()  # Consumes the stream
        print(f"Request body: {body}")
        return await call_next(request)

app = FastAPI()
app.add_middleware(LoggingMiddleware)

@app.post("/items")
async def create_item(name: str, price: float):
    return {"name": name, "price": price}  # Fails -- body already consumed
```

Fix by caching the body on the request object so it can be read again.
