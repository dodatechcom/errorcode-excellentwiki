---
title: "[Solution] FastAPI Field Constraints Error"
description: "Field constraints not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Field constraints not working.

## Common Causes

Wrong constraints.

## How to Fix

Use Field.

## Example

```python
from pydantic import BaseModel, Field
class User(BaseModel):
    age: int = Field(ge=0, le=150)
```
