---
title: "[Solution] Python ValueError: invalid literal for int() with base 10"
description: "Fix Python ValueError: invalid literal for int() with base 10. Handle non-numeric strings, whitespace, and special characters in string-to-int conversion."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["valueerror", "int", "type-conversion", "parsing"]
weight: 5
---

# ValueError: invalid literal for int() with base 10

A `ValueError: invalid literal for int() with base 10: 'X'` occurs when you pass a string to `int()` that doesn't contain a valid integer representation. The string must contain only digits (and an optional sign) with no whitespace, decimal points, or other characters.

## Description

`int()` parses strings strictly — it rejects anything that isn't a clean integer literal. Common rejected inputs include floating-point strings ("3.14"), strings with spaces (" 42 "), empty strings (""), and strings with non-numeric characters ("abc").

## Common Causes

```python
# Cause 1: Float string passed to int()
int("3.14")  # ValueError: invalid literal for int()

# Cause 2: String with whitespace
int(" 42 ")  # ValueError (Python's int doesn't strip whitespace)

# Cause 3: Empty string
int("")  # ValueError: invalid literal for int()

# Cause 4: Non-numeric string
int("hello")  # ValueError: invalid literal for int()

# Cause 5: Number with comma formatting
int("1,000")  # ValueError: invalid literal for int()
```

## How to Fix

### Fix 1: Use float() for decimal strings

```python
# Wrong
result = int("3.14")

# Correct
result = int(float("3.14"))  # 3
# Or keep the decimal
result = float("3.14")  # 3.14
```

### Fix 2: Strip whitespace before converting

```python
# Wrong
result = int(" 42 ")

# Correct
result = int(" 42 ".strip())  # 42
```

### Fix 3: Handle empty strings

```python
# Wrong
result = int("")

# Correct
value = ""
result = int(value) if value.strip() else 0
```

### Fix 4: Remove formatting characters

```python
# Wrong
result = int("1,000,000")

# Correct
result = int("1,000,000".replace(",", ""))  # 1000000
```

### Fix 5: Use a safe conversion function

```python
def safe_int(value, default=0):
    try:
        cleaned = str(value).strip().replace(",", "")
        return int(cleaned)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))       # 42
print(safe_int("3.14"))     # 0 (default)
print(safe_int(""))         # 0
print(safe_int(None, -1))   # -1
```

## Related Errors

- [TypeError: int() argument must be a string](typeerror-int) — wrong type passed to int()
- [ValueError: could not convert string to float](#) — similar for float()
- [TypeError: unsupported operand type(s) for float](typeerror-float) — float arithmetic failure
