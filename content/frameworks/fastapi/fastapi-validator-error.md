---
title: "[Solution] FastAPI Validator Error"
description: "Validator not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Validator not working.

## Common Causes

Wrong logic.

## How to Fix

Fix validator.

## Example

```python
from pydantic import model_validator
class User(BaseModel):
    p1: str
    p2: str
    @model_validator(mode='after')
    def check(self):
        if self.p1 != self.p2: raise ValueError('mismatch')
        return self
```
