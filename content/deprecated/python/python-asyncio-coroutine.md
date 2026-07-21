---
title: "[Solution] Deprecated Function Migration: @asyncio.coroutine to async/await"
description: "Migrate from deprecated @asyncio.coroutine decorator to native async/await syntax in Python."
deprecated_function: "@asyncio.coroutine"
replacement_function: "async def"
languages: ["python"]
deprecated_since: "Python 3.8"
---

# [Solution] Deprecated Function Migration: @asyncio.coroutine to async/await

The `@asyncio.coroutine` has been deprecated in favor of `async def`.

## Migration Guide

@asyncio.coroutine was deprecated in Python 3.8 in favor of native async/await syntax.

## Before (Deprecated)

```python
import asyncio

@asyncio.coroutine
def fetch_data():
    data = yield from aiohttp.get("https://api.example.com")
    return data
```

## After (Modern)

```python
import asyncio
import aiohttp

async def fetch_data():
    async with aiohttp.get("https://api.example.com") as response:
        data = await response.json()
        return data
```

## Key Differences

- Replace @asyncio.coroutine with async def
- Replace yield from with await
- async/await is faster and cleaner
