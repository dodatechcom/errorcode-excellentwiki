---
title: "[Solution] Python ImportError: pyarrow not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pyarrow not found or ModuleNotFoundError: No module named 'pyarrow'. Install PyArrow properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "pyarrow", "module-not-found", "pip", "arrow"]
weight: 5
---

# ImportError: pyarrow not found — ModuleNotFoundError Fix

An `ImportError: pyarrow not found` or `ModuleNotFoundError: No module named 'pyarrow'` means Python cannot locate the PyArrow package.

## What This Error Means

PyArrow is a cross-language development platform for in-memory data. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pyarrow not installed
import pyarrow  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pyarrow

# For a specific version
pip install pyarrow==14.0.2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pyarrow
python -c "import pyarrow; print(pyarrow.__version__)"
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-polars" >}} — ImportError: polars
- {{< relref "importerror-dask" >}} — ImportError: dask
