---
title: "[Solution] Python ImportError: cv2 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: cv2 not found or ModuleNotFoundError: No module named 'cv2'. Install opencv-python properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: cv2 not found — ModuleNotFoundError Fix

An `ImportError: cv2 not found` or `ModuleNotFoundError: No module named 'cv2'` means Python cannot locate the OpenCV package.

## What This Error Means

OpenCV is a computer vision library. The package is installed as `opencv-python` but imported as `cv2`.

## Common Causes

```python
# Cause 1: opencv-python not installed
import cv2  # ModuleNotFoundError: No module named 'cv2'

# Cause 2: Installed wrong package name
pip install opencv  # Wrong! Should be opencv-python
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install opencv-python

# NOT: pip install opencv

# With contrib modules
pip install opencv-contrib-python
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install opencv-python
python -c "import cv2; print(cv2.__version__)"
```

## Related Errors

- {{< relref "importerror-pillow" >}} — ImportError: PIL/Pillow
- {{< relref "importerror-yolo" >}} — ImportError: ultralytics
- {{< relref "importerror-tesseract" >}} — ImportError: pytesseract
