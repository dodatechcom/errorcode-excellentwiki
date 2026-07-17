---
title: "[Solution] Python ValueError — Not Enough Values to Unpack"
description: "Fix Python ValueError: not enough values to unpack when unpacking sequences. Learn about sequence unpacking and how to handle variable-length data."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ValueError — Not Enough Values to Unpack

A `ValueError` with the message "not enough values to unpack" is raised when you try to unpack a sequence into more variables than the sequence contains. The number of variables must match the number of elements, or you must use starred expressions.

## Description

Sequence unpacking assigns elements of a sequence to variables. Python requires the number of variables to match the number of elements, unless you use `*` to capture remaining elements. This error is common when data has unexpected length.

Common patterns:

- **Too many variables** — `a, b, c = (1, 2)`.
- **Missing starred expression** — `a, b = (1, 2, 3)`.
- **Dynamic data with fixed unpacking** — function returns fewer values than expected.
- **Dictionary unpacking** — unpacking `.items()` with wrong variable count.

## Common Causes

```python
# Cause 1: Too many variables
a, b, c = (1, 2)  # ValueError: not enough values to unpack (expected 3, got 2)

# Cause 2: Missing starred expression
a, b = (1, 2, 3)  # ValueError: too many values to unpack (expected 2)

# Cause 3: Dynamic data with fixed unpacking
def get_data():
    return (1, 2)  # Sometimes returns 2 elements

a, b, c = get_data()  # ValueError

# Cause 4: Unpacking dict items with wrong count
data = {"a": 1, "b": 2}
for key, value in data.items():
    pass  # Works — but if dict has nested tuples:
data = {"a": (1, 2), "b": (3, 4)}
for key, (x, y, z) in data.items():  # ValueError — tuples have 2 elements
    pass
```

## Solutions

### Fix 1: Match variable count to element count

```python
# Wrong
a, b, c = (1, 2)  # ValueError

# Correct
a, b = (1, 2)  # Works
```

### Fix 2: Use starred expression for remaining elements

```python
# Wrong
a, b = (1, 2, 3)  # ValueError

# Correct — capture remaining elements
a, *b = (1, 2, 3)  # a=1, b=[2, 3]
a, *b, c = (1, 2, 3, 4)  # a=1, b=[2, 3], c=4
```

### Fix 3: Use default values with unpacking

```python
# Wrong
def get_data():
    return (1,)  # Only one element

a, b = get_data()  # ValueError

# Correct
def get_data():
    return (1,)  # Only one element

data = get_data()
a = data[0] if len(data) > 0 else None
b = data[1] if len(data) > 1 else None
```

### Fix 4: Use slicing for safe unpacking

```python
data = (1, 2, 3, 4, 5)

# Wrong
a, b, c, d, e, f = data  # ValueError

# Correct
a, b, c = data[:3]  # Safe
d = data[3] if len(data) > 3 else None
```

## Related Errors

- [ValueError: too many values to unpack](unpack-non-sequence) — opposite problem.
- [IndexError: tuple index out of range](tuple-index) — tuple indexing errors.
- [TypeError](../typeerror) — general type mismatch errors.
