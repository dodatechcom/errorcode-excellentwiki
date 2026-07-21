---
title: "[Solution] Deprecated Function Migration: bool() on collections to explicit check"
description: "Migrate from deprecated bool() on collections to explicit len() check."
deprecated_function: "bool(collection)"
replacement_function: "len(collection) > 0"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: bool() on collections to explicit check

The `bool(collection)` has been deprecated in favor of `len(collection) > 0`.

## Migration Guide

Explicit is better than implicit

bool() on collections relies on __bool__/__len__. Explicit len() is clearer.

## Before (Deprecated)

```python
if bool(my_list):
    process(my_list)
```

## After (Modern)

```python
if len(my_list) > 0:
    process(my_list)

# Or truthiness check
if my_list:
    process(my_list)
```

## Key Differences

- len() is explicit and readable
- if collection: works for truthiness
- bool() adds unnecessary wrapping
- Use len() for explicit length checks
