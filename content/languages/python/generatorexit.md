---
title: "[Solution] Python GeneratorExit — Generator Cleanup Fix"
description: "Fix Python GeneratorExit when a generator or coroutine is closed prematurely. Handle cleanup in generators using try/finally and proper close() patterns."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# GeneratorExit — Generator Cleanup Fix

A `GeneratorExit` exception is raised when a generator's `close()` method is called or when it is garbage collected. It's used to signal that the generator should clean up and stop. Unlike other exceptions, it doesn't propagate out of the generator — the generator simply terminates.

## Description

`GeneratorExit` is a special exception that inherits from `BaseException` (not `Exception`). It's raised when:
- The generator's `.close()` method is called explicitly.
- The generator object is garbage collected without being fully consumed.
- A `break` in a `for` loop over a generator triggers cleanup.

When `GeneratorExit` is raised inside a generator, the generator should perform any necessary cleanup (closing files, releasing resources) and then return. If a generator raises `GeneratorExit` instead of returning, it's silently ignored.

Common scenarios:

- **Explicitly closing a generator** — `gen.close()`.
- **Garbage collection** — generator not fully consumed, gets collected.
- **Break in for loop** — exiting early from iteration.
- **Coroutine cancellation** — `asyncio` task cancellation raises `GeneratorExit`.

## Common Causes

```python
# Cause 1: Calling close() on a generator
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Cleanup!")

gen = my_generator()
next(gen)  # Yields 1
gen.close()  # Raises GeneratorExit, triggers finally block

# Cause 2: Garbage collection of unfinished generator
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Cleanup!")

gen = my_generator()
next(gen)  # Yields 1
del gen  # Garbage collected, GeneratorExit raised

# Cause 3: Break in for loop
def my_generator():
    try:
        for i in range(10):
            yield i
    finally:
        print("Cleanup!")

for i in my_generator():
    if i == 3:
        break  # GeneratorExit raised, cleanup runs

# Cause 4: Coroutine cancellation
import asyncio

async def my_coroutine():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Coroutine cancelled")

async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(0.1)
    task.cancel()  # Raises GeneratorExit in coroutine
```

## Solutions

### Fix 1: Use try/finally for cleanup in generators

```python
# Wrong — no cleanup when generator is closed
def read_files(file_list):
    for filename in file_list:
        f = open(filename)
        yield f.read()
        f.close()  # May never execute if generator is closed early

# Correct — use try/finally for guaranteed cleanup
def read_files(file_list):
    files = []
    try:
        for filename in file_list:
            f = open(filename)
            files.append(f)
            yield f.read()
    finally:
        for f in files:
            f.close()
```

### Fix 2: Handle GeneratorExit explicitly in generators

```python
# Wrong — generator doesn't handle early termination
def process_data():
    while True:
        data = get_data()
        yield process(data)

# Correct — handle GeneratorExit for graceful shutdown
def process_data():
    try:
        while True:
            data = get_data()
            yield process(data)
    except GeneratorExit:
        print("Generator closed, cleaning up...")
        cleanup_resources()
        return  # Return normally instead of raising
```

### Fix 3: Use context managers for resource management

```python
from contextlib import contextmanager

# Wrong — manual resource management
def my_generator():
    conn = create_connection()
    data = conn.query("SELECT * FROM users")
    yield data
    conn.close()  # May not execute

# Correct — context manager ensures cleanup
@contextmanager
def managed_connection():
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()

def my_generator():
    with managed_connection() as conn:
        data = conn.query("SELECT * FROM users")
        yield data
```

### Fix 4: Use weakref.finalize for guaranteed cleanup

import weakref

# Wrong — cleanup may not happen
def my_generator():
    resource = acquire_resource()
    yield process(resource)
    release_resource(resource)  # May not execute

# Correct — weakref.finalize ensures cleanup
def my_generator():
    resource = acquire_resource()
    finalizer = weakref.finalize(resource, release_resource, resource)
    try:
        yield process(resource)
    finally:
        finalizer()  # Explicitly call cleanup

### Fix 5: Handle GeneratorExit in async generators

```python
import asyncio

# Wrong — no cleanup on cancellation
async def async_generator():
    while True:
        data = await fetch_data()
        yield data

# Correct — handle cancellation gracefully
async def async_generator():
    try:
        while True:
            data = await fetch_data()
            yield data
    except asyncio.CancelledError:
        await cleanup_async_resources()
        raise  # Re-raise after cleanup
```

## Related Errors

- [StopIteration](../stopiteration) — iterator exhausted normally.
- [RuntimeError](../runtimeerror) — generator already executing.
- [KeyboardInterrupt](#) — user interrupt (also inherits from BaseException).
