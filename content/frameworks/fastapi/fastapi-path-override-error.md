---
title: "[Solution] FastAPI Path Override Error"
description: "Fix FastAPI path override errors when route parameters conflict or shadow existing endpoints."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When two routes in FastAPI have overlapping path patterns, the first registered route takes precedence. This causes the second route to never be reached.

## Common Causes

- Static path segment shadows a parameterized route
- Path parameters with overlapping patterns like `/users/{id}` vs `/users/me`
- Catch-all routes placed before specific routes
- Router includes registered in the wrong order
- Mounting sub-applications at overlapping paths

## How to Fix

### Register Specific Routes Before Wildcards

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
def get_current_user():
    return {"user": "current"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### Order Router Includes Correctly

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

user_router = APIRouter(prefix="/users")
admin_router = APIRouter(prefix="/admin")

@app.get("/users/me")
def specific_route():
    return {"path": "specific"}

app.include_router(user_router)
app.include_router(admin_router)
```

## Examples

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# This route will NEVER match because /items/{item_id} catches it first
@app.get("/items/special")
def get_special():
    return {"special": True}
```

Fix by reordering:

```python
@app.get("/items/special")
def get_special():
    return {"special": True}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```
