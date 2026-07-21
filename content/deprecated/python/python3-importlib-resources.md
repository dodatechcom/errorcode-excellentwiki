---
title: "[Solution] Deprecated Function Migration: pkg_resources to importlib.resources"
description: "Migrate from deprecated pkg_resources to importlib.resources."
deprecated_function: "pkg_resources.resource_string()"
replacement_function: "importlib.resources.files()"
languages: ["python"]
deprecated_since: "Python 3.7+"
---

# [Solution] Deprecated Function Migration: pkg_resources to importlib.resources

The `pkg_resources.resource_string()` has been deprecated in favor of `importlib.resources.files()`.

## Migration Guide

importlib.resources is faster.

## Before (Deprecated)

```python
import pkg_resources
data = pkg_resources.resource_string('pkg', 'data.txt')
```

## After (Modern)

```python
from importlib import resources
data = resources.files('pkg').joinpath('data.txt').read_bytes()
```

## Key Differences

- importlib.resources is faster
