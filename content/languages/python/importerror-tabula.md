---
title: "[Solution] Python ImportError: tabula not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: tabula not found or ModuleNotFoundError: No module named 'tabula'. Install tabula-py properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "tabula", "module-not-found", "pip", "pdf"]
weight: 5
---

# ImportError: tabula not found — ModuleNotFoundError Fix

An `ImportError: tabula not found` or `ModuleNotFoundError: No module named 'tabula'` means Python cannot locate the tabula-py package.

## What This Error Means

tabula-py is a Python wrapper for tabula-java for extracting tables from PDFs. The package is installed as `tabula-py` but imported as `tabula`.

## Common Causes

```python
# Cause 1: tabula-py not installed
import tabula  # ModuleNotFoundError

# Cause 2: Java not installed
# tabula-py requires Java Runtime Environment
```

## How to Fix

### Fix 1: Install Java and tabula-py

```bash
# Install Java (Ubuntu/Debian)
sudo apt-get install default-jre

# Install tabula-py
pip install tabula-py
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install tabula-py
python -c "import tabula; print('OK')"
```

## Related Errors

- {{< relref "importerror-pdfminer" >}} — ImportError: pdfminer
- {{< relref "importerror-camelot" >}} — ImportError: camelot
- {{< relref "importerror-pypdf" >}} — ImportError: pypdf
