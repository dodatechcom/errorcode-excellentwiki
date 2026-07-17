---
title: "[Solution] Python TypeError: unhashable type: 'dict'"
description: "Fix Python TypeError: unhashable type: 'dict'. Understand why dictionaries can't be set keys or dict keys, and use frozenset or tuples instead."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["typeerror", "dict", "hashable", "unhashable", "set"]
weight: 5
---

# TypeError: unhashable type: 'dict'

A `TypeError: unhashable type: 'dict'` occurs when you try to use a dictionary as a key in another dictionary or as an element in a set. Mutable objects like `dict`, `list`, and `set` are unhashable because their contents can change, making a stable hash impossible.

## Description

Python requires dictionary keys and set elements to be hashable (immutable). Mutable types (`dict`, `list`, `set`) are not hashable. This error commonly appears when nesting data structures incorrectly.

## Common Causes

```python
# Cause 1: Using a dict as a dictionary key
d = {}
key = {"a": 1}
d[key] = "value"  # TypeError: unhashable type: 'dict'

# Cause 2: Adding a dict to a set
s = set()
s.add({"a": 1})  # TypeError: unhashable type: 'dict'

# Cause 3: Using a dict in a tuple that's used as a dict key
d = {}
key = ({"a": 1},)
d[key] = "value"  # TypeError (tuple containing unhashable element)

# Cause 4: Nested dict used as key
cache = {}
cache[{**params}] = result  # TypeError
```

## How to Fix

### Fix 1: Use a frozenset for set-like dict keys

```python
# Wrong
data = {{1, 2}, {3, 4}}  # TypeError

# Correct
data = {frozenset({1, 2}), frozenset({3, 4})}
```

### Fix 2: Convert dict to a hashable tuple

```python
# Wrong
d = {}
d[{"a": 1}] = "value"  # TypeError

# Correct — convert to sorted tuple of items
d = {}
d[tuple(sorted({"a": 1}.items()))] = "value"
```

### Fix 3: Use nested dicts instead of dict-as-key

```python
# Wrong — using dict key for lookup
cache = {}
cache[params_dict] = result

# Correct — use a nested dict structure
cache = {}
cache[params_dict["type"]][params_dict["id"]] = result
```

### Fix 4: Use json serialization as a key

```python
import json

d = {}
key = json.dumps({"a": 1, "b": 2}, sort_keys=True)
d[key] = "value"
```

## Related Errors

- [TypeError: unhashable type: 'list'](#) — lists are also unhashable
- [TypeError: list indices must be integers](typeerror-list) — list indexing issues
- [TypeError: 'dict' object is not callable](typeerror-method) — dict called as function
