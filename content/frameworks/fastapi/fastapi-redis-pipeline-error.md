---
title: "[Solution] FastAPI Redis Pipeline Error"
description: "Fix FastAPI Redis pipeline errors when batch operations fail or produce inconsistent results."
frameworks: ["fastapi"]
error-types: ["cache-error"]
severities: ["error"]
---

When using Redis pipelines in FastAPI for batch operations, errors occur if the pipeline is not properly managed.

## Common Causes

- Pipeline not using `execute()` to run commands
- Transaction pipeline aborted due to WATCH key changes
- Pipeline connection is closed before execute
- Mixed async and sync pipeline usage
- Pipeline command exceeds Redis max command buffer

## How to Fix

### Use Async Pipeline Correctly

```python
from fastapi import FastAPI
import redis.asyncio as redis

app = FastAPI()
r = redis.Redis()

@app.post("/batch-set")
async def batch_set(data: dict):
    async with r.pipeline(transaction=True) as pipe:
        for key, value in data.items():
            pipe.set(key, value)
        results = await pipe.execute()
    return {"results": results}
```

### Handle Pipeline Errors

```python
@app.post("/safe-batch")
async def safe_batch(data: dict):
    try:
        async with r.pipeline() as pipe:
            for key, value in data.items():
                pipe.setex(key, 3600, value)
            results = await pipe.execute()
        return {"count": len(results)}
    except redis.RedisError as e:
        return {"error": str(e)}
```

## Examples

```python
import redis.asyncio as redis

r = redis.Redis()

# Bug -- not executing the pipeline
async def broken_pipeline():
    pipe = r.pipeline()
    pipe.set("key1", "value1")
    pipe.set("key2", "value2")
    # Missing await pipe.execute()

# Fix
async def working_pipeline():
    async with r.pipeline() as pipe:
        pipe.set("key1", "value1")
        pipe.set("key2", "value2")
        await pipe.execute()
```

Always call `execute()` or use the context manager to run queued commands.
