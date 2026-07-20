---
title: "[Solution] Python StopAsyncIteration — Async Iterator Exhausted"
description: "Fix Python StopAsyncIteration in async iterators, __anext__, and async for loops. Properly implement async iteration protocol with correct exception handling."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 25
---

# Python StopAsyncIteration — Async Iterator Exhausted

A `StopAsyncIteration` is raised when an async iterator's `__anext__()` method has no more items to yield. It is the async equivalent of `StopIteration` and signals the end of asynchronous iteration. If it propagates out of `__anext__()` uncaught, it breaks `async for` loops.

## Common Causes

```python
# Cause 1: __anext__ raises StopAsyncIteration directly
class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        self.current += 1
        return self.current

# Cause 2: Forgetting to define __aiter__
class AsyncReader:
    async def __anext__(self):
        data = await read_chunk()
        if not data:
            raise StopAsyncIteration
        return data
    # Missing __aiter__ — async for loop fails

# Cause 3: Async generator yielding and raising StopAsyncIteration
async def bad_async_gen():
    yield 1
    yield 2
    raise StopAsyncIteration  # Wrong — 'return' should be used instead

# Cause 4: Wrapper intercepting StopAsyncIteration incorrectly
class AsyncFilter:
    def __init__(self, source):
        self.source = source

    async def __anext__(self):
        try:
            return await self.source.__anext__()
        except StopAsyncIteration:
            raise  # Must re-raise — swallowing breaks async for

# Cause 5: Async iterator from a synchronous iterator missing protocol
class SyncAsAsync:
    def __init__(self, data):
        self.data = iter(data)
        self.idx = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            val = next(self.data)
        except StopIteration:
            raise StopAsyncIteration  # Must convert StopIteration
        return val
```

## How to Fix

### Fix 1: Use 'return' to end async generators instead of raising StopAsyncIteration

```python
# Wrong
async def bad_gen():
    yield 1
    raise StopAsyncIteration

# Correct
async def good_gen():
    yield 1
    yield 2
    return  # Cleanly signals end of iteration
```

### Fix 2: Implement the full async iterator protocol

```python
class AsyncRange:
    def __init__(self, stop):
        self.stop = stop
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        self.current += 1
        return self.current - 1

async def main():
    async for num in AsyncRange(5):
        print(num)  # 0, 1, 2, 3, 4
```

### Fix 3: Convert synchronous iterators for async use

```python
import asyncio

def sync_to_async_iter(sync_iter):
    """Wrap a synchronous iterable for use with async for."""
    class AsyncWrapper:
        def __init__(self, iterable):
            self._iter = iter(iterable)

        def __aiter__(self):
            return self

        async def __anext__(self):
            try:
                return next(self._iter)
            except StopIteration:
                raise StopAsyncIteration

    return AsyncWrapper(sync_iter)

async def main():
    async for item in sync_to_async_iter([1, 2, 3]):
        print(item)
```

### Fix 4: Handle StopAsyncIteration in custom async iterators

```python
class AsyncBatchReader:
    def __init__(self, source, batch_size=10):
        self.source = aiter(source)
        self.batch_size = batch_size

    def __aiter__(self):
        return self

    async def __anext__(self):
        batch = []
        for _ in range(self.batch_size):
            try:
                item = next(self.source)  # Wraps __anext__
                batch.append(item)
            except StopAsyncIteration:
                break
        if not batch:
            raise StopAsyncIteration
        return batch
```

### Fix 5: Use async for with proper exception handling

```python
import asyncio

async def process_stream(stream):
    results = []
    try:
        async for chunk in stream:
            results.append(chunk)
    except StopAsyncIteration:
        pass  # Stream exhausted — normal termination
    return results
```

## Prevention Checklist

- Use `return` (not `raise StopAsyncIteration`) to end async generators.
- Always implement both `__aiter__` and `__anext__` for async iterators.
- Convert `StopIteration` to `StopAsyncIteration` when wrapping synchronous iterators.
- Never swallow `StopAsyncIteration` inside `__anext__` — always re-raise it.
- Use `async for` loops instead of manual `__anext__()` calls when possible.

## Related Errors

- [StopIteration](/languages/python/stopiteration/) — synchronous iterator exhaustion.
- [RuntimeError](/languages/python/runtimeerror/) — generator raised StopIteration in Python 3.7+.
- [TypeError](/languages/python/typeerror/) — object is not async iterable.
- [AttributeError](/languages/python/attributeerror/) — missing `__aiter__` or `__anext__`.
