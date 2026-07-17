---
title: "[Solution] Python ImportError: openpyxl not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: openpyxl not found or ModuleNotFoundError: No module named 'openpyxl'. Install openpyxl properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: openpyxl not found — ModuleNotFoundError Fix

An `ImportError: openpyxl not found` or `ModuleNotFoundError: No module named 'openpyxl'` means Python cannot locate the openpyxl package.

## What This Error Means

openpyxl is a library for reading/writing Excel 2010+ files (.xlsx). It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: openpyxl not installed
import openpyxl  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install openpyxl
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install openpyxl
python -c "import openpyxl; print(openpyxl.__version__)"
```

## Related Errors

- {{< relref "importerror-xlsxwriter" >}} — ImportError: xlsxwriter
- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
