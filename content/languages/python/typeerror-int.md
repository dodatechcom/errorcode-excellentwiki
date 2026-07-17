---
title: "[Solution] Python TypeError: int() argument must be a string or number"
description: "Fix Python TypeError: int() argument must be a string or bytes-like instance, or a real number, not 'X'. Convert types properly before calling int()."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# TypeError: int() argument must be a string or number

A `TypeError: int() argument must be a string, a bytes-like instance or a real number, not 'list'` occurs when you pass an incompatible type to `int()`. The `int()` constructor only accepts strings (parseable as integers), bytes, or numeric types.

## Description

The `int()` function converts values to integers. It accepts:

- Strings containing digits (optionally with sign): `int("42")`
- Floats: `int(3.7)` → `3` (truncates toward zero)
- Other numeric types: `int(True)` → `1`

It rejects `list`, `dict`, `set`, arbitrary objects, and strings with non-digit characters.

## Common Causes

```python
# Cause 1: Passing a list
int([1, 2, 3])  # TypeError: list is not a valid type

# Cause 2: Passing a dict
int({"a": 1})  # TypeError: dict is not a valid type

# Cause 3: Passing a string with non-digit characters
int("3.14")  # ValueError (not TypeError), but common companion

# Cause 4: Passing None
int(None)  # TypeError: int() argument must be a string, bytes-like instance or a real number, not 'NoneType'

# Cause 5: Passing a custom object
class MyObj:
    pass
int(MyObj())  # TypeError
```

## How to Fix

### Fix 1: Convert the correct element

```python
# Wrong
data = ["1", "2", "3"]
result = int(data)  # TypeError

# Correct — iterate and convert each element
result = [int(x) for x in data]
```

### Fix 2: Handle None before conversion

```python
# Wrong
value = None
result = int(value)  # TypeError

# Correct
value = None
result = int(value) if value is not None else 0
```

### Fix 3: Validate string contents before converting

```python
# Wrong
user_input = "3.14"
result = int(user_input)  # ValueError

# Correct — use float first if decimals expected
result = int(float(user_input))  # 3

# Or validate string content
import re
if re.match(r"^-?\d+$", user_input):
    result = int(user_input)
```

### Fix 4: Implement `__int__` for custom objects

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

m = Money(10.5)
int(m)  # 10
```

## Related Errors

- [ValueError: invalid literal for int() with base 10](valueerror-bool) — string can't be parsed as int
- [TypeError: unsupported operand type(s) for float](typeerror-float) — float arithmetic failure
- [TypeError: can only concatenate str to str](typeerror-str) — string concatenation issue
