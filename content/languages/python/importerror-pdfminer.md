---
title: "[Solution] Python ImportError: pdfminer not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pdfminer not found or ModuleNotFoundError: No module named 'pdfminer'. Install pdfminer.six properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pdfminer not found — ModuleNotFoundError Fix

An `ImportError: pdfminer not found` or `ModuleNotFoundError: No module named 'pdfminer'` means Python cannot locate the pdfminer.six package.

## What This Error Means

pdfminer.six is a PDF text extraction library. The package is installed as `pdfminer.six` but imported as `pdfminer`.

## Common Causes

```python
# Cause 1: pdfminer.six not installed
from pdfminer.high_level import extract_text  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pdfminer.six
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pdfminer.six
python -c "from pdfminer.high_level import extract_text; print('OK')"
```

## Related Errors

- {{< relref "importerror-pypdf" >}} — ImportError: pypdf
- {{< relref "importerror-tabula" >}} — ImportError: tabula
- {{< relref "importerror-camelot" >}} — ImportError: camelot
