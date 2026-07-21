---
title: "[Solution] Deprecated Function Migration: apply() to direct function calls"
description: "Migrate from Python 2 apply() to direct function calls with *args unpacking in Python 3."
deprecated_function: "apply(func, args)"
replacement_function: "func(*args)"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: apply() to direct function calls

The `apply(func, args)` has been deprecated in favor of `func(*args)`.

## Migration Guide

apply() called a function with arguments from a tuple. Use the * operator for argument unpacking.

## Before (Deprecated)

```python
result = apply(function, (arg1, arg2))
result = apply(function, (arg1, arg2), {"key": "value"})
```

## After (Modern)

```python
result = function(arg1, arg2)
result = function(arg1, arg2, key="value")

# With dynamic args
args = (arg1, arg2)
kwargs = {"key": "value"}
result = function(*args, **kwargs)
```

## Key Differences

- Replace apply(func, args) with func(*args)
- Replace apply(func, args, kwargs) with func(*args, **kwargs)
- Direct calls are faster and more readable
