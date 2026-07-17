---
title: "[Solution] Python ImportError: PIL/Pillow not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: PIL/Pillow not found or ModuleNotFoundError: No module named 'PIL'. Install Pillow properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: PIL/Pillow not found — ModuleNotFoundError Fix

An `ImportError: PIL/Pillow not found` or `ModuleNotFoundError: No module named 'PIL'` means Python cannot locate the Pillow package. Pillow is the PIL fork.

## What This Error Means

Pillow is a image processing library. The package is installed as `Pillow` but imported as `PIL`.

## Common Causes

```python
# Cause 1: Pillow not installed
from PIL import Image  # ModuleNotFoundError: No module named 'PIL'

# Cause 2: Installed wrong package name
pip install pil  # Wrong! Should be Pillow
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install Pillow

# NOT: pip install pil
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install Pillow
python -c "from PIL import Image; print('OK')"
```

## Related Errors

- {{< relref "importerror-opencv" >}} — ImportError: cv2
- {{< relref "importerror-tesseract" >}} — ImportError: pytesseract
- {{< relref "importerror-stable-diffusion" >}} — ImportError: diffusers
