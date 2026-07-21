---
title: "[Solution] FastAPI Exception Handler Not Called Error"
description: "Fix FastAPI exception handler not called errors when custom handlers are registered but never executed."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom exception handlers in FastAPI may not be called if they are registered after the exception is raised or if middleware intercepts first.

## Common Causes

- Exception handler registered after the route that raises the exception
- Exception is a subclass of a type with a registered handler
- Middleware catches the exception before the handler processes it
- `raise_server_exceptions=True` in TestClient prevents handlers from running
- Exception raised outside of a request context

## How to Fix

### Register Handlers at App Creation

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid input", "detail": str(exc)},
    )

@app.exception_handler(Exception)
async def general_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"},
    )

@app.get("/validate")
def validate():
    raise ValueError("bad input")
```

### Check Exception Type Hierarchy

```python
class AppError(Exception):
    pass

class NotFoundError(AppError):
    pass

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(status_code=404, content={"error": str(exc)})

# NotFoundError will be caught by app_error_handler
```

### Ensure Middleware Does Not Intercept First

```python
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception:
            raise  # Re-raise so exception handlers can process it
```

## Examples

Always register exception handlers at the top of your application module, before defining routes.
