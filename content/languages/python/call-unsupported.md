---
title: "[Solution] Python TypeError — Unsupported Callable"
description: "Fix Python TypeError: unsupported callable when trying to call an object that is not callable. Debug and resolve call errors."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "callable", "call", "function"]
weight: 5
---

# TypeError — Unsupported Callable

A `TypeError` with the message "unsupported callable" is raised when you try to use the call operator `()` on an object that does not implement the `__call__` method. This means the object is not a function, method, or callable class.

## Description

In Python, only objects that implement the `__call__` method can be invoked using parentheses. Common non-callable objects include integers, strings, lists, and modules. This error often occurs when a variable that should hold a function actually holds something else, such as the result of a function that returns `None`.

Common patterns:

- **Calling a non-function variable** — `my_list()` or `my_int()`.
- **Function returned None** — `result = some_func(); result()`.
- **Wrong import** — importing a module instead of a function.
- **Variable shadowing** — a variable name shadows a function.

## Common Causes

```python
# Cause 1: Calling a list as a function
my_list = [1, 2, 3]
my_list()  # TypeError: 'list' object is not callable

# Cause 2: Function returned None, then called
def process():
    return None

result = process()
result()  # TypeError: 'NoneType' object is not callable

# Cause 3: Importing module instead of function
import json
data = json.loads  # correct
data = json  # wrong — json is a module
data('{"key": "value"}')  # TypeError: 'module' object is not callable

# Cause 4: Variable shadows function name
len = 5
print(len([1, 2, 3]))  # TypeError: 'int' object is not callable
```

## Solutions

### Fix 1: Check if the object is callable before calling

```python
# Wrong
my_list = [1, 2, 3]
my_list()

# Correct
if callable(my_list):
    my_list()
else:
    print("Object is not callable")
```

### Fix 2: Don't shadow built-in names

```python
# Wrong
len = 5
len([1, 2, 3])  # TypeError

# Correct — use a different variable name
length = 5
len([1, 2, 3])  # Returns 3
```

### Fix 3: Verify function return values

```python
# Wrong
def process():
    return None

result = process()
result()  # TypeError

# Correct
def process():
    return lambda x: x * 2

result = process()
if result is not None:
    result(5)  # Returns 10
```

### Fix 4: Use the correct import

```python
# Wrong
import json
data = json
data('{"key": "value"}')  # TypeError: 'module' object is not callable

# Correct
import json
data = json.loads
data('{"key": "value"}')  # Returns dict
```

## Related Errors

- [Module not callable](module-not-callable) — calling a module instead of a function.
- [AttributeError](../attributeerror) — object has no attribute.
- [TypeError](../typeerror) — general type mismatch errors.
