---
title: "[Solution] FastAPI Validation Error -- How to Fix"
description: "Fix FastAPI validation errors. Resolve Pydantic validation failures and request data validation issues."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI validation error occurs when request data does not match defined Pydantic models. FastAPI automatically validates and returns 422 errors.

## Why It Happens

Validation errors happen when request bodies, query parameters, or path parameters do not match expected types, are missing required fields, or fail custom validators.

## Common Error Messages

```
ValidationError: 1 validation error for Request body
```

```
field required (type=value_error.missing)
```

```
value is not a valid integer (type=type_error.integer)
```

```
ensure this value has at least 1 items
```

## How to Fix It

### 1. Define Pydantic Models Clearly

Create explicit request and response models.

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: str
    age: int = Field(..., ge=0, le=150)
    bio: Optional[str] = None

    class Config:
        schema_extra = {
            'example': {'name': 'John', 'email': 'john@example.com', 'age': 30}
        }
```

### 2. Add Custom Validators

Use Pydantic validators for complex rules.

```python
from pydantic import validator, BaseModel

class Order(BaseModel):
    quantity: int
    price: float
    total: float

    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be positive')
        return v

    @validator('total')
    def validate_total(cls, v, values):
        if 'quantity' in values and 'price' in values:
            expected = values['quantity'] * values['price']
            if abs(v - expected) > 0.01:
                raise ValueError(f'Total must be {expected}')
        return v
```

### 3. Use Optional Fields with Defaults

Make fields optional to avoid missing data errors.

```python
from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None

@app.put('/users/{user_id}')
async def update_user(user_id: int, user: UserUpdate):
    update_data = user.dict(exclude_unset=True)
```

### 4. Handle Validation Errors Gracefully

Customize error responses.

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

@app.exception_handler(ValidationError)
async def validation_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={'error': 'Validation failed', 'details': [
            {'field': e['loc'][-1], 'message': e['msg']} for e in exc.errors()
        ]}
    )
```

## Common Scenarios

**Scenario 1: API returns 422 when sending JSON.**
Check Content-Type header is `application/json`.

**Scenario 2: Optional field causes validation error.**
Add `Optional[type] = None`.

**Scenario 3: Nested model validation fails.**
Ensure nested models have proper fields.

## Prevent It

1. **Write OpenAPI documentation.**
Use Pydantic models with examples.

2. **Test all endpoints with invalid data.**
Verify validation rejects bad input.

3. **Use versioned API models.**
Create separate models for versions.

