---
title: "[Solution] FastAPI Body Model Error"
description: "Fix FastAPI body model errors when request body does not match the declared Pydantic model structure."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When the request body does not match the Pydantic model, FastAPI returns a 422 error. This happens with nested JSON structures or incorrect `Body()` usage.

## Common Causes

- Request body wrapped in an extra key when `Body(embed=True)` is not used
- Missing required nested objects in the JSON payload
- Type mismatches in nested model fields
- Using `Body()` without a default value on non-required fields
- Field aliases in Pydantic do not match the JSON keys

## How to Fix

### Match Request Structure to Model

```python
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address

@app.post("/users")
def create_user(user: User):
    return user
```

### Use `Body(embed=True)` for Wrapped Payloads

```python
@app.post("/users")
def create_user(user: User = Body(embed=True)):
    return user
```

### Define Field Aliases

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(alias="userName")
    email: str = Field(alias="userEmail")

    model_config = {"populate_by_name": True}
```

## Examples

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item
```

Sending `{"name": "Widget", "price": 9.99}` works. Sending `[{"name": "Widget", "price": 9.99}]` fails because FastAPI expects a JSON object, not an array. Use `list[Item]` to accept arrays.
