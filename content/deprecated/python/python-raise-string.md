---
title: "[Solution] Deprecated Function Migration: raise string to raise Exception(string)"
description: "Migrate from Python 2 raise string syntax to raise Exception(string) for proper exception handling."
deprecated_function: "raise error"
replacement_function: "raise Exception()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: raise string to raise Exception(string)

The `raise "error"` has been deprecated in favor of `raise Exception("error")`.

## Migration Guide

In Python 2, you could raise a string as an exception. This was removed in Python 3.

## Before (Deprecated)

```python
# Python 2
raise "Something went wrong"
```

## After (Modern)

```python
# Python 3
raise Exception("Something went wrong")
raise ValueError(f"Error: {code}")
```

## Key Differences

- Raise Exception subclasses, not strings
- Use ValueError, TypeError, RuntimeError as appropriate
