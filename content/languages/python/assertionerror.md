---
title: "[Solution] Python AssertionError — Assert Statement Failures"
description: "Fix Python AssertionError from assert statements, testing, and debug mode. Learn when asserts are stripped, how to use them correctly, and alternatives."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 18
---

# Python AssertionError — Assert Statement Failures

An `AssertionError` is raised when an `assert` statement evaluates to `False`. Asserts are debugging aids that are stripped when Python runs with optimization (`-O`), so they should never be used for input validation or production error handling.

## Common Causes

```python
# Cause 1: Assert fails due to wrong assumption
def calculate_discount(price, discount):
    assert discount >= 0, "Discount cannot be negative"
    assert discount <= 1, "Discount cannot exceed 100%"
    return price * (1 - discount)

calculate_discount(100, 1.5)  # AssertionError: Discount cannot exceed 100%

# Cause 2: Asserting a condition that can be False in production
def process_order(order):
    assert order is not None  # Fails if None is passed
    assert order.items        # Fails if items list is empty
    return total(order.items)

# Cause 3: Using assert for type checking (stripped with -O)
def set_name(name):
    assert isinstance(name, str), "Name must be a string"
    return name.strip()
# Running with 'python -O script.py' removes this check entirely

# Cause 4: Assert with side effects that are skipped
data = []
assert data.append(1) is None  # append returns None — passes, but data unchanged
assert len(data) == 1  # AssertionError — data is still empty

# Cause 5: Comparison assertions with misleading messages
x, y = 5, 10
assert x == y, f"Expected {y}, got {x}"
# AssertionError: Expected 10, got 5
```

## How to Fix

### Fix 1: Use if/raise for production input validation

```python
# Wrong — stripped with python -O
def set_age(age):
    assert isinstance(age, int), "Age must be an integer"
    assert 0 <= age <= 150, "Age out of range"
    return age

# Correct — always enforced
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if not 0 <= age <= 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")
    return age
```

### Fix 2: Use assert only for invariants and debugging

```python
def merge_sorted(a, b):
    """Merge two sorted lists. Asserts enforce preconditions during development."""
    assert all(a[i] <= a[i+1] for i in range(len(a)-1)), "a must be sorted"
    assert all(b[i] <= b[i+1] for i in range(len(b)-1)), "b must be sorted"
    # Actual implementation follows
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

### Fix 3: Use pytest assertions with proper comparison

```python
# Wrong — vague assertion
def test_addition():
    result = 2 + 2
    assert result == 5  # AssertionError with no useful info

# Correct — pytest shows detailed comparison
def test_addition():
    result = 2 + 2
    assert result == 4

# Better — custom message for unittest
import unittest
class TestMath(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4, f"2 + 2 should be 4, got {result}")
```

### Fix 4: Never use assert with side effects

```python
# Wrong — assert with side effects
assert database.connect(), "Failed to connect"

# Correct — explicit check with side effect
if not database.connect():
    raise ConnectionError("Failed to connect to database")
```

## Prevention Checklist

- Use `assert` only for debugging invariants, never for input validation or production logic.
- Use `if/raise` for conditions that must be enforced at runtime.
- Do not rely on `assert` for security or data integrity — it is stripped with `python -O`.
- Avoid side effects inside `assert` statements.
- In tests, use the test framework's assertion methods for better error messages.

## Related Errors

- [ValueError](/languages/python/valueerror/) — correct type but wrong value.
- [TypeError](/languages/python/typeerror/) — wrong type passed to a function.
- [RuntimeError](/languages/python/runtimeerror/) — generic runtime failure.
