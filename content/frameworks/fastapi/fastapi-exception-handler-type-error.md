---
title: "[Solution] FastAPI Exception Handler Type Error"
description: "Fix FastAPI exception handler type errors when handler signature does not match the expected exception type."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When registering custom exception handlers in FastAPI, type mismatches between the handler signature and the registered exception class cause the handler to never be called.

## Common Causes

- Handler function signature has wrong parameter types
- Exception class registered is a base class but handler expects a subclass
- Handler returns wrong response type
- Multiple handlers registered for the same exception type
- Handler registered after the exception is raised

## How to Fix

### Use Correct Handler Signature

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class CustomError(Exception):
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code

@app.exception_handler(CustomError)
async def custom_error_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.code,
        content={"error": exc.message},
    )

@app.get("/fail")
def fail():
    raise CustomError("Something went wrong", code=400)
```

### Handle Multiple Exception Types

```python
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"error": str(exc)})

@app.exception_handler(KeyError)
async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(status_code=400, content={"error": f"Missing key: {exc}"})
```

## Examples

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Bug -- wrong parameter type in handler
@app.exception_handler(ValueError)
def wrong_handler(exc: str):  # Should be (request, exc)
    return JSONResponse(status_code=400, content={"error": str(exc)})

# Fix -- correct signature
@app.exception_handler(ValueError)
async def correct_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"error": str(exc)})
```

The handler must accept `request: Request` as the first parameter and `exc: ExceptionType` as the second.
