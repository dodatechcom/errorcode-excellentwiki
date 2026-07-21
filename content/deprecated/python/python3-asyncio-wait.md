---
title: "[Solution] Deprecated Function Migration: asyncio.wait with coroutines to asyncio.gather"
description: "Migrate from deprecated asyncio.wait with raw coroutines to asyncio.gather."
deprecated_function: "asyncio.wait(coroutines)"
replacement_function: "asyncio.gather(*tasks)"
languages: ["python"]
deprecated_since: "Python 3.8+"
---

# [Solution] Deprecated Function Migration: asyncio.wait with coroutines to asyncio.gather

The `asyncio.wait(coroutines)` has been deprecated in favor of `asyncio.gather(*tasks)`.

## Migration Guide

asyncio.wait requires Tasks/Futures, not raw coroutines

asyncio.wait with raw coroutines was deprecated in Python 3.8. Use asyncio.gather for collecting results.

## Before (Deprecated)

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    return url

# Deprecated
tasks = [fetch(url) for url in urls]
done, pending = await asyncio.wait(tasks)
```

## After (Modern)

```python
import asyncio

results = await asyncio.gather(
    fetch(url1),
    fetch(url2),
    fetch(url3)
)

# With error handling
try:
    results = await asyncio.gather(*tasks, return_exceptions=True)
except Exception as e:
    print(f"Error: {e}")
```

## Key Differences

- gather returns results in order
- wait returns done/pending sets
- gather is simpler for result collection
- Use create_task with wait for cancellation
