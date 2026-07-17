---
title: "[Solution] Python ImportError: dask not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: dask not found or ModuleNotFoundError: No module named 'dask'. Install dask properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "dask", "module-not-found", "pip", "distributed"]
weight: 5
---

# ImportError: dask not found — ModuleNotFoundError Fix

An `ImportError: dask not found` or `ModuleNotFoundError: No module named 'dask'` means Python cannot locate the dask package.

## What This Error Means

dask is a parallel computing library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: dask not installed
import dask  # ModuleNotFoundError: No module named 'dask'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install dask

# With all optional dependencies
pip install dask[complete]

# With dataframe support
pip install dask[dataframe]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install dask[complete]
python -c "import dask; print(dask.__version__)"
```

## Related Errors

- {{< relref "importerror-modin" >}} — ImportError: modin
- {{< relref "importerror-ray" >}} — ImportError: ray
- {{< relref "importerror-pandas" >}} — ImportError: pandas
