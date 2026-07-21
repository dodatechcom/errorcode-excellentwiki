---
title: "[Solution] Deprecated Function Migration: imp.find_module to importlib"
description: "Migrate from deprecated imp.find_module to importlib."
deprecated_function: "imp.find_module(name)"
replacement_function: "importlib.import_module(name)"
languages: ["python"]
deprecated_since: "Python 3.4+"
---

# [Solution] Deprecated Function Migration: imp.find_module to importlib

The `imp.find_module(name)` has been deprecated in favor of `importlib.import_module(name)`.

## Migration Guide

imp module is deprecated.

## Before (Deprecated)

```python
import imp
module_info = imp.find_module('mymodule')
```

## After (Modern)

```python
import importlib
module = importlib.import_module('mymodule')
```

## Key Differences

- importlib is the standard
