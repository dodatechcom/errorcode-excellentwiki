---
title: "[Solution] Deprecated Function Migration: dict.has_key() to in operator"
description: "Migrate from deprecated dict.has_key() to the in operator in Python for membership testing."
deprecated_function: "dict.has_key()"
replacement_function: "in operator"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: dict.has_key() to in operator

The `dict.has_key()` has been deprecated in favor of `in operator`.

## Migration Guide

The dict.has_key() method was removed in Python 3. Use the in operator for membership testing.

## Before (Deprecated)

```python
data = {"name": "Alice", "age": 30}

if data.has_key("name"):
    print("Name exists")
```

## After (Modern)

```python
data = {"name": "Alice", "age": 30}

if "name" in data:
    print("Name exists")

if "email" not in data:
    print("No email")
```

## Key Differences

- Replace obj.has_key(key) with key in obj
- Replace not obj.has_key(key) with key not in obj
- in works with dicts, sets, lists
