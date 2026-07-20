---
title: "[Solution] Python ArithmeticError — Math Operation Failures"
description: "Fix Python ArithmeticError including ZeroDivisionError, FloatingPointError, and OverflowError. Handle math operations, precision, and overflow scenarios."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 17
---

# Python ArithmeticError — Math Operation Failures

`ArithmeticError` is the base class for errors that occur during mathematical operations. Its subclasses — `ZeroDivisionError`, `FloatingPointError`, and `OverflowError` — each represent a distinct failure mode in numeric computation.

## Common Causes

```python
# Cause 1: Division by zero (ZeroDivisionError)
result = 10 / 0

# Cause 2: Modulo by zero (ZeroDivisionError)
result = 10 % 0

# Cause 3: Integer division by zero (ZeroDivisionError)
result = 10 // 0

# Cause 4: Floating-point overflow (OverflowError)
import math
result = math.exp(1000)  # Too large for float

# Cause 5: Decimal rounding with invalid context (decimal.InvalidOperation)
from decimal import Decimal, getcontext
getcontext().prec = 2
Decimal(1) / Decimal(3)  # May raise with certain settings
```

## How to Fix

### Fix 1: Guard against zero divisors before dividing

```python
# Wrong
def average(values):
    return sum(values) / len(values)  # ZeroDivisionError on empty list

# Correct
def average(values):
    if not values:
        return 0
    return sum(values) / len(values)
```

### Fix 2: Use math.isclose() for floating-point comparisons

```python
# Wrong — floating-point precision issues
import math
result = 0.1 + 0.2
if result == 0.3:
    print("Equal")

# Correct
import math
result = 0.1 + 0.2
if math.isclose(result, 0.3, rel_tol=1e-9):
    print("Equal")
```

### Fix 3: Handle OverflowError in exponential calculations

```python
import math

# Wrong
result = math.exp(1000)  # OverflowError

# Correct
def safe_exp(x):
    try:
        return math.exp(x)
    except OverflowError:
        return float('inf')

# Better — use math.isinf to detect before computing
def safe_exp_v2(x):
    if x > 709:  # math.exp overflows around 710
        return float('inf')
    return math.exp(x)
```

### Fix 4: Use try/except for division-heavy code

```python
def divide_safely(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        if a == 0:
            return float('nan')
        return float('inf') if a > 0 else float('-inf')
```

### Fix 5: Use decimal.Decimal for precise financial calculations

```python
# Wrong — float rounding
price = 0.1 + 0.2  # 0.30000000000000004

# Correct
from decimal import Decimal
price = Decimal('0.1') + Decimal('0.2')  # Decimal('0.3')
```

## Prevention Checklist

- Check for zero before dividing, especially with user-provided or computed values.
- Use `math.isclose()` instead of `==` for floating-point comparisons.
- Wrap `math.exp()`, `math.pow()`, and similar functions in try/except for `OverflowError`.
- Use `decimal.Decimal` for financial and precision-critical calculations.
- Validate numeric input ranges before performing arithmetic operations.

## Related Errors

- [ZeroDivisionError](/languages/python/zerodivisionerror/) — specific to division by zero.
- [FloatingPointError](/languages/python/floatingpointerror/) — floating-point operation failure.
- [OverflowError](/languages/python/overflowerror/) — result too large to represent.
- [ValueError](/languages/python/valueerror/) — invalid value for a math function.
