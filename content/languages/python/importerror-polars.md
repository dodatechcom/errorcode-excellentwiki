---
title: "[Solution] Python ImportError: polars not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: polars not found or ModuleNotFoundError: No module named 'polars'. Install polars properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: polars not found — ModuleNotFoundError Fix

An `ImportError: polars not found` or `ModuleNotFoundError: No module named 'polars'` means Python cannot locate the polars package.

## What This Error Means

polars is a fast DataFrame library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: polars not installed
import polars  # ModuleNotFoundError: No module named 'polars'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install polars

# For a specific version
pip install polars==0.20.2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install polars
python -c "import polars; print(polars.__version__)"
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
- {{< relref "importerror-modin" >}} — ImportError: modin
