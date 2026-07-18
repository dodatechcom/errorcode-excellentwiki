---
title: "[Solution] Python Pydantic Validation Error — How to Fix"
description: "Fix Pydantic ValidationError when model validation fails. Resolve field type coercion, custom validators, and model config."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Pydantic Validation Error

A `pydantic.ValidationError` is raised when input data fails model validation. Pydantic enforces type constraints at model instantiation time, producing detailed error messages listing every invalid field.

## Why It Happens

Pydantic performs strict type checking at model instantiation. When you pass a string where an integer is expected, or omit required fields, Pydantic raises a ValidationError with the exact list of invalid fields and reasons.

## Common Error Messages

- `ValidationError: 1 validation error for Model`
- `Input should be a valid integer, unable to parse string as int`
- `Value is not a valid dict`
- `Field required [type=missing]`

## How to Fix It

### Fix 1: Use model_validate with coercion

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    name: str
    age: int

user = User.model_validate({'name': 'Alice', 'age': '25'})
```

### Fix 2: Add custom validators

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v.lower()
```

### Fix 3: Handle nested model errors

```python
from pydantic import BaseModel, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    addresses: List[Address]

try:
    user = User.model_validate({
        'name': 'Alice',
        'addresses': [{'street': '123 Main', 'city': 'NYC'}]
    })
except ValidationError as e:
    for error in e.errors():
        print(error['loc'], error['msg'])
```

### Fix 4: Configure extra fields

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
```

## Common Scenarios

- **API request validation** — FastAPI returns 422 when request body fails Pydantic validation.
- **ORM model mapping** — SQLAlchemy model attributes don't match Pydantic field types.
- **Config loading** — YAML/JSON config has unexpected types that fail Pydantic coercion.

## Prevent It

- Use model_validate() instead of **kwargs for better error messages
- Set model_config = ConfigDict(strict=True) during development
- Define __get_pydantic_validators__ for custom types

## Related Errors

- - [TypeError](/languages/python/typeerror/) — unsupported operand type
- - [ValueError](/languages/python/valueerror/) — invalid argument value
