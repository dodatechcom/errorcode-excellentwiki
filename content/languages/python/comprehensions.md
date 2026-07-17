---
title: "[Solution] Python SyntaxError — Positional Argument Follows Keyword Argument"
description: "Fix Python SyntaxError when positional arguments follow keyword arguments. Learn about function call syntax and argument ordering rules."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 5
---

# SyntaxError — Positional Argument Follows Keyword Argument

A `SyntaxError` with the message "positional argument follows keyword argument" is raised when you pass a positional argument after a keyword argument in a function call. Python requires all positional arguments to come before keyword arguments.

## Description

In Python function calls, arguments must be in this order: positional arguments, `*args`, keyword arguments, and `**kwargs`. Placing a positional argument after a keyword argument violates this rule and causes a `SyntaxError`.

Common patterns:

- **Positional after keyword** — `func(key=value, positional)`.
- **Mixed argument order** — `func(1, key=2, 3)`.
- **In function definition** — `def func(key, *args, positional):` (also invalid).
- **In comprehensions** — similar rules apply in generator expressions.

## Common Causes

```python
# Cause 1: Positional after keyword
def greet(name, greeting):
    return f"{greeting}, {name}!"

greet(name="Alice", "Hello")  # SyntaxError

# Cause 2: Mixed argument order
def func(a, b, c):
    pass

func(1, b=2, 3)  # SyntaxError

# Cause 3: In function definition
def func(key, *args, positional):  # SyntaxError
    pass

# Cause 4: In comprehension
result = [x for x in range(10) if x > 5 if x < 8]  # SyntaxError
```

## Solutions

### Fix 1: Put positional arguments first

```python
# Wrong
greet(name="Alice", "Hello")  # SyntaxError

# Correct
greet("Hello", name="Alice")
```

### Fix 2: Convert positional to keyword or vice versa

```python
# Wrong
func(1, b=2, 3)  # SyntaxError

# Correct — all keyword
func(a=1, b=2, c=3)

# Or all positional
func(1, 2, 3)
```

### Fix 3: Use *args for variable positional arguments

```python
# Wrong
def func(key, *args, positional):  # SyntaxError
    pass

# Correct
def func(key, *args, positional=None):
    pass
```

### Fix 4: Use / for positional-only parameters

```python
# Python 3.8+ — positional-only parameters
def func(a, b, /, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)  # Works
func(1, 2, 3, d=4)  # Works
func(a=1, b=2, c=3)  # SyntaxError — a and b are positional-only
```

## Related Errors

- [SyntaxError](../syntaxerror) — general syntax errors.
- [TypeError](../typeerror) — wrong number of arguments at runtime.
- [TypeError: method argument issues](method-argument) — method argument errors.
