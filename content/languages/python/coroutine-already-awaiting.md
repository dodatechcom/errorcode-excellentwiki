---
title: "[Solution] Python RuntimeError — coroutine already being awaited"
description: "Fix Python RuntimeError: coroutine already being awaited. Learn how to avoid double awaiting coroutines and manage async tasks properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 703
---

# Python RuntimeError — coroutine already being awaited

A `RuntimeError` with the message `coroutine '...' is being awaited` or `coroutine already being awaited` is raised when you try to `await` a coroutine that is already being awaited by another coroutine or event loop. A coroutine can only be awaited once — attempting to await it again causes this error.

## Common Causes

```python
import asyncio

# Cause 1: Double awaiting the same coroutine
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    coro = fetch_data()
    result1 = await coro  # First await works
    result2 = await coro  # RuntimeError: coroutine already being awaited

asyncio.run(main())

# Cause 2: Awaiting a coroutine that's already scheduled as a task
async def background():
    await asyncio.sleep(5)

async def main():
    coro = background()
    task = asyncio.create_task(coro)  # Task is now running
    result = await coro  # RuntimeError: coroutine already being awaited

asyncio.run(main())

# Cause 3: Sharing a coroutine between two event loops
async def worker():
    await asyncio.sleep(1)
    return "done"

async def main():
    coro = worker()
    result = await coro  # First event loop awaits it

loop2 = asyncio.new_event_loop()
loop2.run_until_complete(coro)  # RuntimeError: coroutine already being awaited

# Cause 4: Awaiting in multiple concurrent tasks
async def fetch(url):
    await asyncio.sleep(1)
    return url

async def main():
    coro = fetch("http://example.com")
    # Wrong — both tasks try to await the same coroutine
    task1 = asyncio.create_task(coro)
    task2 = asyncio.create_task(coro)  # RuntimeError

asyncio.run(main())
```

## How to Fix

### Fix 1: Create separate coroutines for each await

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    # Wrong — reusing the same coroutine
    coro = fetch_data()
    result1 = await coro
    result2 = await coro  # Error

    # Correct — call the function again to create a new coroutine
    result1 = await fetch_data()
    result2 = await fetch_data()

asyncio.run(main())
```

### Fix 2: Use asyncio.create_task for concurrent execution

```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # Correct — create separate tasks
    task1 = asyncio.create_task(fetch_data("http://a.com"))
    task2 = asyncio.create_task(fetch_data("http://b.com"))

    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())
```

### Fix 3: Use asyncio.gather for multiple coroutines

```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # Correct — gather creates tasks internally
    results = await asyncio.gather(
        fetch_data("http://a.com"),
        fetch_data("http://b.com"),
        fetch_data("http://c.com"),
    )
    print(results)

asyncio.run(main())
```

### Fix 4: Don't pass coroutines to event loops that already ran them

```python
import asyncio

async def worker():
    await asyncio.sleep(1)
    return "done"

async def main():
    result = await worker()  # Correct — await in the same loop

asyncio.run(main())
# Don't try to run the same coroutine in another loop
```

## Examples

```python
# Real-world: Web scraper with multiple concurrent requests
import asyncio
import aiohttp

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    async with aiohttp.ClientSession() as session:
        # Correct — create separate coroutines
        tasks = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        print(f"Fetched {len(pages)} pages")

asyncio.run(main())

# Real-world: Managing a shared database connection
import asyncio

class Database:
    def __init__(self):
        self.connection = None

    async def connect(self):
        await asyncio.sleep(0.5)  # Simulate connection
        self.connection = True

    async def query(self, sql):
        if not self.connection:
            await self.connect()
        return f"Results for: {sql}"

async def main():
    db = Database()

    # Correct — create a single connection task
    connect_task = asyncio.create_task(db.connect())
    await connect_task

    # Now query multiple times
    results = await asyncio.gather(
        db.query("SELECT 1"),
        db.query("SELECT 2"),
    )
    print(results)

asyncio.run(main())
```

## Related Errors

- [Async/await errors](async-await) — general async/await issues.
- [asyncio errors](asyncio-error) — asyncio event loop errors.
- [RuntimeError](../runtimeerror) — general runtime errors.
