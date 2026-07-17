---
title: "[Solution] Python UnboundLocalError: Local Variable Referenced Before Assignment"
description: "Fix Python UnboundLocalError: local variable 'X' referenced before assignment. Understand variable scope, initialization, and the LEGB rule."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# UnboundLocalError: Local Variable Referenced Before Assignment

An `UnboundLocalError: local variable 'X' referenced before assignment` is raised when you try to use a local variable before it has been assigned a value. This typically happens when a variable is used before being initialized, or when a global/enclosing scope variable is shadowed by a local assignment that occurs later in the function.

## Description

This error occurs when Python's runtime tries to read a variable in a local scope, but no assignment has been made to that variable within that scope. Common variants include:

- `UnboundLocalError: local variable 'x' referenced before assignment`
- `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`

Python resolves variable names at runtime using the LEGB rule (Local, Enclosing, Global, Built-in). If a variable is assigned anywhere in a function, Python treats it as local for the entire function.

## Common Causes

```python
# Cause 1: Using a variable before assignment
def example():
    print(x)  # UnboundLocalError: x not yet assigned
    x = 10

# Cause 2: Conditional assignment not covering all paths
def get_value(choice):
    if choice == "a":
        result = "apple"
    return result  # UnboundLocalError if choice != "a"

# Cause 3: Global variable shadowed by local assignment
count = 10
def increment():
    count = count + 1  # UnboundLocalError: local 'count' referenced before assignment
    return count

# Cause 4: Variable assigned only in exception handler
def risky_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        error = "division by zero"
    return result  # UnboundLocalError if exception was raised

# Cause 5: List comprehension variable leak (Python 2 style)
# In Python 3, comprehension variables don't leak, but this can still confuse
```

## How to Fix

### Fix 1: Initialize variables before use

```python
# Wrong
def example():
    print(x)
    x = 10

# Correct
def example():
    x = 10  # Initialize first
    print(x)
```

### Fix 2: Use default values for conditional assignments

```python
# Wrong
def get_value(choice):
    if choice == "a":
        result = "apple"
    return result

# Correct
def get_value(choice):
    result = None  # Default value
    if choice == "a":
        result = "apple"
    return result
```

### Fix 3: Use the `global` keyword when modifying global variables

```python
# Wrong
count = 10
def increment():
    count = count + 1  # UnboundLocalError
    return count

# Correct
count = 10
def increment():
    global count
    count = count + 1
    return count
```

### Fix 4: Return early from exception handlers

```python
# Wrong
def risky_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        error = "division by zero"
    return result

# Correct
def risky_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "division by zero"
```

### Fix 5: Use `nonlocal` for enclosing scope variables

```python
# Wrong
def outer():
    x = 10
    def inner():
        x = x + 1  # UnboundLocalError
        return x
    return inner()

# Correct
def outer():
    x = 10
    def inner():
        nonlocal x
        x = x + 1
        return x
    return inner()
```

## Related Errors

- [NameError: name 'X' is not defined](#) — variable not found in any scope
- [SyntaxError: cannot access local variable](#) — syntax-level scope issue
- [AttributeError](../attributeerror) — attribute doesn't exist on object
