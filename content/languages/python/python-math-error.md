---
title: "[Solution] Python math Error — Math Module Domain and Overflow Errors"
description: "Fix Python math errors including ValueError in sqrt/log/asin, domain errors, overflow in factorial, and math.inf/math.nan issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 228
---

# Python math Error — Math Module Domain and Overflow Errors

The `math` module provides mathematical functions. Errors involve domain violations (e.g., sqrt of negative), overflow in large computations, and invalid arguments.

## Common Causes

```python
import math

# Error: Square root of negative number
math.sqrt(-1)
# ValueError: math domain error
```

```python
import math

# Error: Logarithm of zero or negative number
math.log(0)
# ValueError: math domain error

math.log(-1)
# ValueError: math domain error
```

```python
import math

# Error: Asin/acosh with out-of-range argument
math.asin(2)
# ValueError: math domain error
```

```python
import math

# Error: Factorial of negative number
math.factorial(-1)
# ValueError: factorial() not defined for negative values
```

```python
import math

# Error: math.pow with very large exponent causes overflow
math.pow(2, 1000000)
# OverflowError: (34, 'Result too large')
```

## How to Fix

### Fix 1: Validate Arguments Before Domain-Sensitive Functions

```python
import math

def safe_sqrt(x):
    if x < 0:
        raise ValueError(f"Cannot compute sqrt of {x}")
    return math.sqrt(x)

def safe_log(x, base=None):
    if x <= 0:
        raise ValueError(f"Cannot compute log of {x}")
    if base is not None:
        return math.log(x, base)
    return math.log(x)

print(safe_sqrt(16))    # 4.0
print(safe_log(100))    # 4.60517...
```

### Fix 2: Use cmath for Complex Numbers

```python
import cmath

# cmath handles negative inputs for sqrt
result = cmath.sqrt(-1)
print(result)  # 1j

# Convert to real if needed
real_result = cmath.sqrt(-1).real  # 0.0
```

### Fix 3: Use math.isclose for Floating-Point Comparisons

```python
import math

# Don't compare floats directly with domain checks
x = -0.0  # negative zero
print(math.sqrt(x))  # 0.0 — works fine

# Use isclose for comparisons near domain boundaries
a = math.sqrt(2) * math.sqrt(2)
b = 2.0
print(math.isclose(a, b))  # True
```

### Fix 4: Handle Factorial Overflow with Python Integers

```python
import math
import sys

# Python integers don't overflow, but very large ones use lots of memory
try:
    result = math.factorial(10**6)  # works but uses ~2.5MB
except OverflowError:
    print("Factorial too large to compute")

# Use Stirling's approximation for very large factorials
def stirling_approx(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n
```

## Examples

```python
import math

# Safe mathematical operations
def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def safe_acos(x):
    x = clamp(x, -1.0, 1.0)
    return math.acos(x)

# Calculate compound interest safely
def compound_interest(principal, rate, years):
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("All arguments must be non-negative")
    return principal * math.pow(1 + rate / 100, years)

result = compound_interest(1000, 5, 10)
print(f"Final amount: ${result:.2f}")  # Final amount: $1628.89
```

## Related Errors

- [Python ValueError](/languages/python/python-valueerror/)
- [Python OverflowError](/languages/python/python-overflowerror/)
- [Python ArithmeticError](/languages/python/python-arithmeticerror/)
