---
title: "[Solution] Deprecated Function Migration: backtick repr to repr() function"
description: "Migrate from Python 2 backtick repr syntax to the repr() function in Python 3."
deprecated_function: "`x`"
replacement_function: "repr(x)"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: backtick repr to repr() function

The ``x`` has been deprecated in favor of `repr(x)`.

## Migration Guide

In Python 2, backticks around an expression called repr() on it. This syntax was removed in Python 3.

## Before (Deprecated)

```python
# Python 2
print `obj`
```

## After (Modern)

```python
# Python 3
print(repr(obj))
print(f"{obj!r}")
```

## Key Differences

- Replace `expr` with repr(expr)
- Use !r in f-strings for repr formatting
