---
title: "[Solution] Python FastAPI Error — Web Framework Failures"
description: "Fix Python FastAPI errors like request validation, dependency injection, response model errors, and middleware. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 435
---

# Python FastAPI Error — Web Framework Failures

FastAPI errors occur when request validation fails, dependency injection is misconfigured, response models don't match actual data, or middleware conflicts. These are common in API development.

## Common Causes

```python
# RequestValidationError: request body doesn't match model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item

# Send: {"name": "Widget", "price": "not-a-number"}

# DependencyError: dependency injection fails
from fastapi import Depends

async def get_db():
    db = connect_db()
    if not db:
        raise Exception("Database connection failed")
    yield db

@app.get("/users")
def get_users(db=Depends(get_db)):
    return db.query(User)

# ResponseValidationError: return data doesn't match response_model
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return {"name": "Widget", "price": "abc", "extra": "field"}

# StarletteHTTPException: route not found
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Missing dependency: route depends on param not in request
@app.get("/search")
def search(q: str = None):
    return {"q": q}
```

## How to Fix

### Fix 1: Validate Request Bodies with Pydantic Models
Use Pydantic models to automatically validate request data.
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: str | None = None

@app.post("/items")
def create_item(item: Item):
    return {"item": item.model_dump(), "message": "Item created"}
```

### Fix 2: Handle Dependency Injection Errors
Use proper error handling in dependencies.
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection failed")
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```

### Fix 3: Match Response Model to Actual Return Data
Ensure response data matches the declared response_model.
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemResponse(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    return {"name": "Widget", "price": 29.99}
```

### Fix 4: Use Proper Exception Handlers
Register custom exception handlers for different error types.
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class CustomException(Exception):
    def __init__(self, name: str, detail: str):
        self.name = name
        self.detail = detail

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=400,
        content={"error": exc.name, "detail": exc.detail},
    )

@app.get("/error")
def trigger_error():
    raise CustomException(name="CustomError", detail="Something went wrong")
```

### Fix 5: Use APIRouter for Modular Routes
Organize routes into separate routers to avoid conflicts.
```python
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter(prefix="/api/v1", tags=["items"])

@router.get("/items")
def list_items():
    return {"items": []}

@router.post("/items")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

app.include_router(router)
```

## Examples

```python
# Complete FastAPI application with error handling
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI(title="User API")

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(request: CreateUserRequest):
    if request.age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Age must be positive",
        )
    user = {"id": 1, "name": request.name, "email": request.email}
    return user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return {"id": user_id, "name": "John", "email": "john@example.com"}
```

## Related Errors

- [Python Pydantic Error](/languages/python/python-pydantic-error/)
- [Python Loguru Error](/languages/python/python-loguru-error/)
- [Python pytest Error](/languages/python/python-pytest-error-extended/)
