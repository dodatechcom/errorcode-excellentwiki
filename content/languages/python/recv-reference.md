---
title: "[Solution] Python UnboundLocalError — Local Variable Reference"
description: "Fix Python UnboundLocalError when a local variable is referenced before assignment. Learn about variable scoping and how to resolve this error."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnboundLocalError — Local Variable Reference

An `UnboundLocalError` with the message "local variable 'X' referenced before assignment" is raised when you try to use a variable inside a function before it has been assigned a value within that function's scope. This is a scoping issue that occurs because Python determines variable scope at compile time.

## Description

When Python compiles a function, it determines which variables are local based on assignment statements. If a variable is assigned anywhere in the function, Python treats it as local throughout the entire function. Referencing it before the assignment triggers `UnboundLocalError`, even if the variable exists in an outer scope.

Common patterns:

- **Assignment after reference** — using a variable before the assignment line.
- **Conditional assignment** — variable assigned only in some code paths.
- **Forgetting `global` or `nonlocal`** — not declaring scope for outer variables.
- **Exception handling** — variable only assigned in `try` block but used after `except`.

## Common Causes

```python
# Cause 1: Assignment after reference
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

# Cause 4: Exception handling scope
def func():
    try:
        result = int("abc")
    except ValueError:
        pass
    print(result)  # UnboundLocalError if exception occurred
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

### Fix 2: Use global keyword for module-level variables

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

### Fix 3: Use nonlocal for nested function variables

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

### Fix 4: Handle all code paths

```python
# Wrong
def func(condition):
    if condition:
        value = 42
    print(value)  # UnboundLocalError if condition is False

# Correct
def func(condition):
    value = None
    if condition:
        value = 42
    print(value)
```

### Fix 5: Initialize in exception handlers

```python
# Wrong
def func():
    try:
        result = int("abc")
    except ValueError:
        pass
    print(result)  # UnboundLocalError

# Correct
def func():
    result = None  # Default value
    try:
        result = int("abc")
    except ValueError:
        pass
    print(result)
```

## Related Errors

- [Local variable reference](local-variable-reference) — similar scoping issue.
- [NameError](#) — variable name not defined at all.
- [SyntaxError](../syntaxerror) — related scope syntax errors.
