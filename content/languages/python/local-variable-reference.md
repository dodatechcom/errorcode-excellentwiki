---
title: "[Solution] Python UnboundLocalError — Local Variable Referenced Before Assignment"
description: "Fix Python UnboundLocalError when a local variable is referenced before assignment. Learn why this happens and how to fix variable scoping issues."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnboundLocalError — Local Variable Referenced Before Assignment

An `UnboundLocalError` with the message "local variable 'X' referenced before assignment" is raised when you try to use a variable inside a function before it has been assigned a value within that function's scope. This commonly happens when a variable is assigned inside a function but used before the assignment statement is reached.

## Description

Python determines variable scope at compile time. If a variable is assigned anywhere inside a function, Python treats it as a local variable throughout the entire function. If you reference this variable before the assignment statement, even if it exists in an outer scope, Python raises an `UnboundLocalError`.

Common patterns:

- **Assignment after usage** — using a variable before the assignment line.
- **Conditional assignment** — variable is only assigned in some code paths.
- **Global keyword confusion** — forgetting to use `global` for module-level variables.
- **Loop variable scope** — variable defined in a loop used after the loop.

## Common Causes

```python
# Cause 1: Assignment after usage
def func():
    print(x)  # UnboundLocalError
    x = 10

# Cause 2: Conditional assignment
def func(condition):
    if condition:
        value = 42
    print(value)  # UnboundLocalError if condition is False

# Cause 3: Forgetting global keyword
counter = 0
def increment():
    counter += 1  # UnboundLocalError — Python thinks counter is local
    return counter

# Cause 4: Variable in try/except
def func():
    try:
        value = int("abc")
    except ValueError:
        pass
    print(value)  # UnboundLocalError if exception occurred
```

## Solutions

### Fix 1: Initialize variables before use

```python
# Wrong
def func():
    print(x)  # UnboundLocalError
    x = 10

# Correct
def func():
    x = None  # Initialize first
    print(x)
    x = 10
```

### Fix 2: Use the global keyword when needed

```python
# Wrong
counter = 0
def increment():
    counter += 1  # UnboundLocalError
    return counter

# Correct
counter = 0
def increment():
    global counter
    counter += 1
    return counter
```

### Fix 3: Handle all code paths

```python
# Wrong
def func(condition):
    if condition:
        value = 42
    print(value)  # UnboundLocalError if condition is False

# Correct
def func(condition):
    value = None  # Default value
    if condition:
        value = 42
    print(value)
```

### Fix 4: Use nonlocal for nested functions

```python
# Wrong
def outer():
    x = 10
    def inner():
        x += 1  # UnboundLocalError
        return x
    return inner()

# Correct
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
```

### Fix 5: Initialize in try/except blocks

```python
# Wrong
def func():
    try:
        value = int("abc")
    except ValueError:
        pass
    print(value)  # UnboundLocalError

# Correct
def func():
    value = None  # Default
    try:
        value = int("abc")
    except ValueError:
        pass
    print(value)
```

## Related Errors

- [NameError](#) — variable name not defined at all.
- [Local variable reference](recv-reference) — similar scoping issue.
- [SyntaxError](../syntaxerror) — related scope syntax errors.
