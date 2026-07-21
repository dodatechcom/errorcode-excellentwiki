---
title: "[Solution] Deprecated Function Migration: map/filter to list comprehensions"
description: "Migrate from deprecated map/filter to list comprehensions."
deprecated_function: "list(map(func, iterable))"
replacement_function: "[func(x) for x in iterable]"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: map/filter to list comprehensions

The `list(map(func, iterable))` has been deprecated in favor of `[func(x) for x in iterable]`.

## Migration Guide

List comprehensions are more Pythonic.

## Before (Deprecated)

```python
result = list(map(str.upper, words))
```

## After (Modern)

```python
result = [w.upper() for w in words]
```

## Key Differences

- List comprehensions are more Pythonic
