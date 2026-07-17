---
title: "[Solution] Python TypeError: list indices must be integers"
description: "Fix Python TypeError: list indices must be integers or slices, not 'str'. Understand list indexing vs dictionary access."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["typeerror", "list", "indexing", "subscript"]
weight: 5
---

# TypeError: list indices must be integers or slices

A `TypeError: list indices must be integers or slices, not 'str'` occurs when you use a non-integer value (like a string or float) to index a list. Lists in Python require integer indices, unlike dictionaries which accept arbitrary hashable keys.

## Description

Lists are zero-indexed sequences that only accept integer keys. This error commonly happens when a developer confuses a list for a dictionary, or when data structures are nested differently than expected.

## Common Causes

```python
# Cause 1: Using string key on a list
items = ["apple", "banana", "cherry"]
print(items["0"])  # TypeError: list indices must be integers

# Cause 2: Using float as index
items = [10, 20, 30]
print(items[1.5])  # TypeError: list indices must be integers

# Cause 3: Wrong data structure assumption
data = [[1, 2], [3, 4]]
print(data["row"])  # TypeError

# Cause 4: List returned where dict was expected
response = [100, 200, 300]
print(response["status"])  # TypeError

# Cause 5: Nested list accessed like a dict
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0]["x"])  # TypeError
```

## How to Fix

### Fix 1: Use integer indices for lists

```python
# Wrong
items = ["apple", "banana", "cherry"]
print(items["first"])  # TypeError

# Correct
print(items[0])  # "apple"
```

### Fix 2: Convert string indices to integers

```python
key = "2"
items = [10, 20, 30]
print(items[int(key)])  # 30
```

### Fix 3: Use a dictionary instead of a list

```python
# Wrong — using list with string keys
data = ["value1", "value2"]
result = data["key"]

# Correct — use a dictionary
data = {"key": "value1", "key2": "value2"}
result = data["key"]
```

### Fix 4: Check data structure at runtime

```python
def safe_get(data, key):
    if isinstance(data, dict):
        return data.get(key)
    elif isinstance(data, (list, tuple)):
        if isinstance(key, int) and 0 <= key < len(data):
            return data[key]
    return None
```

## Related Errors

- [IndexError: list index out of range](../indexerror) — integer index beyond list bounds
- [KeyError: 'X'](#) — dictionary key not found
- [TypeError: unhashable type: 'dict'](# typeerror-dict) — dict as dict key
