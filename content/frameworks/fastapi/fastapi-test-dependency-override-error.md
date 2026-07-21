---
title: "[Solution] FastAPI Test Dependency Override Error"
description: "Fix FastAPI test dependency override errors when overridden dependencies are not used during testing."
frameworks: ["fastapi"]
error-types: ["test-error"]
severities: ["error"]
---

When overriding dependencies for testing in FastAPI, the override may not take effect if the dependency graph is not correctly configured.

## Common Causes

- Override registered after TestClient makes the request
- Dependency is nested but only the top level is overridden
- Override function does not return the expected type
- Override not cleared between tests, causing test pollution
- Override uses wrong dependency key

## How to Fix

### Register Overrides Before Tests

```python
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

def get_db():
    return ProductionDB()

def get_current_user():
    return {"id": 1, "name": "Alice"}

@app.get("/me")
def read_me(user=Depends(get_current_user)):
    return user

# Override for testing
app.dependency_overrides[get_current_user] = lambda: {"id": 99, "name": "TestUser"}

client = TestClient(app)

def test_override():
    response = client.get("/me")
    assert response.json()["name"] == "TestUser"
```

### Clear Overrides Between Tests

```python
import pytest

@pytest.fixture(autouse=True)
def reset_overrides():
    yield
    app.dependency_overrides.clear()
```

### Override Nested Dependencies

```python
def get_db_override():
    return TestingDB()

def get_user_service_override():
    db = get_db_override()
    return UserService(db)

app.dependency_overrides[get_db] = get_db_override
app.dependency_overrides[UserService] = get_user_service_override
```

## Examples

```python
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

def real_auth():
    raise Exception("Should not be called in tests")

def test_auth():
    return {"id": 1, "name": "TestUser"}

@app.get("/protected")
def protected(user=Depends(real_auth)):
    return user

# Bug -- override not set up before client creation
client = TestClient(app)
# app.dependency_overrides[real_auth] = test_auth  # Too late!

# Fix -- set override first
app.dependency_overrides[real_auth] = test_auth
client = TestClient(app)

def test_protected():
    response = client.get("/protected")
    assert response.json()["name"] == "TestUser"
```
