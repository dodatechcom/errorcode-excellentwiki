---
title: "[Solution] Python ImportError: docx not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: docx not found or ModuleNotFoundError: No module named 'docx'. Install python-docx properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "python-docx", "docx", "module-not-found", "pip", "docx"]
weight: 5
---

# ImportError: docx not found — ModuleNotFoundError Fix

An `ImportError: docx not found` or `ModuleNotFoundError: No module named 'docx'` means Python cannot locate the python-docx package.

## What This Error Means

python-docx is a library for creating and modifying DOCX files. The package is installed as `python-docx` but imported as `docx`.

## Common Causes

```python
# Cause 1: python-docx not installed
from docx import Document  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install docx  # Wrong! Should be python-docx
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install python-docx

# NOT: pip install docx
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install python-docx
python -c "from docx import Document; print('OK')"
```

## Related Errors

- {{< relref "importerror-docx2txt" >}} — ImportError: docx2txt
- {{< relref "importerror-openpyxl" >}} — ImportError: openpyxl
- {{< relref "importerror-xlsxwriter" >}} — ImportError: xlsxwriter
