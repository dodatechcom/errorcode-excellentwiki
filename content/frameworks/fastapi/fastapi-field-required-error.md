---
title: "[Solution] FastAPI Field Required Error"
description: "422 for missing field."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

422 for missing field.

## Common Causes

Missing required field.

## How to Fix

Include all fields.

## Example

```python
class User(BaseModel):
    name: str
    email: str
```
