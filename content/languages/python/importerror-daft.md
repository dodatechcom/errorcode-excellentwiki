---
title: "[Solution] Python ImportError: daft not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: daft not found or ModuleNotFoundError: No module named 'daft'. Install daft properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "daft", "module-not-found", "pip", "distributed"]
weight: 5
---

# ImportError: daft not found — ModuleNotFoundError Fix

An `ImportError: daft not found` or `ModuleNotFoundError: No module named 'daft'` means Python cannot locate the daft package.

## What This Error Means

daft is a distributed DataFrame library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: daft not installed
import daft  # ModuleNotFoundError: No module named 'daft'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install getdaft
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install getdaft
python -c "import daft; print(daft.__version__)"
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-dask" >}} — ImportError: dask
- {{< relref "importerror-ray" >}} — ImportError: ray
