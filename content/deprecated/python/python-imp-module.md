---
title: "[Solution] Deprecated Function Migration: imp module to importlib"
description: "Migrate from deprecated imp module to importlib for dynamic module imports in Python."
deprecated_function: "imp"
replacement_function: "importlib"
languages: ["python"]
deprecated_since: "Python 3.4+"
---

# [Solution] Deprecated Function Migration: imp module to importlib

The `imp` has been deprecated in favor of `importlib`.

## Migration Guide

The imp module has been deprecated since Python 3.4 in favor of importlib.

## Before (Deprecated)

```python
import imp

module = imp.load_source("mymodule", "/path/to/mymodule.py")
result = imp.find_module("mymodule")
```

## After (Modern)

```python
import importlib
import importlib.util

spec = importlib.util.spec_from_file_location("mymodule", "/path/to/mymodule.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

module = importlib.import_module("mymodule")
```

## Key Differences

- Replace imp.load_source with importlib.util.spec_from_file_location
- Replace imp.find_module with importlib.import_module
- Replace imp.reload with importlib.reload
