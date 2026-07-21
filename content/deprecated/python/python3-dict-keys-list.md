---
title: "[Solution] Deprecated Function Migration: dict.keys() to list(dict.keys())"
description: "Migrate from deprecated dict.keys() to list conversion."
deprecated_function: "dict.keys()"
replacement_function: "list(dict.keys())"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: dict.keys() to list(dict.keys())

The `dict.keys()` has been deprecated in favor of `list(dict.keys())`.

## Migration Guide

dict.keys() returns view, not list.

## Before (Deprecated)

```python
keys = d.keys()
keys.append('new')
```

## After (Modern)

```python
keys = list(d.keys())
keys.append('new')
```

## Key Differences

- dict.keys() returns view
