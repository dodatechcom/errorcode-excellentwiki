---
title: "[Solution] Python SyntaxError — 'await' Outside Async Function"
description: "Fix Python SyntaxError when using await outside an async function. Learn about await syntax and how to use it correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "await", "async", "coroutine"]
weight: 5
---

# SyntaxError — 'await' Outside Async Function

A `SyntaxError` with the message "'await' outside async function" is raised when you use the `await` keyword outside of an `async def` function. `await` can only be used inside asynchronous functions.

## Description

The `await` keyword is used to pause execution of an async function until the awaited coroutine completes. It can only be used inside `async def` functions. Using `await` in a regular function or at the module level causes a `SyntaxError`.

Common patterns:

- **await in regular function** — `await coroutine()` in a `def` function.
- **await at module level** — `await coroutine()` outside any function.
- **await in class body** — `await` inside a class but outside an async method.
- **Missing async def** — forgetting to make the function async.

## Common Causes

```python
# Cause 1: await in regular function
def greet():
    await asyncio.sleep(1)  # SyntaxError: 'await' outside async function

# Cause 2: await at module level
await asyncio.sleep(1)  # SyntaxError

# Cause 3: await in class body
class MyClass:
    await asyncio.sleep(1)  # SyntaxError

# Cause 4: Missing async keyword
def process():
    result = await some_coroutine()  # SyntaxError
```

## Solutions

### Fix 1: Make the function async

```python
# Wrong
def greet():
    await asyncio.sleep(1)  # SyntaxError

# Correct
async def greet():
    await asyncio.sleep(1)
```

### Fix 2: Put await inside async function

```python
# Wrong
await asyncio.sleep(1)  # SyntaxError

# Correct
async def main():
    await asyncio.sleep(1)

asyncio.run(main())
```

### Fix 3: Use async methods in classes

```python
# Wrong
class MyClass:
    def process(self):
        await some_coroutine()  # SyntaxError

# Correct
class MyClass:
    async def process(self):
        await some_coroutine()
```

### Fix 4: Run async code properly

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done")

# Wrong — can't await in regular code
# await main()  # SyntaxError

# Correct
asyncio.run(main())
```

## Related Errors

- [SyntaxError: 'async' outside function](async-await) — async outside function.
- [SyntaxError: 'yield' outside function](yield-outside-function) — yield outside function.
- [SyntaxError](../syntaxerror) — general syntax errors.
