---
title: "[Solution] Deprecated Function Migration: sorted with cmp to key function"
description: "Migrate from deprecated cmp parameter in sorted to key function."
deprecated_function: "sorted(list, cmp=func)"
replacement_function: "sorted(list, key=func)"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: sorted with cmp to key function

The `sorted(list, cmp=func)` has been deprecated in favor of `sorted(list, key=func)`.

## Migration Guide

key function is faster and more Pythonic

The cmp parameter was removed in Python 3. Use key parameter instead.

## Before (Deprecated)

```python
from functools import cmp_to_key
sorted(items, key=cmp_to_key(compare_func))
```

## After (Modern)

```python
sorted(items, key=lambda x: x.age)
from operator import attrgetter
sorted(items, key=attrgetter('age', 'name'))
```

## Key Differences

- key function is applied once per element
- cmp function is called O(n log n) times
- key is much faster for large lists
- Use functools.cmp_to_key if needed
