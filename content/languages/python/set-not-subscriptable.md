---
title: "[Solution] Python TypeError — 'set' Object Is Not Subscriptable"
description: "Fix Python TypeError when trying to subscript a set. Learn why sets don't support indexing and how to work with sets properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "set", "subscript", "index"]
weight: 5
---

# TypeError — 'set' Object Is Not Subscriptable

A `TypeError` with the message "'set' object is not subscriptable" is raised when you try to access a set element using indexing `set[0]` or slicing `set[1:3]`. Sets are unordered collections that don't support indexing.

## Description

Sets in Python are unordered collections of unique elements. Unlike lists and tuples, sets don't maintain insertion order and don't support indexing. You can check membership with `in`, add/remove elements, and perform set operations, but you cannot access elements by position.

Common patterns:

- **Indexing a set** — `my_set[0]`.
- **Slicing a set** — `my_set[1:3]`.
- **Using [] for lookup** — `my_set[key]` (dict syntax on a set).
- **Converting to list implicitly** — code expects a list but receives a set.

## Common Causes

```python
# Cause 1: Indexing a set
my_set = {1, 2, 3}
value = my_set[0]  # TypeError: 'set' object is not subscriptable

# Cause 2: Slicing a set
my_set = {1, 2, 3}
subset = my_set[1:3]  # TypeError: 'set' object is not subscriptable

# Cause 3: Using dict-like access
my_set = {"a", "b", "c"}
value = my_set["a"]  # TypeError

# Cause 4: Code expects list but receives set
def process(items):
    return items[0]  # TypeError if items is a set

process({1, 2, 3})
```

## Solutions

### Fix 1: Convert set to list or tuple for indexing

```python
# Wrong
my_set = {1, 2, 3}
value = my_set[0]  # TypeError

# Correct
my_list = sorted(my_set)  # Convert to sorted list
value = my_list[0]

# Or use a specific conversion
my_list = list(my_set)
value = my_list[0]
```

### Fix 2: Use the 'in' operator for membership testing

```python
# Wrong
my_set = {1, 2, 3}
if my_set[0] == 1:  # TypeError
    print("Found")

# Correct
if 1 in my_set:
    print("Found")
```

### Fix 3: Use pop() to get an arbitrary element

```python
my_set = {1, 2, 3}

# Get and remove an arbitrary element
value = my_set.pop()
print(value)  # Any element from the set
```

### Fix 4: Use a list if you need indexing

```python
# Wrong — using set when you need indexing
my_set = {1, 2, 3}
first = my_set[0]

# Correct — use a list
my_list = [1, 2, 3]
first = my_list[0]  # Returns 1
```

## Related Errors

- [IndexError: list index out of range](index-out-of-range) — index out of bounds.
- [IndexError: tuple index out of range](tuple-index) — tuple indexing errors.
- [KeyError](../keyerror) — missing key in dictionary.
