---
title: "[Solution] Python ImportError: pandas not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pandas not found or ModuleNotFoundError: No module named 'pandas'. Install Pandas properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "pandas", "module-not-found", "pip", "data-analysis"]
weight: 5
---

# ImportError: pandas not found — ModuleNotFoundError Fix

An `ImportError: pandas not found` or `ModuleNotFoundError: No module named 'pandas'` means Python cannot locate the Pandas package.

## What This Error Means

Pandas is a data analysis and manipulation library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: Pandas not installed
import pandas  # ModuleNotFoundError: No module named 'pandas'

# Cause 2: Installed for wrong Python version
# Cause 3: Virtual environment doesn't have Pandas
```

## How to Fix

### Fix 1: Install Pandas with pip

```bash
pip install pandas

# For a specific version
pip install pandas==2.1.4

# With optional dependencies
pip install pandas[all]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pandas
python -c "import pandas; print(pandas.__version__)"
```

### Fix 3: Install with conda

```bash
conda install pandas
```

## Related Errors

- {{< relref "importerror-numpy" >}} — ImportError: numpy
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
- {{< relref "importerror-polars" >}} — ImportError: polars
