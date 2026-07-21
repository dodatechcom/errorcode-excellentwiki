---
title: "[Solution] FastAPI Pydantic Config Error"
description: "Pydantic config wrong."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Pydantic config wrong.

## Common Causes

Wrong config dict.

## How to Fix

Use ConfigDict.

## Example

```python
from pydantic import ConfigDict
class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
```
