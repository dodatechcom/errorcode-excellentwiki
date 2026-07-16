---
title: "[Solution] Python SyntaxError — 'yield' Outside Function"
description: "Fix Python SyntaxError when using yield outside a function. Learn why yield must be inside a function and how to use generators correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "yield", "generator", "function"]
weight: 5
---

# SyntaxError — 'yield' Outside Function

A `SyntaxError` with the message "'yield' outside function" is raised when you use the `yield` keyword outside of a function body. `yield` can only be used inside a function to create a generator.

## Description

The `yield` keyword is used in functions to create generators. When `yield` is encountered, the function's execution is paused and the value is returned to the caller. The function can be resumed later. Using `yield` at the module level or inside a class body (outside a method) causes a `SyntaxError`.

Common patterns:

- **yield at module level** — `yield 5` outside any function.
- **yield in class body** — `yield` inside a class but outside a method.
- **yield in lambda** — `lambda: yield 5`.
- **yield in comprehension** — `yield` inside a list comprehension (Python 2 only).

## Common Causes

```python
# Cause 1: yield at module level
yield 5  # SyntaxError: 'yield' outside function

# Cause 2: yield in class body
class MyClass:
    yield 5  # SyntaxError

# Cause 3: yield in lambda
my_func = lambda: yield 5  # SyntaxError

# Cause 4: yield in comprehension (Python 2)
result = [yield x for x in range(5)]  # SyntaxError in Python 2
```

## Solutions

### Fix 1: Put yield inside a function

```python
# Wrong
yield 5  # SyntaxError

# Correct
def my_generator():
    yield 5
    yield 6
    yield 7

# Use the generator
for value in my_generator():
    print(value)
```

### Fix 2: Use yield in a method

```python
# Wrong
class MyClass:
    yield 5  # SyntaxError

# Correct
class MyClass:
    def my_method(self):
        yield 5
        yield 6
```

### Fix 3: Use return with value instead of yield in non-generator functions

```python
# Wrong
def not_a_generator():
    yield 5  # SyntaxError — function must be a generator

# Correct — use return instead
def not_a_generator():
    return 5

# Or make it a proper generator
def my_generator():
    yield 5
```

### Fix 4: Use yield from for delegation

```python
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield from sub_generator()
    yield 3

list(main_generator())  # [1, 2, 3]
```

## Related Errors

- [SyntaxError: 'yield from' outside function](yield-from) — yield from outside function.
- [SyntaxError: 'async' outside function](async-await) — async outside function.
- [GeneratorExit](generator-close) — generator closed unexpectedly.
