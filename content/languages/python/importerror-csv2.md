---
title: "[Solution] Python ImportError: csv module not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: csv module not found. The csv module is part of the standard library."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "csv", "module-not-found", "standard-library"]
weight: 5
---

# ImportError: csv module not found — ModuleNotFoundError Fix

The `csv` module is part of the Python standard library and should not produce an ImportError. This error typically indicates a naming conflict or corrupted Python installation.

## What This Error Means

Common message:

- `ModuleNotFoundError: No module named 'csv'`

## Common Causes

```python
# Cause 1: File named csv.py in your project
# If you have a file named csv.py, it shadows the standard library

# Cause 2: Corrupted Python installation

# Cause 3: Virtual environment issues
```

## How to Fix

### Fix 1: Rename conflicting file

```bash
# Check if you have a file named csv.py
ls csv.py

# Rename it
mv csv.py my_csv_parser.py
```

### Fix 2: Verify standard library

```python
import sys
print(sys.path)

# Check if stdlib is in the path
import csv
print(csv.__file__)
```

### Fix 3: Reinstall Python or recreate virtual environment

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
