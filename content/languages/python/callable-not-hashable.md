---
title: "[Solution] Python TypeError — Unhashable Type"
description: "Fix Python TypeError: unhashable type when using mutable objects as dictionary keys or in sets. Learn about hashability and how to fix it."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "unhashable", "hash", "dict", "set"]
weight: 5
---

# TypeError — Unhashable Type

A `TypeError` with the message "unhashable type: 'X'" is raised when you try to use a mutable object (like a list, dict, or set) as a dictionary key or as a set element. Only hashable (immutable) objects can be used as dictionary keys or set members.

## Description

Hashable objects have a `__hash__()` method that returns a consistent integer value. Immutable types like `int`, `str`, `tuple`, and `frozenset` are hashable. Mutable types like `list`, `dict`, and `set` are not hashable because their contents can change, which would invalidate the hash.

Common patterns:

- **Using list as dict key** — `{[1, 2]: "value"}`.
- **Using dict as set element** — `{{"key": "value"}}`.
- **Using list in set** — `{{1, 2}, [3, 4]}`.
- **Nested mutable objects in tuple** — `hash(([1, 2], 3))`.

## Common Causes

```python
# Cause 1: Using list as dict key
data = {[1, 2, 3]: "value"}  # TypeError: unhashable type: 'list'

# Cause 2: Using dict as set element
data = {{"key": "value"}}  # TypeError: unhashable type: 'dict'

# Cause 3: Using list in set
my_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# Cause 4: Nested mutable objects in tuple
key = ([1, 2], [3, 4])
hash(key)  # TypeError: unhashable type: 'list'
```

## Solutions

### Fix 1: Convert mutable objects to immutable ones

```python
# Wrong
data = {[1, 2, 3]: "value"}  # TypeError

# Correct — use tuple instead of list
data = {(1, 2, 3): "value"}
```

### Fix 2: Use frozenset instead of set

```python
# Wrong
data = {{1, 2, 3}: "value"}  # TypeError

# Correct — use frozenset
data = {frozenset({1, 2, 3}): "value"}
```

### Fix 3: Use string representation as key

```python
# Wrong
data = {[1, 2, 3]: "value"}  # TypeError

# Correct — use string representation
import json
data = {json.dumps([1, 2, 3]): "value"}
```

### Fix 4: Implement __hash__ for custom objects

```python
# Wrong
class MyClass:
    def __init__(self, value):
        self.value = value  # Mutable attribute

obj = MyClass(42)
hash(obj)  # TypeError: unhashable type: 'MyClass'

# Correct — make it hashable
class MyClass:
    def __init__(self, value):
        self._value = value  # Immutable (by convention)

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        return self._value == other._value

obj = MyClass(42)
hash(obj)  # Works
```

### Fix 5: Use default dict or Counter for counting

```python
# Wrong — trying to count with mutable keys
data = {}
items = [[1, 2], [3, 4], [1, 2]]
for item in items:
    data[item] = data.get(item, 0) + 1  # TypeError

# Correct — use frozenset or tuple
data = {}
items = [[1, 2], [3, 4], [1, 2]]
for item in items:
    key = tuple(item)
    data[key] = data.get(key, 0) + 1
```

## Related Errors

- [KeyError](../keyerror) — missing key in dictionary.
- [TypeError](../typeerror) — general type mismatch errors.
- [Set not subscriptable](set-not-subscriptable) — set indexing errors.
