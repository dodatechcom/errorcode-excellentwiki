---
title: "[Solution] FastAPI Lifespan Error"
description: "Fix FastAPI lifespan errors when startup or shutdown events fail to execute or raise exceptions."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When using FastAPI's lifespan context manager, exceptions during startup or shutdown prevent the application from running or cleaning up resources.

## Common Causes

- Exception raised during database connection initialization
- Third-party service not available at startup time
- Missing required environment variables during startup
- Shutdown logic accesses already-closed resources
- Using both lifespan and deprecated `on_event` decorators simultaneously

## How to Fix

### Use Context Manager Lifespan

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await database.connect()
    yield
    # Shutdown
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
```

### Handle Startup Failures

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()
        logger.info("Database connected")
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise
    try:
        yield
    finally:
        await database.disconnect()
        logger.info("Database disconnected")

app = FastAPI(lifespan=lifespan)
```

## Examples

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Bug -- exception in startup prevents app from running
@asynccontextmanager
async def bad_lifespan(app):
    await connect_to_db()  # May raise if DB is down
    yield

# Fix -- wrap in try/except
@asynccontextmanager
async def good_lifespan(app):
    try:
        await connect_to_db()
    except Exception as e:
        print(f"Failed to connect: {e}")
        raise
    yield
```
