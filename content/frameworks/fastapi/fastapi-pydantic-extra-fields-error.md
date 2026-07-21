---
title: "[Solution] FastAPI Pydantic Extra Fields Error"
description: "Fix FastAPI Pydantic extra fields error when models reject or silently accept unknown request data."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When a Pydantic model receives unexpected fields in the request body, FastAPI returns a 422 Validation Error. This happens because Pydantic v2 disallows extra fields by default.

## Common Causes

- Client sends additional fields not defined in the Pydantic model
- API contract changed but client still sends old field names
- Model class does not use `model_config` to allow extras
- Nested models receive unexpected keys from the request payload
- Third-party integration sends extra metadata fields

## How to Fix

### Allow Extra Fields on the Model

```python
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: str
    email: str
```

### Ignore Extra Fields Silently

```python
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str
    email: str
```

## Examples

```python
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()

class CreateUser(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str
    password: str

@app.post("/users")
def create_user(user: CreateUser):
    return {"username": user.username}
```

Sending `{"username": "alice", "password": "secret", "role": "admin"}` returns:

```json
{
  "detail": [
    {
      "type": "extra_forbidden",
      "loc": ["body", "role"],
      "msg": "Extra inputs are not permitted"
    }
  ]
}
```

Change `extra="forbid"` to `extra="allow"` or `extra="ignore"` to handle the extra fields.
