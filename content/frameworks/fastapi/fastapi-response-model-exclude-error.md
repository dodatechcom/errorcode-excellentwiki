---
title: "[Solution] FastAPI Response Model Exclude Error"
description: "Fix FastAPI response model exclude errors when fields are unexpectedly omitted or included in API responses."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When using `response_model_exclude` in FastAPI endpoints, fields may be excluded that should be included, or vice versa.

## Common Causes

- `response_model_exclude` set too broadly, removing required fields
- Using set instead of list for exclude parameter
- Field names do not match the Pydantic model attribute names
- `exclude_unset=True` in Pydantic model hides explicitly set defaults
- Both `include` and `exclude` parameters provided simultaneously

## How to Fix

### Use Specific Exclude Fields

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str

@app.get("/users/{user_id}", response_model=User, response_model_exclude={"password_hash"})
def get_user(user_id: int):
    return User(id=user_id, name="Alice", email="alice@example.com", password_hash="hashed")
```

### Use Response Model Alias

```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    model_config = {"from_attributes": True}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = get_user_from_db(user_id)
    return user  # password_hash excluded by not being in response model
```

## Examples

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    secret: str

@app.get("/user", response_model=User, response_model_exclude={"secret"})
def read_user():
    return {"id": 1, "name": "Alice", "secret": "hidden"}
```
