---
title: "[Solution] Python ValueError: too many values to unpack Fix"
description: "Fix Python ValueError: too many values to unpack (expected N). Use underscore for unused variables, star expressions, or restructure unpacking."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ValueError: too many values to unpack

A `ValueError` with `too many values to unpack (expected N)` is raised when you try to unpack more values from an iterable than you have variables to receive them. The number of variables on the left side must match the number of values on the right.

## Description

Python unpacking requires an exact match between the number of variables and values. This error occurs in tuple/list unpacking, function return value unpacking, and loop variable unpacking.

Common variants:

- `ValueError: too many values to unpack (expected 2)`
- `ValueError: too many values to unpack (expected 1)`
- `ValueError: not enough values to unpack (expected 2, got 1)` — the reverse error

## Common Causes

```python
# Cause 1: Unpacking more values than variables
a, b = (1, 2, 3)  # ValueError: too many values to unpack (expected 2)

# Cause 2: Function returns more values than expected
def get_user():
    return "Alice", 30, "admin", "alice@example.com"

name, age = get_user()  # ValueError: too many values to unpack (expected 2)

# Cause 3: CSV parsing with unexpected number of columns
line = "Alice,30,admin,alice@example.com"
name, age = line.split(",")  # ValueError: too many values to unpack (expected 2)

# Cause 4: Unpacking nested structures incorrectly
data = [(1, 2, 3), (4, 5, 6)]
for a, b in data:  # ValueError: too many values to unpack (expected 2)
    print(a, b)

# Cause 5: Database query returning more columns
cursor.execute("SELECT name, age FROM users")
row = cursor.fetchone()
name, age, extra = row  # ValueError if only 2 columns selected
```

## How to Fix

### Fix 1: Use underscore for unused values

```python
# Wrong — only 2 variables but 3 values
a, b = (1, 2, 3)

# Correct — use underscore for unused values
a, b, _ = (1, 2, 3)

# For many unused values
a, _, _, _, _ = (1, 2, 3, 4, 5)
```

### Fix 2: Use star expression to capture remaining values

```python
# Wrong
first, second = [1, 2, 3, 4, 5]

# Correct — star captures remaining values as a list
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5
```

### Fix 3: Unpack the correct number of values

```python
# Wrong
def get_user():
    return "Alice", 30, "admin", "alice@example.com"

name, age = get_user()  # Too many values

# Correct — unpack all values
name, age, role, email = get_user()

# Or use a named tuple for clarity
from collections import namedtuple
User = namedtuple("User", ["name", "age", "role", "email"])
user = User(*get_user())
print(user.name, user.age)
```

### Fix 4: Use indexed access for specific elements

```python
# Wrong
data = [1, 2, 3, 4, 5]
a, b = data

# Correct — access specific indices
a = data[0]
b = data[1]
# Or use unpacking with star
a, b, *_ = data
```

### Fix 5: Validate data before unpacking

```python
# Wrong — assumes correct number of columns
line = "Alice,30,admin,alice@example.com"
name, age = line.split(",")

# Correct — check length first
parts = line.split(",")
if len(parts) >= 2:
    name, age = parts[0], parts[1]
else:
    print(f"Expected at least 2 values, got {len(parts)}")
```

## Examples

This error commonly occurs when:

- Parsing CSV files with variable numbers of columns
- Unpacking function return values after adding a new return field
- Using tuple unpacking in loops with nested structures
- Processing API responses with inconsistent data shapes

## Related Errors

- [ValueError: not enough values to unpack](#) — fewer values than variables
- [TypeError: cannot unpack non-iterable](#) — trying to unpack a non-iterable
- [IndexError: list index out of range](#) — accessing unpacked values incorrectly
