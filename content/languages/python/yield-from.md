---
title: "[Solution] Python SyntaxError — 'yield from' Outside Function"
description: "Fix Python SyntaxError when using yield from outside a function. Learn about yield from syntax and generator delegation."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "yield", "from", "generator", "delegation"]
weight: 5
---

# SyntaxError — 'yield from' Outside Function

A `SyntaxError` with the message "'yield from' outside function" is raised when you use the `yield from` expression outside of a function body. Like `yield`, `yield from` can only be used inside a function to create a generator.

## Description

`yield from` is used to delegate to a sub-generator. It yields all values from the sub-generator and can receive values sent to the generator via `send()`. Like `yield`, it can only be used inside a function body. Using it at the module level or inside a class body (outside a method) causes a `SyntaxError`.

Common patterns:

- **yield from at module level** — `yield from iterable` outside any function.
- **yield from in class body** — `yield from` inside a class but outside a method.
- **yield from in comprehension** — `yield from` inside a list comprehension.
- **Missing function wrapper** — forgetting to wrap in a `def` function.

## Common Causes

```python
# Cause 1: yield from at module level
yield from [1, 2, 3]  # SyntaxError: 'yield from' outside function

# Cause 2: yield from in class body
class MyClass:
    yield from [1, 2, 3]  # SyntaxError

# Cause 3: yield from in comprehension
result = [yield from x for x in [[1, 2], [3, 4]]]  # SyntaxError

# Cause 4: Missing function wrapper
def not_a_generator():
    pass

yield from not_a_generator()  # SyntaxError
```

## Solutions

### Fix 1: Put yield from inside a function

```python
# Wrong
yield from [1, 2, 3]  # SyntaxError

# Correct
def my_generator():
    yield from [1, 2, 3]
    yield from [4, 5, 6]

list(my_generator())  # [1, 2, 3, 4, 5, 6]
```

### Fix 2: Use yield from for generator delegation

```python
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield from sub_generator()  # Delegates to sub_generator
    yield 3

list(main_generator())  # [1, 2, 3]
```

### Fix 3: Use yield from for string iteration

```python
def char_generator():
    yield from "hello"  # Yields each character

list(char_generator())  # ['h', 'e', 'l', 'l', 'o']
```

### Fix 4: Use yield from in methods

```python
class MyClass:
    def __iter__(self):
        yield from [1, 2, 3]
        yield from [4, 5, 6]

list(MyClass())  # [1, 2, 3, 4, 5, 6]
```

## Related Errors

- [SyntaxError: 'yield' outside function](yield-outside-function) — yield outside function.
- [SyntaxError: 'async' outside function](async-await) — async outside function.
- [GeneratorExit](generator-close) — generator closed unexpectedly.
