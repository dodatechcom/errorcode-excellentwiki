---
title: "[Solution] FastAPI Exception Response Model Error"
description: "Fix FastAPI exception response model errors when error responses do not match declared response schema."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When FastAPI endpoint declares a `response_model`, exception responses may not conform to the model schema.

## Common Causes

- `response_model` defined but exception returns different structure
- `responses` parameter missing error response definitions
- Pydantic model strict mode rejects the error response format
- OpenAPI documentation shows wrong error response schema
- Custom exception handler returns data that does not match model

## How to Fix

### Define Error Response Schemas

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str
    message: str
    code: int

class SuccessResponse(BaseModel):
    data: str

app = FastAPI()

@app.get(
    "/items/{item_id}",
    response_model=SuccessResponse,
    responses={404: {"model": ErrorResponse}},
)
def get_item(item_id: int):
    if item_id > 100:
        raise HTTPException(
            status_code=404,
            detail={"error": "not_found", "message": "Item not found", "code": 404},
        )
    return {"data": f"Item {item_id}"}
```

### Disable Response Model for Error Cases

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/data")
async def get_data():
    return JSONResponse(
        status_code=500,
        content={"error": "Server error"},
    )
```

## Examples

```python
from fastapi import FastAPI
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id == 0:
        # Bug -- returns JSONResponse that does not match UserResponse
        return JSONResponse(status_code=404, content={"error": "not found"})
    return {"id": user_id, "name": "Alice"}
```

Fix by raising HTTPException instead of returning JSONResponse directly.
