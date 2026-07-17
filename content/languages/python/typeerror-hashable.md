---
title: "[Solution] Python TypeError: unhashable type — 'dict' / 'list' Fix"
description: "Fix Python TypeError: unhashable type 'dict' or 'list'. Understand hashability, convert dicts to tuples, and use frozenset for set operations."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError: unhashable type — 'dict' / 'list'

A `TypeError` with `unhashable type: 'dict'` (or `'list'`) is raised when you try to use a mutable container (dict, list, set) as a dictionary key or as an element of a set. Python requires hashable (immutable) types for keys and set members.

## Description

A hashable object must have a `__hash__()` method that returns the same value for the object's lifetime. Mutable types like `dict`, `list`, and `set` cannot be hashed because their content can change, which would invalidate the hash.

Common patterns:

- **Using a dict as a dict key** — `{my_dict: "value"}`.
- **Using a list in a set** — `{[1, 2, 3]}`.
- **Using a dict in a set** — `{{"a": 1}}`.
- **Passing a dict to a function that requires hashable keys**.

## Common Causes

```python
# Cause 1: Using a dict as a dictionary key
my_dict = {"a": 1}
lookup = {my_dict: "found"}  # TypeError: unhashable type: 'dict'

# Cause 2: Using a list in a set
my_list = [1, 2, 3]
s = {my_list}  # TypeError: unhashable type: 'list'

# Cause 3: Using a dict in a set
s = {{"a": 1}}  # TypeError: unhashable type: 'dict'

# Cause 4: Nested dicts in a set of tuples
data = [{"x": 1}, {"y": 2}]
unique = set(data)  # TypeError

# Cause 5: Using a list as a default dict key
cache = {}
cache[[1, 2, 3]] = "cached"  # TypeError
```

## How to Fix

### Fix 1: Convert dicts to tuples of sorted items

```python
# Wrong
my_dict = {"a": 1, "b": 2}
lookup = {my_dict: "found"}

# Correct — convert to frozenset of items
key = frozenset(my_dict.items())
lookup = {key: "found"}

# Or use a tuple of sorted items
key = tuple(sorted(my_dict.items()))
lookup = {key: "found"}
```

### Fix 2: Convert lists to tuples

```python
# Wrong
my_list = [1, 2, 3]
s = {my_list}

# Correct — tuples are hashable
s = {tuple(my_list)}

# Or use frozenset if order doesn't matter
s = {frozenset(my_list)}
```

### Fix 3: Use a different data structure

```python
# Wrong — using a dict as a key
data = {}
data[{"x": 1}] = "value"

# Correct — use a nested dict or namedtuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
data = {}
data[Point(1, 2)] = "value"

# Or use a string key
data = {}
data[str({"x": 1})] = "value"
```

### Fix 4: Use JSON string as a hashable key

```python
import json

# Wrong
cache = {}
cache[{"query": "SELECT *"}] = result

# Correct — JSON string is hashable
cache = {}
cache[json.dumps({"query": "SELECT *"}, sort_keys=True)] = result
```

### Fix 5: Use a custom hashable wrapper class

```python
class HashableDict:
    def __init__(self, d):
        self._d = d
        self._hash = hash(tuple(sorted(d.items())))

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self._d == other._d

# Usage
cache = {}
cache[HashableDict({"a": 1})] = "found"
```

## Examples

This error commonly occurs when:

- Building a cache where the keys are configuration dicts
- Trying to deduplicate a list of dicts using a set
- Using a dict as a key in memoization decorators
- Serializing nested structures to JSON and using the dict as a key

## Related Errors

- [TypeError: not hashable](#) — using a custom object as a dict key without `__hash__`
- [TypeError: argument of type 'NoneType' is not iterable](typeerror-none) — related None handling issues
- [KeyError](#) — dictionary key not found
