---
title: "[Solution] Python TypeError: missing required positional argument Fix"
description: "Fix Python TypeError: missing required positional argument. Add default values, check function signatures, and handle optional parameters correctly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError: missing required positional argument

A `TypeError` with `missing required positional argument: 'X'` is raised when you call a function without providing a value for a parameter that has no default. Python enforces that all non-default parameters must be passed by the caller.

## Description

Every function parameter without a default value is required. When you forget to pass it, Python raises this error with the parameter name. This is common with refactored functions, misused `*args`, and callbacks that don't match expected signatures.

Common variants:

- `TypeError: greet() missing 1 required positional argument: 'name'`
- `TypeError: process() missing 2 required positional arguments: 'data' and 'callback'`
- `TypeError: __init__() missing 1 required positional argument: 'self'`

## Common Causes

```python
# Cause 1: Forgetting to pass a required argument
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet()  # TypeError: greet() missing 1 required positional argument: 'name'

# Cause 2: Confusing positional and keyword arguments
def process(data, callback):
    return callback(data)

process(callback=lambda x: x)  # TypeError: missing 'data'

# Cause 3: Refactoring adds required parameters
# Old: def save(filename)
# New: def save(filename, format)
# Existing calls to save() break

# Cause 4: Class method missing 'self'
class MyClass:
    def method(self, x):
        return x * 2

obj = MyClass()
obj.method()  # TypeError: method() missing 1 required positional argument: 'x'

# Cause 5: Using *args without handling the required args
def wrapper(*args, **kwargs):
    return original_function(*args, **kwargs)

def original_function(a, b):
    return a + b

wrapper()  # TypeError: missing 'a' and 'b'
```

## How to Fix

### Fix 1: Add default values to parameters

```python
# Wrong
def greet(name, greeting):
    return f"{greeting}, {name}!"

# Correct — add default to optional parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### Fix 2: Pass all required arguments

```python
# Wrong
def process(data, callback):
    return callback(data)

result = process(callback=lambda x: x)

# Correct — pass both arguments
result = process(data=[1, 2, 3], callback=lambda x: sum(x))
```

### Fix 3: Use *args and **kwargs carefully

```python
# Wrong — wrapper doesn't know what original_function needs
def wrapper(*args, **kwargs):
    return original_function(*args, **kwargs)

# Correct — explicitly pass known arguments
def wrapper(data=None, callback=None):
    return original_function(data=data, callback=callback)
```

### Fix 4: Inspect function signatures before calling

```python
import inspect

def safe_call(func, *args, **kwargs):
    sig = inspect.signature(func)
    bound = sig.bind(*args, **kwargs)
    bound.apply_defaults()
    return func(*bound.args, **bound.kwargs)

# Usage — won't crash if arguments are missing
result = safe_call(greet)
```

### Fix 5: Use functools.partial for pre-filling arguments

```python
from functools import partial

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Create a partial with the required argument filled
hello_alice = partial(greet, name="Alice")
hello_alice()  # "Hello, Alice!"
```

## Examples

This error commonly occurs when:

- After adding a new required parameter to an existing function
- When a callback function signature doesn't match what the caller expects
- Using `*args` in a wrapper that doesn't forward all arguments
- When a class method is called without instantiating the class first

## Related Errors

- [TypeError: takes X positional arguments but Y were given](#) — too many positional arguments
- [TypeError: argument of type 'NoneType' is not iterable](typeerror-none) — None passed where required
- [AttributeError](#) — calling a method on an object that doesn't have it
