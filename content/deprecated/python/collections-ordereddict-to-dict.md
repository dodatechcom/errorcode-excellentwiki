---
title: "[Solution] Deprecated Function Migration: collections.OrderedDict to dict"
description: "Migrate from collections.OrderedDict to built-in dict in Python 3.7+ where dicts preserve insertion order."
deprecated_function: "collections.OrderedDict"
replacement_function: "dict"
languages: ["python"]
deprecated_since: "Python 3.7+"
---

# [Solution] Deprecated Function Migration: collections.OrderedDict to dict

The `collections.OrderedDict` has been deprecated in favor of `dict`.

## Migration Guide

Since Python 3.7, built-in dict preserves insertion order as part of the language specification. OrderedDict is no longer necessary for most use cases.

## Before (Deprecated)

```python
from collections import OrderedDict

data = OrderedDict()
data["banana"] = 3
data["apple"] = 1
data["cherry"] = 2

for key, value in data.items():
    print(key, value)
```

## After (Modern)

```python
data = {}
data["banana"] = 3
data["apple"] = 1
data["cherry"] = 2

for key, value in data.items():
    print(key, value)  # banana, apple, cherry

# Equality is value-based (order does not matter)
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)  # True
```

## Key Differences

- dict is ordered since Python 3.7+
- Keep OrderedDict only for popitem(last=False) FIFO
- Keep OrderedDict for order-sensitive equality
