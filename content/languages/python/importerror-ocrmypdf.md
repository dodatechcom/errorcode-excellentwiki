---
title: "[Solution] Python ImportError: ocrmypdf not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: ocrmypdf not found or ModuleNotFoundError: No module named 'ocrmypdf'. Install ocrmypdf properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "ocrmypdf", "module-not-found", "pip", "pdf", "ocr"]
weight: 5
---

# ImportError: ocrmypdf not found — ModuleNotFoundError Fix

An `ImportError: ocrmypdf not found` or `ModuleNotFoundError: No module named 'ocrmypdf'` means Python cannot locate the ocrmypdf package.

## What This Error Means

ocrmypdf is a tool for adding OCR text layer to PDFs. It requires Tesseract and Ghostscript.

## Common Causes

```python
# Cause 1: ocrmypdf not installed
import ocrmypdf  # ModuleNotFoundError

# Cause 2: Tesseract or Ghostscript not installed
```

## How to Fix

### Fix 1: Install dependencies and ocrmypdf

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim ghostscript

# Install ocrmypdf
pip install ocrmypdf
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ocrmypdf
python -c "import ocrmypdf; print(ocrmypdf.__version__)"
```

## Related Errors

- {{< relref "importerror-tesseract" >}} — ImportError: pytesseract
- {{< relref "importerror-pdfminer" >}} — ImportError: pdfminer
- {{< relref "importerror-pypdf" >}} — ImportError: pypdf
