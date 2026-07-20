---
title: "[Solution] Python decimal Error — Decimal Module Precision and Context Errors"
description: "Fix Python decimal errors including InvalidOperation, DivisionByZero, Overflow, context errors, rounding, and precision issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 224
---

# Python decimal Error — Decimal Module Precision and Context Errors

The `decimal` module provides arbitrary-precision decimal arithmetic. Errors involve invalid operations, division by zero, overflow/underflow, context traps, and rounding issues.

## Common Causes

```python
from decimal import Decimal, InvalidOperation

# Error: Invalid string for Decimal construction
d = Decimal("abc")
# decimal.InvalidOperation
```

```python
from decimal import Decimal, DivisionByZero

# Error: Division by zero
context = Decimal("0")
result = Decimal("1") / context
# decimal.DivisionByZero
```

```python
from decimal import Decimal, InvalidOperation

# Error: square root of negative number
result = Decimal("-1").sqrt()
# decimal.InvalidOperation
```

```python
from decimal import Decimal, Context, getcontext

# Error: Result exceeds the context precision
getcontext().prec = 5
result = Decimal("1") / Decimal("3") * Decimal("100000")
# decimal.Inexact (if Inexact is trapped)
```

```python
from decimal import Decimal, InvalidOperation

# Error: Invalid rounding mode
Decimal("1.5").quantize(Decimal("0.1"), rounding="INVALID_MODE")
# decimal.InvalidOperation
```

## How to Fix

### Fix 1: Validate Input Before Decimal Construction

```python
from decimal import Decimal, InvalidOperation

def safe_decimal(value):
    try:
        return Decimal(str(value))
    except InvalidOperation:
        print(f"Invalid decimal value: {value}")
        return None

result = safe_decimal("abc")  # None
result = safe_decimal("3.14")  # Decimal('3.14')
```

### Fix 2: Handle DivisionByZero Explicitly

```python
from decimal import Decimal, DivisionByZero, localcontext

def safe_divide(a, b):
    try:
        return Decimal(str(a)) / Decimal(str(b))
    except DivisionByZero:
        print("Cannot divide by zero")
        return None

result = safe_divide(1, 0)  # None
result = safe_divide(10, 3)  # Decimal('3.333333333...')
```

### Fix 3: Set Context Precision Appropriately

```python
from decimal import Decimal, localcontext, getcontext

# Use localcontext for precision-sensitive calculations
with localcontext() as ctx:
    ctx.prec = 50
    result = Decimal("1") / Decimal("3")
    print(result)

# Or set global precision
getcontext().prec = 28  # default
```

### Fix 4: Handle Overflow and Trapped Exceptions

```python
from decimal import Decimal, Context, getcontext, Inexact, Rounded

# Disable traps for non-critical exceptions
with localcontext() as ctx:
    ctx.traps[Inexact] = 0
    ctx.traps[Rounded] = 0
    ctx.prec = 5
    result = Decimal("1") / Decimal("3")
    print(result)  # Decimal('0.33333')
```

## Examples

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN

# Financial calculations with proper rounding
getcontext().prec = 10

price = Decimal("19.99")
quantity = Decimal("3")
tax_rate = Decimal("0.08")

subtotal = price * quantity
tax = subtotal * tax_rate
total = (subtotal + tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"Total: ${total}")  # Total: $21.59

# Avoid floating-point issues
result = Decimal("0.1") + Decimal("0.2")
print(result)  # Decimal('0.3') — exact!
```

## Related Errors

- [Python ArithmeticError](/languages/python/python-arithmeticerror/)
- [Python ValueError](/languages/python/python-valueerror/)
- [Python ZeroDivisionError](/languages/python/python-zerodivisionerror/)
