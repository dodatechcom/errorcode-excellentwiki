---
title: "[Solution] Python ImportError: camelot not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: camelot not found or ModuleNotFoundError: No module named 'camelot'. Install camelot-py properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: camelot not found — ModuleNotFoundError Fix

An `ImportError: camelot not found` or `ModuleNotFoundError: No module named 'camelot'` means Python cannot locate the camelot-py package.

## What This Error Means

camelot-py is a library for extracting tables from PDFs. The package is installed as `camelot-py` but imported as `camelot`.

## Common Causes

```python
# Cause 1: camelot-py not installed
import camelot  # ModuleNotFoundError

# Cause 2: Ghostscript not installed
# camelot-py requires Ghostscript for PDF parsing
```

## How to Fix

### Fix 1: Install dependencies and camelot-py

```bash
# Install Ghostscript (Ubuntu/Debian)
sudo apt-get install ghostscript

# Install camelot-py
pip install camelot-py[cv]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install camelot-py[cv]
python -c "import camelot; print('OK')"
```

## Related Errors

- {{< relref "importerror-pdfminer" >}} — ImportError: pdfminer
- {{< relref "importerror-tabula" >}} — ImportError: tabula
- {{< relref "importerror-pypdf" >}} — ImportError: pypdf
