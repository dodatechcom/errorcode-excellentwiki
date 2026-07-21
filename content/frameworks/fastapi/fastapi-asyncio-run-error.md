---
title: "[Solution] FastAPI Asyncio Run Error"
description: "Fix FastAPI asyncio.run errors when creating new event loops inside an already running application."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When calling `asyncio.run()` inside a running FastAPI application, a `RuntimeError` is raised because an event loop is already running.

## Common Causes

- Calling `asyncio.run()` in a sync route or dependency
- Using synchronous library that internally calls `asyncio.run()`
- Trying to create a new event loop in a running async context
- Mixing `await` and `asyncio.run()` in the same code path
- Third-party library uses `asyncio.run()` internally

## How to Fix

### Use `asyncio.get_event_loop()` Instead

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
async def get_data():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, synchronous_function)
    return {"result": result}
```

### Use `asyncio.to_thread` for Sync Functions

```python
import asyncio
import time

def blocking_operation():
    time.sleep(2)
    return "done"

@app.get("/process")
async def process():
    result = await asyncio.to_thread(blocking_operation)
    return {"result": result}
```

### Run Sync Code in Background

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

@app.get("/heavy")
async def heavy_task():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, compute_heavy)
    return {"result": result}
```

## Examples

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

# Bug -- asyncio.run() inside running loop
@app.get("/broken")
async def broken():
    result = asyncio.run(some_async_func())  # RuntimeError
    return {"result": result}

# Fix -- await directly
@app.get("/working")
async def working():
    result = await some_async_func()
    return {"result": result}
```

```text
RuntimeError: This event loop is already running
```

In async functions, use `await` directly. In sync functions, use `asyncio.run()` or `loop.run_until_complete()`.
