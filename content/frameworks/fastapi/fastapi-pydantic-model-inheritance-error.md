---
title: "[Solution] FastAPI Pydantic Model Inheritance Error"
description: "Fix FastAPI Pydantic model inheritance errors when child classes lose parent field validation or configuration."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When inheriting from a Pydantic model, child classes may lose parent field validators, default values, or model configuration.

## Common Causes

- Child model overrides a parent field without redefining validators
- `model_config` from parent is not inherited correctly
- Private attributes prefixed with `_` are not inherited
- `@field_validator` or `@model_validator` decorators are not inherited
- Field ordering differs between parent and child

## How to Fix

### Use Proper Model Inheritance

```python
from pydantic import BaseModel, Field, field_validator

class BaseUser(BaseModel):
    name: str
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v

class AdminUser(BaseUser):
    role: str = "user"
    permissions: list[str] = []
```

### Redefine Validators in Child When Needed

```python
class SuperAdminUser(AdminUser):
    level: int = 1

    @field_validator("level")
    @classmethod
    def validate_level(cls, v):
        if v < 1 or v > 10:
            raise ValueError("Level must be between 1 and 10")
        return v
```

## Examples

```python
from pydantic import BaseModel, field_validator

class BaseResponse(BaseModel):
    status: str

    @field_validator("status")
    @classmethod
    def check_status(cls, v):
        if v not in ("ok", "error"):
            raise ValueError("Status must be ok or error")
        return v

class ErrorResponse(BaseResponse):
    message: str
    code: int
```

The validator is inherited. If not, call `ErrorResponse.model_rebuild()` after dynamic changes.
