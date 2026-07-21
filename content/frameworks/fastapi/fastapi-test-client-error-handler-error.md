---
title: "[Solution] FastAPI Test Client Error Handler Error"
description: "Fix FastAPI test client error handler errors when exception handlers are not invoked during testing."
frameworks: ["fastapi"]
error-types: ["test-error"]
severities: ["error"]
---

When testing FastAPI applications, custom exception handlers may not be invoked if the test client does not trigger them correctly.

## Common Causes

- Exception handler registered after test client creation
- Test client does not send requests that trigger the handler
- Exception type in handler does not match the actual exception
- Handler returns response before middleware processes it
- `raise_server_exceptions=True` in TestClient bypasses handlers

## How to Fix

### Set `raise_server_exceptions=False`

```python
from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def custom_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "custom": True},
    )

client = TestClient(app, raise_server_exceptions=False)

def test_custom_error():
    response = client.get("/missing")
    assert response.status_code == 404
    assert response.json()["custom"] is True
```

### Register Handlers Before Tests

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)},
    )

@app.get("/validate")
def validate():
    raise ValueError("Invalid input")

# Test after handler is registered
client = TestClient(app)

def test_validation_error():
    response = client.get("/validate")
    assert response.json()["error"] == "Invalid input"
```

## Examples

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

# Bug -- raise_server_exceptions=True hides the custom handler
client = TestClient(app, raise_server_exceptions=True)

# Fix
client = TestClient(app, raise_server_exceptions=False)
```

With `raise_server_exceptions=True` (the default), exceptions propagate as test failures instead of being handled by exception handlers.
