---
title: "[Solution] FastAPI Test Async Client Error"
description: "Fix FastAPI test async client errors when using AsyncClient with TestClient or mixing sync and async test modes."
frameworks: ["fastapi"]
error-types: ["test-error"]
severities: ["error"]
---

When testing FastAPI endpoints with `httpx.AsyncClient`, mixing synchronous `TestClient` and async patterns causes event loop conflicts.

## Common Causes

- Using `AsyncClient` in a synchronous test function without `pytest-asyncio`
- Mixing `TestClient` (sync) and `AsyncClient` (async) in the same test module
- Not using the `lifespan` parameter when async setup is needed
- Forgetting to close the `AsyncClient` response properly
- Running sync and async tests in the wrong order

## How to Fix

### Use pytest-asyncio for Async Tests

```python
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users", json={"name": "Alice"})
        assert response.status_code == 200
```

### Use Sync Client for Simple Tests

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_simple_endpoint():
    response = client.get("/ping")
    assert response.status_code == 200
```

## Examples

```python
# Wrong -- AsyncClient in sync test causes RuntimeError
def test_fetch_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/data")
```

```python
# Correct -- async test with pytest.mark.asyncio
@pytest.mark.asyncio
async def test_fetch_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/data")
        assert response.status_code == 200
```
