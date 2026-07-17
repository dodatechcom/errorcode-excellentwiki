---
title: "[Solution] Python ImportError: ray not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: ray not found or ModuleNotFoundError: No module named 'ray'. Install ray properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: ray not found — ModuleNotFoundError Fix

An `ImportError: ray not found` or `ModuleNotFoundError: No module named 'ray'` means Python cannot locate the ray package.

## What This Error Means

ray is a distributed computing framework. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: ray not installed
import ray  # ModuleNotFoundError: No module named 'ray'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install ray

# With data support
pip install ray[data]

# With serve support
pip install ray[serve]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ray
python -c "import ray; print(ray.__version__)"
```

## Related Errors

- {{< relref "importerror-modin" >}} — ImportError: modin
- {{< relref "importerror-dask" >}} — ImportError: dask
- {{< relref "importerror-transformers" >}} — ImportError: transformers
