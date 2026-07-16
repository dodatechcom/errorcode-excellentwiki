---
title: "[Solution] Python RecursionError — Maximum Recursion Depth Fix"
description: "Fix Python RecursionError when maximum recursion depth exceeded. Increase sys.setrecursionlimit, convert to iteration, or use memoization."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["recursionerror", "recursion", "depth", "stack-overflow"]
weight: 75
---

# RecursionError — Maximum Recursion Depth Fix

A `RecursionError` is raised when a function calls itself too many times, exceeding Python's default recursion limit (usually 1000). This protects against infinite recursion and stack overflow.

## Description

Python has a default maximum recursion depth of 1000 (configurable via `sys.getrecursionlimit()`). Each recursive call adds a frame to the call stack. When the limit is hit, Python raises `RecursionError`. In some cases, the stack may actually overflow before the error is raised.

Common scenarios:

- **Missing or incorrect base case** — recursion never terminates.
- **Recursive case doesn't move toward base case** — infinite loop.
- **Deep but valid recursion** — traversing deeply nested structures.
- **Circular references** — object A references B which references A.
- **Default limit too low** — for legitimate deep recursion like tree traversal.

## Common Causes

```python
# Cause 1: Missing base case
def countdown(n):
    print(n)
    countdown(n - 1)  # RecursionError: no base case to stop

# Cause 2: Base case doesn't trigger
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
factorial(-5)  # Never reaches 0, infinite recursion

# Cause 3: Recursive case doesn't reduce problem size
def search(data, target):
    index = 0
    if data[index] == target:
        return index
    return search(data, target)  # Same arguments, infinite recursion

# Cause 4: Circular object references
class Node:
    def __init__(self):
        self.parent = None
a = Node()
b = Node()
a.parent = b
b.parent = a  # Circular reference

# Cause 5: Default limit too low for tree traversal
def traverse(node):
    if node:
        traverse(node.left)
        traverse(node.right)
# With 1000+ depth tree, hits default limit
```

## Solutions

### Fix 1: Add a proper base case

```python
# Wrong
def countdown(n):
    print(n)
    countdown(n - 1)

# Correct
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)
```

### Fix 2: Ensure base case is reachable

```python
# Wrong — negative numbers never reach 0
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Correct — handle all cases
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Fix 3: Increase recursion limit for legitimate deep recursion

```python
import sys

# Wrong — default limit too low
def traverse很深(node):
    # tree with 5000+ depth
    pass

# Correct — increase limit if needed
sys.setrecursionlimit(10000)
def traverse(node):
    if node:
        traverse(node.left)
        traverse(node.right)
```

### Fix 4: Convert recursion to iteration

```python
# Wrong — recursive Fibonacci hits limit for large n
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Correct — iterative approach
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Fix 5: Use memoization to reduce redundant calls

```python
from functools import lru_cache

# Wrong — exponential time, hits recursion limit
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Correct — memoized, O(n) time
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Fix 6: Use an explicit stack for deep traversal

```python
# Wrong — recursive DFS
def dfs(node, result=None):
    if result is None:
        result = []
    result.append(node.value)
    for child in node.children:
        dfs(child, result)
    return result

# Correct — iterative DFS with stack
def dfs(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        stack.extend(reversed(node.children))
    return result
```

## Related Errors

- [StackOverflowError](#) — OS-level stack overflow from too many frames.
- [MemoryError](../memoryerror) — recursion consuming too much memory.
- [RuntimeError](../runtimeerror) — generic runtime error.
