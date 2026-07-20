---
title: "[Solution] Python 3.11 asyncio.TaskGroup Error — ExceptionGroup, Task Cancellation, Nursery"
description: "Fix Python 3.11 asyncio.TaskGroup errors including ExceptionGroup handling, task cancellation patterns, and structured concurrency."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 510
---

# Python 3.11 asyncio.TaskGroup Error — ExceptionGroup, Task Cancellation, Nursery

Python 3.11 added `asyncio.TaskGroup` as a structured concurrency primitive. Errors commonly occur when tasks raise exceptions that get wrapped in `ExceptionGroup`, when tasks are cancelled unexpectedly, or when using the nursery pattern incorrectly.

## Common Causes

```python
# Cause 1: Unhandled ExceptionGroup from TaskGroup
import asyncio

async def fail():
    raise ValueError("task failed")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fail())
        tg.create_task(fail())
    # ExceptionGroup raised here, not individual ValueError

# Cause 2: CancelledError propagation
async def main():
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(some_coroutine())
        task.cancel()  # May cause ExceptionGroup with CancelledError

# Cause 3: Missing await for TaskGroup tasks
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro_a())
        tg.create_task(coro_b())
    # Tasks run, but exceptions may be lost if not handled

# Cause 4: Nested TaskGroups without proper handling
async def main():
    async with asyncio.TaskGroup() as outer:
        outer.create_task(nested_task_group())

# Cause 5: TaskGroup used outside async context
with asyncio.TaskGroup() as tg:  # TypeError - must be used with async with
    tg.create_task(some_coroutine())
```

## How to Fix

### Fix 1: Catch ExceptionGroup from TaskGroup

```python
import asyncio
from asyncio import ExceptionGroup

async def fail(name):
    raise ValueError(f"{name} failed")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fail("task1"))
            tg.create_task(fail("task2"))
    except* ValueError as eg:
        print(f"Got {len(eg.exceptions)} value errors:")
        for exc in eg.exceptions:
            print(f"  {exc}")
```

### Fix 2: Handle task cancellation properly

```python
import asyncio

async def long_running():
    await asyncio.sleep(10)
    return "done"

async def main():
    task = None
    try:
        async with asyncio.TaskGroup() as tg:
            task = tg.create_task(long_running())
            await asyncio.sleep(1)  # Let it start
            task.cancel()  # Cancel the task
    except* asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())
```

### Fix 3: Use nursery pattern correctly

```python
import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")
    return name

async def main():
    results = []
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(worker("a", 1)),
            tg.create_task(worker("b", 2)),
            tg.create_task(worker("c", 0.5)),
        ]
    # All tasks complete here, results are in task objects
    for t in tasks:
        results.append(t.result())
    print(f"All done: {results}")

asyncio.run(main())
```

### Fix 4: Properly propagate exceptions from nested TaskGroups

```python
import asyncio
from asyncio import ExceptionGroup

async def inner_work():
    raise RuntimeError("inner failed")

async def outer_work():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(inner_work())
    except* RuntimeError as eg:
        print(f"Inner caught: {eg.exceptions}")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(outer_work())
            tg.create_task(inner_work())
    except* RuntimeError as eg:
        print(f"Outer caught {len(eg.exceptions)} errors")

asyncio.run(main())
```

### Fix 5: Use TaskGroup for proper structured concurrency

```python
import asyncio

async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(0.1)  # Simulate network
    return f"Response from {url}"

async def main():
    urls = ["http://a.com", "http://b.com", "http://c.com"]
    responses = []

    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch(url)) for url in urls]

    responses = [t.result() for t in tasks]
    print(f"Got {len(responses)} responses")

asyncio.run(main())
```

## Examples

```python
# Real-world: concurrent database queries
import asyncio
from asyncio import ExceptionGroup

async def query_db(conn, sql):
    await asyncio.sleep(0.05)  # Simulate query
    if "DROP" in sql:
        raise ValueError("Dangerous query rejected")
    return {"sql": sql, "rows": 42}

async def run_queries(connections, queries):
    results = []
    errors = []

    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(query_db(conn, sql))
            for conn, sql in zip(connections, queries)
        ]

    for task in tasks:
        try:
            results.append(task.result())
        except Exception as e:
            errors.append(e)

    return results, errors

# Retry pattern with TaskGroup
async def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await fetch(url)
        except Exception:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(0.1 * (attempt + 1))
```

## Related Errors

- [python-exception-group-error](../python-exception-group-error) — ExceptionGroup handling
- [asyncio-error](../asyncio-error) — General asyncio errors
- [await-outside-async](../await-outside-async) — Async context issues
- [CancelledError](../cancellederror) — Task cancellation
