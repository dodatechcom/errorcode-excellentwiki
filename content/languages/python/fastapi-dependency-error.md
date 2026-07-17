---
title: "[Solution] FastAPI Dependency Injection Error Fix"
description: "Fix FastAPI dependency injection errors. Resolve circular dependencies, override dependencies correctly, and handle async dependency issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["fastapi", "dependency-injection", "di", "api", "inject"]
weight: 5
---

# FastAPI Dependency Injection Error Fix

A FastAPI dependency injection error occurs when a dependency cannot be resolved, has circular references, or fails during execution. These typically surface as 500 or 422 errors.

## What This Error Means

Common messages:

- `FastAPIError: Dependency [func] has circular dependency`
- `AssertionError` during dependency resolution
- `RuntimeError: No suitable constructor for dependency`

FastAPI's dependency injection system resolves function arguments by calling sub-dependencies. When a dependency chain is broken, circular, or misconfigured, FastAPI cannot build the dependency graph.

## Common Causes

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Cause 1: Circular dependency
def get_db():
    yield db_session

def get_user(db=Depends(get_db)):
    return db.query(User).first()

def get_current_user(user=Depends(get_user)):
    return user

@app.get("/items")
def get_items(user=Depends(get_current_user), db=Depends(get_db)):
    pass  # May create circular resolution

# Cause 2: Missing yield in async generator
async def get_db():
    db = SessionLocal()
    return db  # No yield — not a proper generator dependency

# Cause 3: Dependency raises during resolution
def get_current_user(token: str = Header(...)):
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=401)  # Dependency fails
    return user
```

## How to Fix

### Fix 1: Break circular dependencies

```python
# Wrong — circular
def dep_a(b=Depends(dep_b)):
    return a

def dep_b(a=Depends(dep_a)):
    return b

# Correct — shared intermediate dependency
def get_db():
    yield SessionLocal()

def dep_a(db=Depends(get_db)):
    return "a"

def dep_b(db=Depends(get_db)):
    return "b"
```

### Fix 2: Use proper generator pattern for cleanup

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Fix 3: Override dependencies in tests

```python
from fastapi.testclient import TestClient

def override_get_db():
    yield test_db_session

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
response = client.get("/users")
```

### Fix 4: Use callable classes for complex dependencies

```python
class AuthService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_current_user(self, token: str = Header(...)):
        return self.db.query(User).filter_by(token=token).first()

@app.get("/me")
def get_me(auth: AuthService = Depends()):
    return auth.get_current_user()
```

### Fix 5: Validate dependency signature

```python
from typing import Annotated
from fastapi import Depends, Query

def pagination(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    return {"offset": offset, "limit": limit}

@app.get("/items")
def list_items(pages: dict = Depends(pagination)):
    return pages
```

## Related Errors

- {{< relref "fastapi-validation-error" >}} — FastAPI request validation error.
- {{< relref "pydantic-validation-error" >}} — Pydantic field validation error.
