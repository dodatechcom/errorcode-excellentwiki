---
title: "[Solution] FastAPI HTTPException Error Detail"
description: "Fix FastAPI HTTPException error detail messages not appearing correctly in API responses."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When raising `HTTPException` in FastAPI, the `detail` message may not appear in the response if the exception handler configuration is incorrect.

## Common Causes

- `detail` parameter is not a string (e.g., passing a dict without stringifying)
- `response_model` on the endpoint does not include error response schema
- Custom exception handler overrides the default HTTP error format
- `headers` parameter in HTTPException conflicts with middleware headers
- Status code 200 used with HTTPException (should use 4xx/5xx)

## How to Fix

### Use Proper Detail Format

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found",
        )
    return {"user_id": user_id}
```

### Return Structured Error Responses

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id > 100:
        raise HTTPException(
            status_code=404,
            detail={
                "message": "Item not found",
                "item_id": item_id,
                "suggestion": "Check the item ID and try again",
            },
        )
    return {"item_id": item_id}
```

### Set Response Model for Error Documentation

```python
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str

@app.get("/data", responses={404: {"model": ErrorResponse}})
def get_data(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return {"data": "value"}
```

## Examples

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Bug -- passing None as detail
@app.get("/broken")
def broken():
    raise HTTPException(status_code=400, detail=None)

# Fix -- always provide a detail string
@app.get("/working")
def working():
    raise HTTPException(status_code=400, detail="Bad request")
```

Always provide a meaningful `detail` string in HTTPException.
