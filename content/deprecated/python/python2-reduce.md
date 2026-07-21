---
title: "[Solution] Deprecated Function Migration: reduce() to functools.reduce()"
description: "Migrate from Python 2 built-in reduce() to functools.reduce() in Python 3."
deprecated_function: "reduce()"
replacement_function: "functools.reduce()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: reduce() to functools.reduce()

The `reduce()` has been deprecated in favor of `functools.reduce()`.

## Migration Guide

In Python 2, reduce() is a built-in. In Python 3, it was moved to functools.

## Before (Deprecated)

```python
# Python 2
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
```

## After (Modern)

```python
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4])

# Consider using sum() instead
result = sum([1, 2, 3, 4])
```

## Key Differences

- Add from functools import reduce
- Consider using sum/max/min instead
- reduce is still useful for complex aggregations
