---
title: "[Solution] FastAPI Request Validation Error Fix"
description: "Fix FastAPI request validation errors. Define proper Pydantic models, use correct parameter types, and handle validation responses."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# FastAPI Request Validation Error Fix

A FastAPI `Request Validation Error` is raised when an incoming HTTP request does not match the expected schema defined by path parameters, query parameters, or request body models.

## What This Error Means

Common messages:

- `422 Unprocessable Entity`
- `{"detail": [{"loc": ["body", "email"], "msg": "value is not a valid email address"}]}`
- `{"detail": [{"loc": ["path", "user_id"], "msg": "value is not a valid integer"}]}`

FastAPI uses Pydantic to validate all incoming data. When the request data does not conform to the defined types or constraints, FastAPI returns a 422 response with detailed error information.

## Common Causes

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

# Cause 1: Missing required field
@app.post("/users")
def create_user(user: UserCreate):
    return user
# POST /users {"name": "Alice"}  # Missing age and email -> 422

# Cause 2: Wrong type in path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
# GET /users/abc  # "abc" is not a valid int -> 422

# Cause 3: Invalid nested model data
class Order(BaseModel):
    items: list[str]
    total: float

@app.post("/orders")
def create_order(order: Order):
    return order
# POST /orders {"items": "not a list", "total": "not a float"}  # 422
```

## How to Fix

### Fix 1: Send complete request bodies

```python
# Correct request body
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```

### Fix 2: Use optional fields with defaults

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    bio: Optional[str] = None  # Optional field
```

### Fix 3: Add custom validation messages

```python
from pydantic import BaseModel, Field, field_validator

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v
```

### Fix 4: Handle validation errors globally

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def validation_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc), "path": request.url.path},
    )
```

### Fix 5: Use query parameter validation

```python
from fastapi import Query

@app.get("/search")
def search(q: str = Query(..., min_length=1), limit: int = Query(10, ge=1, le=100)):
    return {"q": q, "limit": limit}
```

## Related Errors

- {{< relref "pydantic-validation-error" >}} — Pydantic field validation error.
- {{< relref "jsondecodeerror" >}} — JSON decode error in request body.
