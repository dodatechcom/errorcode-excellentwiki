---
title: "[Solution] FastAPI Middleware Set Cookie Error"
description: "Fix FastAPI middleware set cookie errors when cookies are not set or overwritten in response headers."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When middleware sets cookies on the response, they may not reach the browser if the middleware order is wrong or if the response is already committed.

## Common Causes

- Middleware order prevents cookies from being added to the final response
- Response is already started when middleware tries to set a cookie
- Cookie domain or path does not match the current request
- SameSite attribute conflicts with cross-origin requests
- Secure flag set but application is running over HTTP

## How to Fix

### Add Cookies in Middleware Before Response

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

class CookieMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.set_cookie(
            key="session_id",
            value="abc123",
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=3600,
        )
        return response

app = FastAPI()
app.add_middleware(CookieMiddleware)
```

## Examples

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

class BrokenCookieMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = call_next(request)  # Bug -- missing await
        response.set_cookie("key", "value")
        return response
```

The missing `await` on `call_next(request)` means the response is a coroutine. Always use `response = await call_next(request)`.
