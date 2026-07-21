---
title: "[Solution] FastAPI Asyncio Task Cancel Error"
description: "Fix FastAPI asyncio task cancellation errors when background tasks or concurrent operations are interrupted."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When FastAPI cancels asyncio tasks during shutdown or when clients disconnect, running tasks raise `asyncio.CancelledError`.

## Common Causes

- Application shutdown cancels running background tasks
- Client disconnect triggers cancellation of in-progress operations
- `asyncio.wait_for` timeout cancels the underlying task
- Task groups cancel sibling tasks on failure
- Database transactions left open after cancellation

## How to Fix

### Handle CancelledError in Tasks

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

async def resilient_task():
    try:
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled -- cleaning up")
        raise
```

### Use Shield for Critical Operations

```python
async def critical_operation():
    try:
        await asyncio.shield(save_important_data())
    except asyncio.CancelledError:
        pass
```

### Clean Up Resources in Finally

```python
async def safe_task():
    db = await get_connection()
    try:
        await db.execute("UPDATE users SET active = true")
    except asyncio.CancelledError:
        await db.rollback()
        raise
    finally:
        await db.close()
```

## Examples

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

async def long_running_task():
    # Bug -- no cancellation handling
    for i in range(100):
        await asyncio.sleep(1)
        print(f"Step {i}")

# Fix -- handle cancellation
async def safe_long_task():
    for i in range(100):
        try:
            await asyncio.sleep(1)
            print(f"Step {i}")
        except asyncio.CancelledError:
            print(f"Cancelled at step {i}")
            raise
```

During shutdown, FastAPI cancels all running tasks. Always handle `CancelledError` to clean up resources.
