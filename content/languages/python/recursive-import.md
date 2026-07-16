---
title: "[Solution] Python RecursionError — Maximum Recursion Depth Exceeded"
description: "Fix Python RecursionError caused by infinite or excessive recursion. Learn why recursion limits exist and how to optimize recursive code."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["recursionerror", "recursion", "stack", "depth"]
weight: 5
---

# RecursionError — Maximum Recursion Depth Exceeded

A `RecursionError` with the message "maximum recursion depth exceeded" is raised when a function calls itself too many times without reaching a base case. Python has a default recursion limit (usually 1000) to prevent stack overflow.

## Description

Recursion occurs when a function calls itself. Each recursive call adds a frame to the call stack. Python limits recursion depth to prevent stack overflow. When the limit is exceeded, `RecursionError` is raised. This can also happen with circular imports or infinite loops that indirectly call themselves.

Common patterns:

- **Missing base case** — function always calls itself.
- **Wrong base case** — base case never triggers.
- **Infinite mutual recursion** — two functions calling each other.
- **Circular imports** — modules importing each other create infinite recursion.

## Common Causes

```python
# Cause 1: Missing base case
def factorial(n):
    return n * factorial(n - 1)  # Never stops — RecursionError

# Cause 2: Wrong base case
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n + 1)  # n increases — never reaches 0

# Cause 3: Infinite mutual recursion
def func_a():
    return func_b()

def func_b():
    return func_a()  # Infinite recursion

# Cause 4: Circular import causing recursion
# module_a.py imports module_b.py
# module_b.py imports module_a.py
```

## Solutions

### Fix 1: Add a proper base case

```python
# Wrong
def factorial(n):
    return n * factorial(n - 1)

# Correct
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)
```

### Fix 2: Convert recursion to iteration

```python
# Wrong — recursive
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Correct — iterative
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Fix 3: Use memoization for repeated calculations

```python
# Without memoization — exponential time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# With memoization — linear time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Fix 4: Increase recursion limit (use cautiously)

```python
import sys

# Default limit
print(sys.getrecursionlimit())  # Usually 1000

# Increase limit (use with caution)
sys.setrecursionlimit(10000)

# Better: convert to iteration
```

## Related Errors

- [Import circular](import-circular) — circular imports causing recursion.
- [RuntimeError](../runtimeerror) — general runtime errors.
- [Stack overflow](#) — system-level stack overflow.
