---
title: "[Solution] Python Built-inFunctionAttribute — Cannot Call Built-in as Method"
description: "Fix Python Built-inFunctionAttribute when trying to call a built-in function as a method. Learn why this error occurs and how to fix it."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# Built-inFunctionAttribute — Cannot Call Built-in as Method

A `Built-inFunctionAttribute` or related `TypeError` is raised when you try to call a built-in function as a method of an object. Built-in functions are not bound to objects and cannot be used with dot notation.

## Description

Built-in functions like `len`, `print`, `range`, `abs`, `min`, `max`, etc. are standalone functions. They are not methods of any class. When you attempt to call them using dot notation on an object, Python raises an error because built-in functions do not have a `__get__` descriptor.

Common patterns:

- **Calling `len` as a method** — `my_list.len()` instead of `len(my_list)`.
- **Calling `print` as a method** — `obj.print()` when `print` is not defined on `obj`.
- **Using `type()` as a method** — `value.type()` instead of `type(value)`.
- **Confusing built-in with custom method** — assuming a built-in like `abs` is available on a number object.

## Common Causes

```python
# Cause 1: Calling len() as a method
my_list = [1, 2, 3]
count = my_list.len()  # Built-inFunctionAttribute: 'list' object has no attribute 'len'

# Cause 2: Calling abs() as a method
number = -5
result = number.abs()  # Built-inFunctionAttribute: 'int' object has no attribute 'abs'

# Cause 3: Calling type() as a method
value = "hello"
t = value.type()  # Built-inFunctionAttribute: 'str' object has no attribute 'type'

# Cause 4: Calling print() as a method on an object
my_string = "hello"
my_string.print()  # Built-inFunctionAttribute: 'str' object has no attribute 'print'
```

## Solutions

### Fix 1: Use built-in functions as standalone calls

```python
# Wrong
my_list = [1, 2, 3]
count = my_list.len()

# Correct
count = len(my_list)
```

### Fix 2: Use the correct method name if it exists

```python
# Wrong
number = -5
result = number.abs()

# Correct — use the built-in function
result = abs(number)

# Or use math.fabs for floating point
import math
result = math.fabs(number)
```

### Fix 3: Check if the method exists before calling

```python
value = "hello"

# Wrong
t = value.type()

# Correct
t = type(value)

# Or check with hasattr
if hasattr(value, 'upper'):
    result = value.upper()
```

### Fix 4: Use the function-style call for type checking

```python
# Wrong
value = 42
t = value.type()

# Correct
t = type(value)
print(t)  # <class 'int'>
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [AttributeError](../attributeerror) — object has no attribute.
- [Module not callable](module-not-callable) — calling a module instead of a function.
