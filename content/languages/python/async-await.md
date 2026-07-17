---
title: "[Solution] Python SyntaxError — 'async' Outside Function"
description: "Fix Python SyntaxError when using async outside a function. Learn about async/await syntax and how to use async functions correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 5
---

# SyntaxError — 'async' Outside Function

A `SyntaxError` with the message "'async' outside function" is raised when you use the `async` keyword outside of a function body. `async` can only be used to define asynchronous functions or asynchronous context managers/for loops inside functions.

## Description

The `async` keyword is used to define asynchronous functions (coroutines) in Python 3.5+. When used outside a function, it causes a `SyntaxError`. The `async def` syntax creates a coroutine that can be awaited using `await`.

Common patterns:

- **async at module level** — `async print_hello()` outside any function.
- **async in class body** — `async` inside a class but outside a method.
- **async for without function** — `async for` outside a function.
- **async with without function** — `async with` outside a function.

## Common Causes

```python
# Cause 1: async at module level
async def greet():  # This is fine — but if you write:
async for x in aiter():  # SyntaxError if outside function
    pass

# Cause 2: async for outside function
async for x in aiter():  # SyntaxError: 'async for' outside function
    print(x)

# Cause 3: async with outside function
async with aiohttp.ClientSession() as session:  # SyntaxError if outside function
    pass

# Cause 4: Using async as a variable name (Python 3.7+)
async = 5  # SyntaxError in Python 3.7+
```

## Solutions

### Fix 1: Put async code inside an async function

```python
# Wrong
async for x in aiter():  # SyntaxError
    print(x)

# Correct
async def process():
    async for x in aiter():
        print(x)
```

### Fix 2: Use async def for async functions

```python
# Wrong
async def greet():  # This is correct syntax
    pass

# If you meant:
def greet():
    async for x in aiter():  # SyntaxError
        print(x)

# Correct
async def greet():
    async for x in aiter():
        print(x)
```

### Fix 3: Don't use async as a variable name

```python
# Wrong (Python 3.7+)
async = 5  # SyntaxError

# Correct
is_async = 5
```

### Fix 4: Run async functions with asyncio

```python
import asyncio

async def main():
    async for x in aiter():
        print(x)

asyncio.run(main())
```

## Related Errors

- [SyntaxError: 'await' outside async function](await-outside-async) — await outside async.
- [SyntaxError: 'yield' outside function](yield-outside-function) — yield outside function.
- [SyntaxError](../syntaxerror) — general syntax errors.
