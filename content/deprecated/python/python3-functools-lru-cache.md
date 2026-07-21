---
title: "[Solution] Deprecated Function Migration: functools.lru_cache maxsize to functools.cache"
description: "Migrate from deprecated functools.lru_cache(maxsize=None) to functools.cache."
deprecated_function: "functools.lru_cache(maxsize=None)"
replacement_function: "functools.cache"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: functools.lru_cache maxsize to functools.cache

The `functools.lru_cache(maxsize=None)` has been deprecated in favor of `functools.cache`.

## Migration Guide

functools.cache is simpler.

## Before (Deprecated)

```python
@functools.lru_cache(maxsize=None)
def compute(x):
```

## After (Modern)

```python
@functools.cache
def compute(x):
```

## Key Differences

- functools.cache is simpler
