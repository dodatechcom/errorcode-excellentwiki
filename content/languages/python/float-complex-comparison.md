---
title: "[Solution] Python TypeError — Float and Complex Comparison"
description: "Fix Python TypeError: unsupported operand type when comparing float with complex numbers. Learn why this comparison fails and how to fix it."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "float", "complex", "comparison"]
weight: 5
---

# TypeError — Float and Complex Comparison

A `TypeError` with the message "unsupported operand type(s)" is raised when you try to compare a `float` with a `complex` number using comparison operators like `<`, `>`, `<=`, or `>=`. Complex numbers do not support ordering comparisons in Python.

## Description

In Python, complex numbers cannot be ordered because there is no natural way to define "greater than" or "less than" for complex numbers. You can check equality (`==`) and inequality (`!=`) between complex numbers and other numeric types, but you cannot use `<`, `>`, `<=`, or `>=`.

Common patterns:

- **Comparing complex with float** — `complex_num < 3.14`.
- **Sorting a list with complex numbers** — `sorted([1+2j, 3+4j])`.
- **Using max() or min() on complex numbers** — `max([1+2j, 3+4j])`.
- **Comparing complex with int** — `complex_num > 5`.

## Common Causes

```python
# Cause 1: Direct comparison with <
result = (1 + 2j) < (3 + 4j)  # TypeError: '<' not supported between instances of 'complex' and 'complex'

# Cause 2: Comparing complex with float
result = (1 + 2j) < 3.14  # TypeError: '<' not supported between instances of 'complex' and 'float'

# Cause 3: Sorting a list containing complex numbers
numbers = [3 + 4j, 1 + 2j, 2 + 1j]
sorted_numbers = sorted(numbers)  # TypeError

# Cause 4: Using max() or min() with complex numbers
result = max(1 + 2j, 3 + 4j)  # TypeError
```

## Solutions

### Fix 1: Compare magnitudes instead

```python
# Wrong
result = (1 + 2j) < (3 + 4j)  # TypeError

# Correct — compare absolute values (magnitudes)
result = abs(1 + 2j) < abs(3 + 4j)  # True
```

### Fix 2: Sort by a specific attribute of the complex number

```python
# Wrong
numbers = [3 + 4j, 1 + 2j, 2 + 1j]
sorted_numbers = sorted(numbers)  # TypeError

# Correct — sort by real part, then imaginary part
sorted_numbers = sorted(numbers, key=lambda c: (c.real, c.imag))
print(sorted_numbers)  # [(1+2j), (2+1j), (3+4j)]

# Or sort by magnitude
sorted_numbers = sorted(numbers, key=abs)
```

### Fix 3: Use max/min with a key function

```python
# Wrong
result = max(1 + 2j, 3 + 4j)  # TypeError

# Correct — use key function
result = max(1 + 2j, 3 + 4j, key=abs)  # (3+4j)
```

### Fix 4: Check equality instead of ordering

```python
# Wrong
a = 1 + 2j
b = 1 + 2j
if a > b:
    print("a is greater")

# Correct
a = 1 + 2j
b = 1 + 2j
if a == b:
    print("a equals b")
elif abs(a) > abs(b):
    print("a has larger magnitude")
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [ValueError](../valueerror) — value is wrong but type is correct.
- [ZeroDivisionError](../zerodivisionerror) — division by zero in complex math.
