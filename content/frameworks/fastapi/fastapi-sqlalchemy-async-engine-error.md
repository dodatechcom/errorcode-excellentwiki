---
title: "[Solution] FastAPI SQLAlchemy Async Engine Error"
description: "Fix FastAPI SQLAlchemy async engine errors when database connections fail or async queries hang."
frameworks: ["fastapi"]
error-types: ["database-error"]
severities: ["error"]
---

When using SQLAlchemy's async engine with FastAPI, connection errors occur if the async driver is not installed or the engine is configured for synchronous use.

## Common Causes

- Using `sqlalchemy` instead of `asyncpg` or `aiosqlite` driver
- Engine created with `create_engine` instead of `create_async_engine`
- Connection pool not configured for async operation
- `expire_on_commit` causes lazy loading failures after commit
- Sessions used across multiple async tasks without proper scoping

## How to Fix

### Use Async Engine with Proper Driver

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/db"

engine = create_async_engine(DATABASE_URL, echo=True, pool_size=20)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
```

### Create Async Dependency

```python
from fastapi import Depends

async def get_db():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()
```

## Examples

```python
from sqlalchemy import create_engine  # Wrong -- sync engine

# This will hang or fail with async FastAPI
engine = create_engine("postgresql+asyncpg://localhost/db")
```

```python
from sqlalchemy.ext.asyncio import create_async_engine  # Correct

engine = create_async_engine("postgresql+asyncpg://localhost/db")
```

Install the async driver: `pip install asyncpg` for PostgreSQL or `pip install aiosqlite` for SQLite.
