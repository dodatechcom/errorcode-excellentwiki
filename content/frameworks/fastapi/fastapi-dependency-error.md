---
title: "[Solution] FastAPI Dependency Error — How to Fix"
description: "Fix FastAPI dependency injection errors. Resolve dependency resolution failures and circular dependency issues."
frameworks: ["fastapi"]
error-types: ["application-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI dependency error occurs when the dependency injection system fails to resolve or execute dependencies.

## Why It Happens

Dependency errors happen due to circular dependencies, missing providers, incorrect function signatures, or runtime failures.

## Common Error Messages

```
AssertionError: Dependency pool exhausted
```

```
TypeError: 'NoneType' object is not callable
```

```
NameError: name 'db' is not defined
```

```
FastAPIError: Dependency has parameters that cannot be resolved
```

## How to Fix It

### 1. Define Dependencies with Yield

Use generator dependencies for cleanup.

```python
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.token == token).first()
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return user

@app.get('/users/me')
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

### 2. Avoid Circular Dependencies

Restructure to break cycles.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db)):
    return db.query(User).first()

def get_user_posts(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Post).filter(Post.user_id == user.id).all()
```

### 3. Use Class-Based Dependencies

Create classes for complex initialization.

```python
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get('/items/')
async def read_items(commons: CommonQueryParams = Depends()):
    return get_items(query=commons.q, skip=commons.skip, limit=commons.limit)
```

### 4. Handle Dependency Errors

Add error handling for failures.

```python
async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != 'secret-key':
        raise HTTPException(status_code=403, detail='Invalid API key')
    return x_api_key

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={'error': exc.detail})
```

## Common Scenarios

**Scenario 1: Database session not closing.**
Use `yield` with try/finally.

**Scenario 2: Dependency returns None.**
Check that the function returns a value.

**Scenario 3: Circular dependency detected.**
Restructure to separate concerns.

## Prevent It

1. **Keep dependency chains short.**
Limit to 3-4 levels.

2. **Test dependencies in isolation.**
Write unit tests for each.

3. **Use dependency overrides for testing.**
Override with mocks.

