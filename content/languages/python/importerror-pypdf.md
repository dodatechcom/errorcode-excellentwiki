---
title: "[Solution] Python ImportError: pypdf not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pypdf not found or ModuleNotFoundError: No module named 'pypdf'. Install pypdf properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pypdf not found — ModuleNotFoundError Fix

An `ImportError: pypdf not found` or `ModuleNotFoundError: No module named 'pypdf'` means Python cannot locate the pypdf package.

## What This Error Means

pypdf is a PDF processing library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pypdf not installed
from pypdf import PdfReader  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pypdf

# For a specific version
pip install pypdf==3.17.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pypdf
python -c "from pypdf import PdfReader; print('OK')"
```

## Related Errors

- {{< relref "importerror-pdfminer" >}} — ImportError: pdfminer
- {{< relref "importerror-tabula" >}} — ImportError: tabula
- {{< relref "importerror-camelot" >}} — ImportError: camelot
