---
title: "[Solution] Python Pydantic Error — Data Validation Failures"
description: "Fix Python Pydantic errors like ValidationError, model construction, field validators, and type coercion. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 434
---

# Python Pydantic Error — Data Validation Failures

Pydantic errors occur when input data fails validation, models cannot be constructed, field validators reject values, or type coercion fails. These are common in API development and data processing pipelines.

## Common Causes

```python
# ValidationError: field type mismatch
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

User(name="John", age="not-a-number")  # age must be int

# ValidationError: missing required field
User(name="John")

# ValidationError: value fails custom validator
from pydantic import BaseModel, field_validator

class PositiveNumber(BaseModel):
    value: int

    @field_validator("value")
    @classmethod
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("must be positive")
        return v

PositiveNumber(value=-5)

# ConfigError: model configuration error
class BadModel(BaseModel):
    class Config:
        orm_mode = True  # Pydantic v2: from_attributes = True

# ValidationError: extra fields not allowed
class StrictModel(BaseModel):
    name: str

    class Config:
        extra = "forbid"

StrictModel(name="John", age=30)
```

## How to Fix

### Fix 1: Match Field Types Exactly
Ensure input data types match model field types.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Correct: provide int for age
user = User(name="John", age=30)

# Pydantic will coerce compatible types (str to int fails, int to str works)
user = User(name="John", age="30")  # Pydantic v2 coerces int from str
```

### Fix 2: Provide All Required Fields
Include all required fields in model instantiation.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int = 0  # optional with default

# All required fields provided
user = User(name="John", email="john@example.com")
print(user.age)  # 0
```

### Fix 3: Use Field Validators Correctly
Implement validators with proper decorator usage.
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError("Age must be between 0 and 150")
        return v

user = User(name="John", age=25)
```

### Fix 4: Use Pydantic v2 Configuration
Update model configuration for Pydantic v2.
```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        str_strip_whitespace=True,
    )

    name: str
    age: int
```

### Fix 5: Handle Validation Errors Gracefully
Catch and process ValidationError details.
```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    user = User(name="John", age="invalid")
except ValidationError as e:
    for error in e.errors():
        print(f"Field: {error['loc']}, Error: {error['msg']}")
```

## Examples

```python
# Complete API request validation
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    age: int
    role: str = "user"

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters")
        return v.strip()

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v < 18:
            raise ValueError("Must be at least 18 years old")
        return v

try:
    request = CreateUserRequest(name="John", email="john@example.com", age=25)
    print(request.model_dump())
except ValidationError as e:
    print(e.errors())
```

## Related Errors

- [Python FastAPI Error](/languages/python/python-fastapi-error/)
- [Python Loguru Error](/languages/python/python-loguru-error/)
- [Python pytest Error](/languages/python/python-pytest-error-extended/)
