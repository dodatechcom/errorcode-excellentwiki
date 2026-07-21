---
title: "[Solution] FastAPI Pydantic Model Error"
description: "Pydantic model issues."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Pydantic model issues.

## Common Causes

Wrong field types.

## How to Fix

Define correctly.

## Example

```python
class User(BaseModel):
    age: int
    @field_validator('age')
    @classmethod
    def pos(cls, v):
        if v < 0: raise ValueError('must be positive')
        return v
```
