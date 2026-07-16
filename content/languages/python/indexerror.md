---
title: "[Solution] Python IndexError — List Index Out of Range Fix"
description: "Fix Python IndexError: list index out of range. Check list bounds, use enumerate(), and handle empty lists properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["indexerror", "list", "index", "range"]
weight: 40
---

# IndexError — List Index Out of Range Fix

An `IndexError` is raised when a sequence subscript is out of range. You are accessing an index that doesn't exist in the list, tuple, or string.

## Description

Python sequences are zero-indexed. A list of length 3 has valid indices `0`, `1`, `2`. Accessing index `3` or higher raises `IndexError: list index out of range`. The same applies to negative indices — `list[-4]` on a length-3 list also fails.

Common triggers:

- **Off-by-one error in loops** — `range(len(list) + 1)` instead of `range(len(list))`.
- **Assuming list has elements** — accessing index 0 of an empty list.
- **Stale index after list modification** — removing elements while iterating with index.
- **Confusing len() with last valid index** — `len()` returns count, last index is `len() - 1`.

## Common Causes

```python
# Cause 1: Off-by-one in loop
items = ["a", "b", "c"]
for i in range(len(items) + 1):
    print(items[i])  # IndexError when i == 3

# Cause 2: Accessing index 0 of an empty list
empty = []
value = empty[0]  # IndexError

# Cause 3: Stale index after list modification
data = [10, 20, 30, 40, 50]
for i in range(len(data)):
    if data[i] == 20:
        del data[i]  # After deletion, indices shift
print(data[i])  # IndexError — i is now out of bounds

# Cause 4: Negative index exceeds list length
short = [1, 2]
print(short[-3])  # IndexError
```

## Solutions

### Fix 1: Use range(len(list)) — not len(list) + 1

```python
# Wrong
items = ["a", "b", "c"]
for i in range(len(items) + 1):
    print(items[i])

# Correct
for i in range(len(items)):
    print(items[i])

# Even better — avoid index access entirely
for item in items:
    print(item)
```

### Fix 2: Check list length before accessing

```python
# Wrong
empty = []
value = empty[0]

# Correct
if empty:
    value = empty[0]
else:
    value = None
```

### Fix 3: Use try/except for index access

```python
# Wrong
data = []
first = data[0]

# Correct
try:
    first = data[0]
except IndexError:
    first = None
```

### Fix 4: Use enumerate() when you need both index and value

```python
# Wrong — manual index management is error-prone
data = [10, 20, 30]
i = 0
while i < len(data):
    print(f"{i}: {data[i]}")
    i += 1

# Correct
for i, value in enumerate(data):
    print(f"{i}: {value}")
```

### Fix 5: Use slicing to safely access sub-ranges

```python
# Wrong
items = [1, 2, 3]
subset = [items[0], items[1], items[2], items[3]]  # IndexError

# Correct — slicing never raises IndexError
subset = items[:4]  # Returns [1, 2, 3] — no error
```

### Fix 6: Don't modify a list while iterating by index

```python
# Wrong
data = [10, 20, 30, 40, 50]
for i in range(len(data)):
    if data[i] % 20 == 0:
        del data[i]

# Correct — iterate over a copy or build a new list
data = [10, 20, 30, 40, 50]
data = [x for x in data if x % 20 != 0]
print(data)  # [10, 30, 50]
```

## Related Errors

- [KeyError](../keyerror) — missing key in a dictionary (same concept, different data structure).
- [ValueError](../valueerror) — value is wrong but the index/key exists.
- [TypeError](../typeerror) — wrong type used for indexing (e.g., indexing a string with a float).
