---
title: "[Solution] Deprecated Function Migration: @asyncio.coroutine to async def"
description: "Migrate from deprecated @asyncio.coroutine to native async/await."
deprecated_function: "@asyncio.coroutine"
replacement_function: "async def"
languages: ["python"]
deprecated_since: "Python 3.8+"
---

# [Solution] Deprecated Function Migration: @asyncio.coroutine to async def

The `@asyncio.coroutine` has been deprecated in favor of `async def`.

## Migration Guide

Native async/await is faster and cleaner.

## Before (Deprecated)

```python
@asyncio.coroutine
def fetch():
    data = yield from aiohttp.get(url)
```

## After (Modern)

```python
async def fetch():
    async with aiohttp.get(url) as resp:
        data = await resp.json()
```

## Key Differences

- Replace @asyncio.coroutine with async def
- Replace yield from with await
