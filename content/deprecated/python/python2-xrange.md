---
title: "[Solution] Deprecated Function Migration: xrange() to range()"
description: "Migrate from Python 2 xrange() to range() in Python 3 for memory-efficient iteration."
deprecated_function: "xrange()"
replacement_function: "range()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: xrange() to range()

The `xrange()` has been deprecated in favor of `range()`.

## Migration Guide

In Python 2, range() creates a list while xrange() returns a lazy iterator. In Python 3, range() behaves like xrange().

## Before (Deprecated)

```python
# Python 2
for i in xrange(1000000):
    print(i)

numbers = list(xrange(10))
```

## After (Modern)

```python
# Python 3
for i in range(1000000):
    print(i)

numbers = list(range(10))
```

## Key Differences

- Replace xrange with range
- range is lazy in Python 3
- Use 2to3 -f range for conversion
