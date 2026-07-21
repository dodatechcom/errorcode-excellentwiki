---
title: "[Solution] FastAPI Request ID Middleware Error"
description: "Fix FastAPI request ID middleware errors when context variables are lost between middleware and route handlers."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When using middleware to assign a request ID, the value may not be accessible in route handlers or dependency functions.

## Common Causes

- Using `contextvars` without proper middleware integration
- Middleware does not set the context variable before calling `call_next`
- Async context lost when using background tasks
- Thread pool execution breaks context propagation
- Middleware order prevents the request ID from being set in time

## How to Fix

### Use a ContextVar with ASGI Middleware

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import contextvars
import uuid

request_id_var: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="")

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        req_id = str(uuid.uuid4())
        request_id_var.set(req_id)
        request.state.request_id = req_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        return response

app = FastAPI()
app.add_middleware(RequestIDMiddleware)

@app.get("/info")
def get_info(request: Request):
    return {"request_id": request.state.request_id}
```

## Examples

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

app = FastAPI()

async def bad_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    # Bug: not storing request_id anywhere accessible
    response = await call_next(request)
    return response
```

Store the ID on `request.state` and read it in the handler using `request.state.request_id`.
