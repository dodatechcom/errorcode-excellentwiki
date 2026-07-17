---
title: "[Solution] Python TypeError: unsupported operand type(s) for float"
description: "Fix Python TypeError: unsupported operand type(s) for float. Understand float arithmetic with non-numeric types and implicit conversion errors."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["typeerror", "float", "arithmetic", "type-conversion"]
weight: 5
---

# TypeError: unsupported operand type(s) for float

A `TypeError: unsupported operand type(s) for +: 'float' and 'str'` (or similar) occurs when you attempt an arithmetic operation between a float and a type that doesn't support it, such as a string, None, or list.

## Description

Python floats support arithmetic with `int`, `float`, `decimal.Decimal`, and `complex`. Operations with other types like `str`, `list`, `dict`, or `None` raise TypeError. This commonly happens when user input isn't converted, or a function returns an unexpected type.

## Common Causes

```python
# Cause 1: String passed to float arithmetic
result = 3.14 + "2"  # TypeError: unsupported operand type(s) for +

# Cause 2: None value from a failed lookup
data = {"price": None}
total = 3.0 + data["price"]  # TypeError

# Cause 3: List instead of number
values = [1, 2, 3]
result = 1.5 + values  # TypeError

# Cause 4: Unconverted user input
amount = float(input("Enter amount: "))  # User enters "abc"
# ValueError (not TypeError), but later arithmetic with the variable can fail

# Cause 5: Boolean arithmetic edge case
result = 3.0 + True  # Works (True == 1), but can be confusing
```

## How to Fix

### Fix 1: Validate and convert types explicitly

```python
def safe_add(a, b):
    try:
        return float(a) + float(b)
    except (TypeError, ValueError):
        return None

result = safe_add(3.14, "2")  # 5.14
result = safe_add(3.14, None)  # None
```

### Fix 2: Use type checking before arithmetic

```python
def compute(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
    return a + b
```

### Fix 3: Handle None values from databases or APIs

```python
# Wrong
price = get_price()  # might return None
total = price * quantity

# Correct
price = get_price() or 0.0
total = price * quantity
```

## Related Errors

- [TypeError: int() argument must be a string](typeerror-int) — int conversion failure
- [TypeError: can only concatenate str to str](typeerror-str) — string concatenation
- [ValueError: invalid literal for int()](valueerror-bool) — string-to-int conversion
