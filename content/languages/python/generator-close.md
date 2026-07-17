---
title: "[Solution] Python GeneratorExit — Generator Closed"
description: "Fix Python GeneratorExit when a generator is closed unexpectedly. Learn why generators close and how to handle GeneratorExit properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# GeneratorExit — Generator Closed

A `GeneratorExit` exception is raised when a generator or coroutine is closed without being fully consumed. This typically happens when you call `.close()` on a generator, or when the garbage collector collects a generator that hasn't been exhausted.

## Description

When a generator is closed, Python sends a `GeneratorExit` exception into the generator at the point where it is suspended at a `yield` statement. If the generator catches this exception and tries to yield another value, a `RuntimeError` is raised. The generator should either re-raise the exception or simply return.

Common patterns:

- **Calling .close() on a generator** — explicitly closing a partially consumed generator.
- **Garbage collection of generators** — unreferenced generators are closed during cleanup.
- **Using `with` statement on generators** — context managers may close generators.
- **Break in a for loop** — exiting a loop over a generator early.

## Common Causes

```python
# Cause 1: Calling .close() on a generator
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
next(gen)  # Returns 1
gen.close()  # Generator is closed

# Cause 2: Breaking out of a generator loop
def my_generator():
    yield 1
    yield 2
    yield 3
    print("Generator finished")

for value in my_generator():
    if value == 2:
        break  # Generator is closed, "Generator finished" never prints

# Cause 3: Generator catching GeneratorExit improperly
def bad_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        yield "cleanup"  # RuntimeError: generator already executing

# Cause 4: Forgetting to consume a generator
def my_generator():
    yield 1
    yield 2

gen = my_generator()
# Generator is never consumed, will be closed during garbage collection
```

## Solutions

### Fix 1: Allow generators to close gracefully

```python
# Wrong — catching GeneratorExit and yielding
def bad_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        yield "cleanup"  # RuntimeError!

# Correct — catch and return (or do cleanup without yielding)
def good_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Generator was closed")
        return  # Don't yield after GeneratorExit
```

### Fix 2: Use try/finally for cleanup

```python
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator cleanup: releasing resources")

# Resources are cleaned up whether generator is consumed or closed
for value in my_generator():
    if value == 2:
        break
# Prints: Generator cleanup: releasing resources
```

### Fix 3: Consume the generator fully when needed

```python
def my_generator():
    yield 1
    yield 2
    yield 3
    print("Generator finished")

# Wrong — not consuming all values
gen = my_generator()
next(gen)  # Only gets 1

# Correct — consume all values
list(my_generator())  # Prints "Generator finished"
```

### Fix 4: Use context managers for resource cleanup

```python
from contextlib import contextmanager

@contextmanager
def my_generator():
    print("Acquiring resource")
    try:
        yield 1
        yield 2
    finally:
        print("Releasing resource")

with my_generator() as value:
    print(value)
# Always prints "Releasing resource"
```

## Related Errors

- [RuntimeError](../runtimeerror) — generator already executing.
- [StopIteration](../stopiteration) — iterator exhausted.
- [RecursionError](../recursionerror) — maximum recursion depth exceeded.
