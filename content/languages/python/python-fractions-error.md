---
title: "[Solution] Python fractions Error — Fraction Creation and Arithmetic Errors"
description: "Fix Python fractions errors including Fraction creation, gcd issues, infinite/NaN fractions, and conversion errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 225
---

# Python fractions Error — Fraction Creation and Arithmetic Errors

The `fractions` module provides rational number arithmetic. Errors occur during Fraction creation from invalid types, division by zero leading to infinite fractions, and conversion issues.

## Common Causes

```python
from fractions import Fraction

# Error: Invalid string format
f = Fraction("1/0")
# ZeroDivisionError
```

```python
from fractions import Fraction

# Error: Fraction from float loses precision unexpectedly
f = Fraction(0.1)
print(f)  # Fraction(3602879701896397, 36028797018963968) — surprising
```

```python
from fractions import Fraction

# Error: Creating Fraction with invalid type
f = Fraction(object())
# TypeError: expected string, int, or float
```

```python
from fractions import Fraction

# Error: Division by zero results in infinite Fraction
f = Fraction(1, 0)
# ZeroDivisionError: Fraction(1, 0)
```

```python
from fractions import Fraction

# Error: Limiting denominator can give unexpected results
f = Fraction(355, 113)
f2 = f.limit_denominator(100)
print(f2)  # Fraction(22, 7) — approximation
```

## How to Fix

### Fix 1: Catch ZeroDivisionError for Invalid Strings

```python
from fractions import Fraction

def safe_fraction(value):
    try:
        if isinstance(value, str):
            return Fraction(value)
        return Fraction(value)
    except ZeroDivisionError:
        print(f"Invalid fraction (division by zero): {value}")
        return None
    except (ValueError, TypeError) as e:
        print(f"Cannot create fraction from {value}: {e}")
        return None

result = safe_fraction("1/0")    # None
result = safe_fraction("3/4")    # Fraction(3, 4)
result = safe_fraction(0.5)      # Fraction(1, 2)
```

### Fix 2: Use Fraction Constructor with limit_denominator for Floats

```python
from fractions import Fraction

# Instead of Fraction(0.1), use:
f = Fraction(0.1).limit_denominator()
print(f)  # Fraction(1, 10) — expected

# Or construct from string for exact representation
f = Fraction("0.1")
print(f)  # Fraction(1, 10)
```

### Fix 3: Use Valid Types for Fraction Construction

```python
from fractions import Fraction

# Valid types: int, float, string, or another Fraction
f1 = Fraction(3, 4)
f2 = Fraction("7/8")
f3 = Fraction(1.5)
f4 = Fraction(f1)

# Convert from unsupported type first
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
f = Fraction(p.x, p.y)  # Convert attributes first
```

### Fix 4: Use gcd Properly

```python
from fractions import Fraction, gcd
import math

# Python 3.5+: use math.gcd
a, b = 12, 8
g = math.gcd(a, b)
print(f"GCD of {a} and {b} is {g}")  # 4

# fractions.Fraction automatically reduces
f = Fraction(4, 8)
print(f)  # Fraction(1, 2) — already reduced
```

## Examples

```python
from fractions import Fraction

# Exact arithmetic with fractions
recipe = [
    ("flour", Fraction(3, 4), "cup"),
    ("sugar", Fraction(1, 2), "cup"),
    ("butter", Fraction(1, 3), "cup"),
]

total = sum(amount for _, amount, _ in recipe)
print(f"Total: {total} cups")  # Total: 17/12 cups
print(f"As decimal: {float(total):.4f}")  # 1.4167

# Probability calculations
favorable = Fraction(1, 6)  # rolling a 6
total_outcomes = Fraction(1)
print(f"P(6) = {favorable}")  # P(6) = 1/6
```

## Related Errors

- [Python ZeroDivisionError](/languages/python/python-zerodivisionerror/)
- [Python TypeError](/languages/python/python-typeerror/)
- [Python ValueError](/languages/python/python-valueerror/)
