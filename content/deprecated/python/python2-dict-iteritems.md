---
title: "[Solution] Deprecated Function Migration: dict.iteritems() to dict.items()"
description: "Migrate from Python 2 dict.iteritems/itervalues/iterkeys to dict.items/values/keys in Python 3."
deprecated_function: "dict.iteritems()"
replacement_function: "dict.items()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: dict.iteritems() to dict.items()

The `dict.iteritems()` has been deprecated in favor of `dict.items()`.

## Migration Guide

In Python 2, dict.items() returns a list and dict.iteritems() returns an iterator. In Python 3, dict.items() returns a view object.

## Before (Deprecated)

```python
data = {"a": 1, "b": 2}

for key, value in data.iteritems():
    print(key, value)

for key in data.iterkeys():
    print(key)
```

## After (Modern)

```python
data = {"a": 1, "b": 2}

for key, value in data.items():
    print(key, value)

for key in data.keys():
    print(key)

for value in data.values():
    print(value)
```

## Key Differences

- Replace iteritems with items
- Replace iterkeys with keys
- Replace itervalues with values
