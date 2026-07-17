---
title: "[Solution] Python IndexError — Tuple Index Out of Range"
description: "Fix Python IndexError: tuple index out of range. Learn why tuple indexing fails and how to safely access tuple elements."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IndexError — Tuple Index Out of Range

An `IndexError` with the message "tuple index out of range" is raised when you try to access an index that doesn't exist in a tuple. Like lists, tuples are zero-indexed, and accessing an invalid index raises an error.

## Description

Tuples are immutable sequences in Python. They are zero-indexed just like lists. A tuple of length `n` has valid indices from `0` to `n-1`. Accessing any index outside this range raises `IndexError`. The key difference from lists is that tuples cannot be modified after creation.

Common patterns:

- **Off-by-one error** — accessing `tuple[len(tuple)]`.
- **Empty tuple access** — accessing index 0 of an empty tuple.
- **Hardcoded index** — assuming a tuple always has a certain number of elements.
- **Using list index on tuple** — wrong data type assumption.

## Common Causes

```python
# Cause 1: Off-by-one error
my_tuple = (1, 2, 3)
value = my_tuple[3]  # IndexError: tuple index out of range

# Cause 2: Empty tuple access
empty = ()
value = empty[0]  # IndexError: tuple index out of range

# Cause 3: Hardcoded index
def get_second(items):
    return items[1]  # IndexError if tuple has fewer than 2 elements

get_second((1,))  # IndexError

# Cause 4: Wrong tuple length assumption
data = (1, 2)
a, b, c = data  # ValueError: not enough values to unpack
```

## Solutions

### Fix 1: Check tuple length before accessing

```python
my_tuple = (1, 2, 3)

# Wrong
value = my_tuple[3]

# Correct
if len(my_tuple) > 3:
    value = my_tuple[3]
else:
    value = None
```

### Fix 2: Use try/except for safe access

```python
my_tuple = (1, 2, 3)

# Wrong
value = my_tuple[10]

# Correct
try:
    value = my_tuple[10]
except IndexError:
    value = None
```

### Fix 3: Use slicing for safe access

```python
my_tuple = (1, 2, 3)

# Wrong — raises IndexError
value = my_tuple[10]

# Correct — slicing returns empty tuple instead of error
value = my_tuple[10:11]  # ()
```

### Fix 4: Use unpacking with defaults

```python
# Wrong
data = (1, 2)
a, b, c = data  # ValueError

# Correct
data = (1, 2)
a = data[0] if len(data) > 0 else None
b = data[1] if len(data) > 1 else None
c = data[2] if len(data) > 2 else None
```

### Fix 5: Use named tuples for clarity

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

# Instead of tuple indexing
x = p[0]  # Works but unclear
y = p[1]  # Works but unclear

# Use named access
x = p.x  # Clear and descriptive
y = p.y
```

## Related Errors

- [IndexError: list index out of range](index-out-of-range) — same error with lists.
- [KeyError](../keyerror) — missing key in a dictionary.
- [ValueError: not enough values to unpack](unpack-non-sequence) — unpacking errors.
