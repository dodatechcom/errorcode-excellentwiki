---
title: "[Solution] Deprecated Function Migration: asyncio.ensure_future to asyncio.create_task"
description: "Migrate from deprecated asyncio.ensure_future to asyncio.create_task."
deprecated_function: "asyncio.ensure_future(coro)"
replacement_function: "asyncio.create_task(coro)"
languages: ["python"]
deprecated_since: "Python 3.7+"
---

# [Solution] Deprecated Function Migration: asyncio.ensure_future to asyncio.create_task

The `asyncio.ensure_future(coro)` has been deprecated in favor of `asyncio.create_task(coro)`.

## Migration Guide

create_task is more explicit and readable

asyncio.ensure_future was the standard way. create_task is the modern replacement.

## Before (Deprecated)

```python
import asyncio
async def main():
    task = asyncio.ensure_future(fetch_data())
```

## After (Modern)

```python
import asyncio
async def main():
    task = asyncio.create_task(fetch_data())
```

## Key Differences

- create_task is more explicit
- ensure_future still works for Futures
- create_task is the preferred API
- More readable intent
