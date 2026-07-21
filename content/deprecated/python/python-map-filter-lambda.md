---
title: "[Solution] Deprecated Function Migration: map/filter with lambda to list comprehensions"
description: "Migrate from deprecated map/filter with lambda to list comprehensions in Python."
deprecated_function: "map(lambda x, ...)"
replacement_function: "list comprehension"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: map/filter with lambda to list comprehensions

The `map(lambda x, ...)` has been deprecated in favor of `list comprehension`.

## Migration Guide

In Python 3, map and filter return lazy iterators. List comprehensions are more readable.

## Before (Deprecated)

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## After (Modern)

```python
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

## Key Differences

- List comprehensions are more readable
- Faster than map/filter for simple operations
- Use generator expressions for memory efficiency
