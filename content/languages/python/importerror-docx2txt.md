---
title: "[Solution] Python ImportError: docx2txt not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: docx2txt not found or ModuleNotFoundError: No module named 'docx2txt'. Install docx2txt properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: docx2txt not found — ModuleNotFoundError Fix

An `ImportError: docx2txt not found` or `ModuleNotFoundError: No module named 'docx2txt'` means Python cannot locate the docx2txt package.

## What This Error Means

docx2txt is a library for extracting text from DOCX files. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: docx2txt not installed
import docx2txt  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install docx2txt
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install docx2txt
python -c "import docx2txt; print('OK')"
```

## Related Errors

- {{< relref "importerror-python-docx" >}} — ImportError: docx
- {{< relref "importerror-openpyxl" >}} — ImportError: openpyxl
- {{< relref "importerror-xlsxwriter" >}} — ImportError: xlsxwriter
