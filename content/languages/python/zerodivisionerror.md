---
title: "[Solution] Python ZeroDivisionError — Division by Zero Fix"
description: "Fix Python ZeroDivisionError: division by zero. Add input validation and handle edge cases in mathematical operations."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["zerodivisionerror", "division", "zero", "math"]
weight: 90
---

# ZeroDivisionError — Division by Zero Fix

A `ZeroDivisionError` is raised when you attempt to divide a number by zero. This applies to integer division (`//`), float division (`/`), and the modulo operator (`%`).

## Description

In Python, dividing by zero is always an error — unlike some languages that return `Infinity` or `NaN` for floats. Both integer and float zero trigger this error.

Common scenarios:

- **Direct division by zero** — `x / 0`.
- **Variable becomes zero at runtime** — divisor is computed and happens to be zero.
- **Modulo by zero** — `x % 0`.
- **Integer division by zero** — `x // 0`.
- **Float zero** — `1.0 / 0.0` also raises the error (not `inf`).

## Common Causes

```python
# Cause 1: Direct division by zero
result = 10 / 0

# Cause 2: Divisor computed from data
numbers = [10, 20, 0, 30]
for n in numbers:
    result = 100 / n  # ZeroDivisionError when n == 0

# Cause 3: Modulo by zero
remainder = 10 % 0

# Cause 4: Integer division by zero
result = 10 // 0

# Cause 5: Denominator from user input
denominator = int(input("Enter a number: "))
result = 100 / denominator  # Crashes if user enters 0
```

## Solutions

### Fix 1: Check divisor before dividing

```python
# Wrong
def divide(a, b):
    return a / b

# Correct
def divide(a, b):
    if b == 0:
        return None
    return a / b
```

### Fix 2: Use try/except to handle zero gracefully

```python
# Wrong
result = numerator / denominator

# Correct
try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = None
```

### Fix 3: Guard against zero in loops with data

```python
# Wrong
numbers = [10, 20, 0, 30]
for n in numbers:
    result = 100 / n

# Correct
numbers = [10, 20, 0, 30]
for n in numbers:
    if n != 0:
        result = 100 / n
    else:
        print(f"Skipping zero, cannot divide 100 by {n}")
```

### Fix 4: Use math.isclose() for float comparisons

```python
import math

# Wrong — floating point comparison with exact zero
def safe_divide(a, b):
    if b == 0.0:  # Might miss very small floats close to zero
        return None
    return a / b

# Correct — account for floating point imprecision
def safe_divide(a, b):
    if math.isclose(b, 0.0, abs_tol=1e-10):
        return None
    return a / b
```

### Fix 5: Use a decorator or context manager for mathematical functions

```python
import functools

def prevent_zero_division(func):
    @functools.wraps(func)
    def wrapper(a, b, *args, **kwargs):
        if b == 0:
            raise ValueError(f"Cannot divide {a} by zero")
        return func(a, b, *args, **kwargs)
    return wrapper

@prevent_zero_division
def divide(a, b):
    return a / b

# This raises ValueError instead of ZeroDivisionError
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # "Cannot divide 10 by zero"
```

## Related Errors

- [OverflowError](#) — result too large to represent (for very large exponents).
- [ValueError](../valueerror) — wrong value type or invalid input.
- [TypeError](../typeerror) — wrong type passed to a mathematical function.
