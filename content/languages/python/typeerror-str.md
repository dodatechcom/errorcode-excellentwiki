---
title: "[Solution] Python TypeError: can only concatenate str to str"
description: "Fix Python TypeError: can only concatenate str (not 'int') to str. Use str() to convert non-string types before concatenation, or use f-strings."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["typeerror", "string", "concatenation", "type-conversion"]
weight: 5
---

# TypeError: can only concatenate str to str

A `TypeError: can only concatenate str (not "int") to str` occurs when you try to join a string with a non-string type using the `+` operator. Unlike other languages, Python does not implicitly convert numbers to strings during concatenation.

## Description

Python's `+` operator for strings performs strict type checking — both operands must be `str`. To concatenate non-string values, you must explicitly convert them. This is different from JavaScript, which coerces types automatically.

## Common Causes

```python
# Cause 1: Concatenating string with integer
name = "Age: " + 25  # TypeError: can only concatenate str to str

# Cause 2: Concatenating string with float
message = "Price: " + 19.99  # TypeError

# Cause 3: Concatenating string with None
greeting = "Hello, " + None  # TypeError

# Cause 4: Print statement with implicit concatenation expectation
print("Count: " + count)  # TypeError if count is int
```

## How to Fix

### Fix 1: Use str() to convert values

```python
# Wrong
message = "Age: " + 25

# Correct
message = "Age: " + str(25)
```

### Fix 2: Use f-strings (recommended)

```python
age = 25
price = 19.99

# Best approach
message = f"Age: {age}"
price_msg = f"Price: {price}"
```

### Fix 3: Use format()

```python
message = "Age: {}".format(25)
message = "Age: %d" % 25
```

### Fix 4: Use join() for multiple concatenations

```python
parts = ["Name", ": ", str(name), ", Age: ", str(age)]
message = "".join(parts)
```

## Related Errors

- [TypeError: unsupported operand type(s) for float](typeerror-float) — float arithmetic with wrong types
- [TypeError: int() argument must be a string](typeerror-int) — int conversion failure
- [TypeError: a bytes-like object is required](typeerror-bytes) — bytes vs str confusion
