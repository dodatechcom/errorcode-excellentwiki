---
title: "[Solution] FastAPI Async Dependency Error"
description: "Fix FastAPI async dependency injection errors when awaitable functions fail or return unexpected types."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When an async dependency function raises an exception or returns a non-awaitable value, FastAPI throws errors during request handling.

## Common Causes

- Mixing sync and async database drivers in dependencies
- Forgetting to `await` an async call inside an async dependency
- Returning a coroutine object instead of the resolved value
- Using synchronous ORM methods in async dependency functions
- Dependency function signature does not match expected parameter types

## How to Fix

### Use Async-Compatible Drivers

```python
from fastapi import Depends
import httpx

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()
```

### Await All Async Calls

```python
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

### Use Proper Async Session Management

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session
```

## Examples

```python
from fastapi import FastAPI, Depends
import asyncio

app = FastAPI()

async def slow_dependency():
    await asyncio.sleep(1)
    return {"status": "ready"}

@app.get("/process")
async def process(data: dict = Depends(slow_dependency)):
    return data
```

A common mistake is writing the dependency as a regular function that returns a coroutine:

```python
# Wrong -- this returns a coroutine, not the result
def broken_dependency():
    return asyncio.sleep(1)  # Missing await, wrong function type
```

The fix is to use `async def` and `await`:

```python
# Correct
async def working_dependency():
    await asyncio.sleep(1)
    return {"status": "ready"}
```
