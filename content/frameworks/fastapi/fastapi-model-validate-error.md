---
title: "[Solution] FastAPI Model Validate Error"
description: "Fix FastAPI Pydantic model validation errors when incoming data fails schema validation rules."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

Pydantic model validation errors in FastAPI occur when request data does not match the declared model schema.

## Common Causes

- Missing required fields in the request body
- Wrong data types (e.g., string where integer is expected)
- Values outside allowed ranges (min/max constraints)
- Invalid email, URL, or UUID format
- Enum fields receive values not in the allowed set

## How to Fix

### Add Clear Validation Rules

```python
from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"

class CreateUser(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=0, le=150)
    role: Role = Role.user
```

### Custom Validators

```python
from pydantic import BaseModel, field_validator

class Order(BaseModel):
    quantity: int
    price: float

    @field_validator("quantity")
    @classmethod
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v
```

### Handle Validation Errors in Routes

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
        })
    return JSONResponse(status_code=422, content={"errors": errors})
```

## Examples

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

# This passes validation
p = Product(name="Widget", price=9.99, stock=100)

# This fails -- price is negative
try:
    p = Product(name="Widget", price=-5.0, stock=100)
except ValueError as e:
    print(e)
```
