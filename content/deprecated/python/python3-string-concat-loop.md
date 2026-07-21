---
title: "[Solution] Deprecated Function Migration: string concatenation in loop to join"
description: "Migrate from deprecated string concatenation in loop to join."
deprecated_function: "s += item"
replacement_function: "''.join(items)"
languages: ["python"]
deprecated_since: "Python 1.0+"
---

# [Solution] Deprecated Function Migration: string concatenation in loop to join

The `s += item` has been deprecated in favor of `''.join(items)`.

## Migration Guide

join is more efficient.

## Before (Deprecated)

```python
result = ''
for item in items:
    result += item
```

## After (Modern)

```python
result = ''.join(items)
```

## Key Differences

- join is more efficient for strings
