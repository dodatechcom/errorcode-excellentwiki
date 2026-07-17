---
title: "[Solution] Python ImportError: xlsxwriter not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: xlsxwriter not found or ModuleNotFoundError: No module named 'xlsxwriter'. Install XlsxWriter properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "xlsxwriter", "module-not-found", "pip", "excel"]
weight: 5
---

# ImportError: xlsxwriter not found — ModuleNotFoundError Fix

An `ImportError: xlsxwriter not found` or `ModuleNotFoundError: No module named 'xlsxwriter'` means Python cannot locate the XlsxWriter package.

## What This Error Means

XlsxWriter is a library for creating Excel XLSX files. The package is installed as `XlsxWriter` but imported as `xlsxwriter`.

## Common Causes

```python
# Cause 1: XlsxWriter not installed
import xlsxwriter  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install XlsxWriter  # Wrong capitalization sometimes causes issues
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install XlsxWriter
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install XlsxWriter
python -c "import xlsxwriter; print(xlsxwriter.__version__)"
```

## Related Errors

- {{< relref "importerror-openpyxl" >}} — ImportError: openpyxl
- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
