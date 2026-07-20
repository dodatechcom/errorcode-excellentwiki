---
title: "[Solution] Python asyncio Error — Event Loop and Coroutine Issues"
description: "Fix asyncio errors by doing X, Y, Z. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 607
---

# Python asyncio Error — Event Loop and Coroutine Issues

asyncio errors involve event loop lifecycle, coroutine scheduling, task cancellation, and synchronization primitives. These typically surface when mixing synchronous and asynchronous code or managing task lifecycles.

## Common Causes

```python
# Cause 1: Running a coroutine without awaiting it
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return {"data": 42}

# Wrong — coroutine created but never awaited
result = fetch_data()  # RuntimeWarning: coroutine was never awaited
print(result)  # <coroutine object fetch_data at 0x...>
```

```python
# Cause 2: Closing the event loop while tasks are running
import asyncio

async def background_task():
    while True:
        await asyncio.sleep(1)

async def main():
    asyncio.create_task(background_task())

asyncio.run(main())  # Task gets cancelled when main() returns

# Wrong — manually closing loop
loop = asyncio.get_event_loop()
loop.close()  # Event loop closed — can't run more coroutines
```

```python
# Cause 3: CancelledError not handled properly
import asyncio

async def slow_task():
    await asyncio.sleep(100)
    return "done"

async def main():
    task = asyncio.create_task(slow_task())
    await asyncio.sleep(1)
    task.cancel()

    # Wrong — not awaiting the cancelled task
    result = await task  # CancelledError propagates

asyncio.run(main())
```

```python
# Cause 4: InvalidStateError when getting result of non-done task
import asyncio

async def worker():
    await asyncio.sleep(5)
    return 42

async def main():
    task = asyncio.create_task(worker())
    result = task.result()  # InvalidStateError: Task is not done yet

asyncio.run(main())
```

```python
# Cause 5: Mixing sync blocking code in async context
import asyncio
import time

async def main():
    time.sleep(5)  # Blocks the entire event loop!

    # Other coroutines starved for CPU time
    await asyncio.sleep(0)  # Yield control, but time.sleep already blocked

asyncio.run(main())
```

## How to Fix

### Fix 1: Always Await or Explicitly Fire-and-Forget Coroutines

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return {"data": 42}

async def main():
    # Properly awaited
    result = await fetch_data()
    print(result)

    # Fire-and-forget (when you intentionally don't need the result)
    asyncio.create_task(fetch_data())  # Runs in background

asyncio.run(main())
```

### Fix 2: Use Proper Task Cancellation with Cleanup

```python
import asyncio

async def slow_task():
    try:
        await asyncio.sleep(100)
        return "done"
    except asyncio.CancelledError:
        # Clean up resources before re-raising
        print("Task cancelled, cleaning up")
        raise  # Re-raise to properly mark task as cancelled

async def main():
    task = asyncio.create_task(slow_task())
    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled successfully")

asyncio.run(main())
```

### Fix 3: Check Task State Before Accessing Result

```python
import asyncio

async def worker():
    await asyncio.sleep(2)
    return 42

async def main():
    task = asyncio.create_task(worker())

    # Check state before accessing result
    if task.done():
        result = task.result()
    elif task.cancelled():
        print("Task was cancelled")
    else:
        print("Task still running, waiting...")
        result = await task

    print(f"Result: {result}")

asyncio.run(main())
```

### Fix 4: Use asyncio.to_thread for Blocking I/O

```python
import asyncio
import time

def blocking_io_operation():
    time.sleep(2)  # Simulates blocking I/O
    return "result"

async def main():
    # Offload blocking code to a thread
    result = await asyncio.to_thread(blocking_io_operation)
    print(result)

    # Or use loop.run_in_executor for more control
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, blocking_io_operation)

asyncio.run(main())
```

### Fix 5: Gather Tasks Properly with Error Handling

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    if "error" in url:
        raise ValueError(f"Failed to fetch {url}")
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "error_url", "url3"]

    # gather returns results in same order as input
    results = await asyncio.gather(
        *[fetch(url) for url in urls],
        return_exceptions=True  # Don't raise — return exception objects
    )

    for url, result in zip(urls, results):
        if isinstance(result, Exception):
            print(f"Failed: {url} — {result}")
        else:
            print(f"Success: {result}")

asyncio.run(main())
```

## Examples

```python
# Full async application with proper error handling
import asyncio
from dataclasses import dataclass
from typing import List

@dataclass
class TaskResult:
    task_name: str
    success: bool
    data: str | None = None
    error: str | None = None

async def fetch_url(name: str, delay: float, should_fail: bool = False) -> TaskResult:
    try:
        await asyncio.sleep(delay)
        if should_fail:
            raise ConnectionError(f"{name} failed")
        return TaskResult(task_name=name, success=True, data=f"Response from {name}")
    except asyncio.CancelledError:
        return TaskResult(task_name=name, success=False, error="Cancelled")
    except Exception as e:
        return TaskResult(task_name=name, success=False, error=str(e))

async def main():
    tasks = [
        fetch_url("fast", 0.5),
        fetch_url("slow", 2.0),
        fetch_url("failing", 1.0, should_fail=True),
        fetch_url("medium", 1.5),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            print(f"Unexpected error: {result}")
        elif result.success:
            print(f"OK: {result.task_name} — {result.data}")
        else:
            print(f"FAIL: {result.task_name} — {result.error}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Related Errors

- [Python BlockingIOError](/languages/python/blockingioerror/) — Blocking I/O in async context
- [Python TimeoutError](/languages/python/timeouterror/) — Timeout exceptions
- [Python RuntimeError](/languages/python/runtimeerror/) — Runtime errors
- [Python Celery Error](/languages/python/python-celery-error/) — Task queue errors
