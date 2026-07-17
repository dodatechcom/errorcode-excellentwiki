---
title: "[Solution] Python IndexError — List Index Out of Range"
description: "Fix Python IndexError: list index out of range. Learn why this error occurs and how to safely access list elements."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IndexError — List Index Out of Range

An `IndexError` with the message "list index out of range" is raised when you try to access an index that doesn't exist in a list. The index is either too large, too negative, or the list is empty.

## Description

Python lists are zero-indexed. A list of length `n` has valid indices from `0` to `n-1`. Accessing any index outside this range raises an `IndexError`. This error is common with off-by-one mistakes, empty lists, and stale indices after list modification.

Common patterns:

- **Off-by-one error** — accessing `list[len(list)]` instead of `list[len(list)-1]`.
- **Empty list access** — accessing index 0 of an empty list.
- **Index after modification** — using an index after removing elements from the list.
- **Hardcoded index** — assuming a list always has a certain number of elements.

## Common Causes

```python
# Cause 1: Off-by-one error
items = [1, 2, 3]
value = items[3]  # IndexError: list index out of range

# Cause 2: Empty list access
empty = []
value = empty[0]  # IndexError: list index out of range

# Cause 3: Stale index after modification
data = [10, 20, 30, 40, 50]
for i in range(len(data)):
    if data[i] == 20:
        del data[i]
print(data[i])  # IndexError — i is out of bounds after deletion

# Cause 4: Wrong range in loop
items = [1, 2, 3]
for i in range(len(items) + 1):
    print(items[i])  # IndexError when i == 3
```

## Solutions

### Fix 1: Check list length before accessing

```python
items = [1, 2, 3]

# Wrong
value = items[3]

# Correct
if len(items) > 3:
    value = items[3]
else:
    value = None
```

### Fix 2: Use safe indexing with try/except

```python
items = [1, 2, 3]

# Wrong
value = items[10]

# Correct
try:
    value = items[10]
except IndexError:
    value = None
```

### Fix 3: Use slicing for safe access

```python
items = [1, 2, 3]

# Wrong — raises IndexError
value = items[10]

# Correct — slicing returns empty list instead of error
value = items[10:11]  # Returns []
```

### Fix 4: Avoid index-based iteration when possible

```python
items = [1, 2, 3]

# Wrong
for i in range(len(items)):
    print(items[i])

# Correct — iterate directly
for item in items:
    print(item)

# Or use enumerate if you need the index
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### Fix 5: Don't modify a list while iterating by index

```python
data = [10, 20, 30, 40, 50]

# Wrong
for i in range(len(data)):
    if data[i] == 20:
        del data[i]

# Correct — build a new list
data = [x for x in data if x != 20]
```

## Related Errors

- [IndexError: tuple index out of range](tuple-index) — same error with tuples.
- [KeyError](../keyerror) — missing key in a dictionary.
- [ValueError](../valueerror) — value is wrong but type is correct.
