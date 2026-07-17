---
title: "[Solution] Python ImportError: pytesseract not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pytesseract not found or ModuleNotFoundError: No module named 'pytesseract'. Install pytesseract properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pytesseract not found — ModuleNotFoundError Fix

An `ImportError: pytesseract not found` or `ModuleNotFoundError: No module named 'pytesseract'` means Python cannot locate the pytesseract package.

## What This Error Means

pytesseract is a Python wrapper for Google's Tesseract-OCR Engine. It requires Tesseract to be installed on the system.

## Common Causes

```python
# Cause 1: pytesseract not installed
import pytesseract  # ModuleNotFoundError

# Cause 2: Tesseract not installed on system
# pytesseract needs Tesseract binary
```

## How to Fix

### Fix 1: Install Tesseract and pytesseract

```bash
# Install Tesseract (Ubuntu/Debian)
sudo apt-get install tesseract-ocr

# Install pytesseract
pip install pytesseract
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pytesseract
python -c "import pytesseract; print('OK')"
```

## Related Errors

- {{< relref "importerror-pillow" >}} — ImportError: PIL/Pillow
- {{< relref "importerror-opencv" >}} — ImportError: cv2
- {{< relref "importerror-pdfminer" >}} — ImportError: pdfminer
