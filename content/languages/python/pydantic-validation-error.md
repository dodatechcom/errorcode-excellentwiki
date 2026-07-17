---
title: "[Solution] Pydantic Field Validation Error Fix"
description: "Fix Pydantic validation errors. Define proper field constraints, use custom validators, and handle coercion settings."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pydantic", "validation", "model", "schema", "field"]
weight: 5
---

# Pydantic Field Validation Error Fix

A Pydantic `ValidationError` is raised when input data does not conform to the defined model schema, field constraints, or custom validation rules.

## What This Error Means

Common messages:

- `pydantic.ValidationError: 1 validation error for Model`
- `field_name: Input should be a valid integer`
- `field_name: Field required`

Pydantic enforces type checking and constraints on model fields. Invalid data raises a `ValidationError` with detailed location and message information.

## Common Causes

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Cause 1: Type mismatch
class User(BaseModel):
    age: int

User(age="not_a_number")  # ValidationError

# Cause 2: Missing required field
class Config(BaseModel):
    database_url: str
    api_key: str

Config(database_url="postgres://...")  # Missing api_key

# Cause 3: Constraint violation
class Product(BaseModel):
    price: float = Field(gt=0, lt=1_000_000)

Product(price=-10)  # price must be > 0

# Cause 4: Strict mode rejects coercion
class StrictModel(BaseModel):
    model_config = {"strict": True}
    count: int

StrictModel(count="42")  # Rejects string-to-int coercion
```

## How to Fix

### Fix 1: Use correct types in input data

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Correct input
user = User(name="Alice", age=30)

# Also works — Pydantic coerces compatible types
user = User(name="Alice", age="30")  # age becomes int 30
```

### Fix 2: Set default values for optional fields

```python
from pydantic import BaseModel, Field
from typing import Optional

class Config(BaseModel):
    database_url: str
    api_key: str = "default-key"
    debug: bool = False
    max_retries: Optional[int] = None
```

### Fix 3: Add custom validators

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v.lower()
```

### Fix 4: Handle validation errors in code

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    age: int

try:
    user = User(age="abc")
except ValidationError as e:
    for error in e.errors():
        print(f"{error['loc']}: {error['msg']}")
```

### Fix 5: Use model_validate for dict input

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# From dict — use model_validate instead of constructor
data = {"name": "Alice", "age": 30}
user = User.model_validate(data)

# From JSON string
user = User.model_validate_json('{"name": "Alice", "age": 30}')
```

## Related Errors

- {{< relref "fastapi-validation-error" >}} — FastAPI request validation error.
- {{< relref "valueerror" >}} — General Python ValueError.
