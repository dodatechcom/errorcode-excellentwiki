---
title: "[Solution] Python Pydantic V2 Migration Error — How to Fix"
description: "Fix Python Pydantic V2 migration errors. Resolve validator changes, schema generation issues, and v1 to v2 compatibility problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Pydantic V2 Migration Error

A `pydantic.ValidationError` or `AttributeError` occurs when code written for Pydantic V1 uses deprecated APIs like `validator`, `root_validator`, or `Config` class that have changed in V2.

## Why It Happens

Pydantic V2 introduced breaking changes including renamed decorators, new model configuration syntax, different serialization behavior, and replacement of `orm_mode` with `model_config`. Code migrated from V1 without updating these patterns will fail.

## Common Error Messages

- `AttributeError: 'ConfigDict' object has no attribute 'orm_mode'`
- `ValidationError: 1 validation error for Model — field required`
- `DeprecationWarning: 'validator' has been deprecated in V2`
- `TypeError: Model.__init__() got an unexpected keyword argument`

## How to Fix It

### Fix 1: Update model configuration

```python
from pydantic import BaseModel

# Wrong — V1 syntax
# class User(BaseModel):
#     name: str
#     class Config:
#         orm_mode = True

# Correct — V2 syntax
from pydantic import ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    age: int

# Create instance
user = User(name="Alice", age=25)
print(user.model_dump())
```

### Fix 2: Replace deprecated validators

```python
from pydantic import BaseModel, field_validator, model_validator

# Wrong — V1 validators
# class User(BaseModel):
#     age: int
#     @validator("age")
#     def validate_age(cls, v):
#         if v < 0:
#             raise ValueError("age must be positive")
#         return v

# Correct — V2 validators
class User(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("age must be positive")
        return v

user = User(age=25)
print(user)

# Model-level validators
class UserWithCheck(BaseModel):
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def check_passwords(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self
```

### Fix 3: Update serialization methods

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=25)

# Wrong — V1 serialization methods
# user.dict()  # AttributeError in V2
# user.json()  # AttributeError in V2

# Correct — V2 serialization
data = user.model_dump()
print(data)

json_str = user.model_dump_json()
print(json_str)

# Deserialize from dict
user2 = User.model_validate(data)
print(user2)

# Deserialize from JSON
user3 = User.model_validate_json(json_str)
print(user3)
```

### Fix 4: Handle Optional fields correctly

```python
from pydantic import BaseModel
from typing import Optional

# Wrong — V1 allowed None for Optional by default
# class User(BaseModel):
#     name: str
#     nickname: Optional[str]  # V2 requires explicit default

# Correct — provide default for Optional fields
class User(BaseModel):
    name: str
    nickname: Optional[str] = None
    age: int = 0

user = User(name="Alice")
print(user.model_dump())

# Use model_fields to inspect
print(User.model_fields.keys())
```

## Common Scenarios

- **orm_mode deprecated** — ORM integration now uses `from_attributes=True` instead of `orm_mode = True`.
- **validator signature changed** — `@validator` is now `@field_validator` with `@classmethod` decorator required.
- **dict() removed** — All `dict()`, `json()`, `parse_obj()` methods replaced with `model_dump()`, `model_dump_json()`, `model_validate()`.

## Prevent It

- Use `pydantic migrate` CLI tool to automatically update V1 code to V2 syntax.
- Run tests with `pydantic` version pinning to catch deprecation warnings early.
- Replace all `.dict()` calls with `.model_dump()` and `.json()` with `.model_dump_json()`.

## Related Errors

- [AttributeError](/languages/python/attributeerror/) — attribute does not exist on object
- [ValidationError](/languages/python/validation-error/) — model validation failed
- [DeprecationWarning](/languages/python/deprecation-warning/) — deprecated API usage
