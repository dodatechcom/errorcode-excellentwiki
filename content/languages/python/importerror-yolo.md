---
title: "[Solution] Python ImportError: ultralytics not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: ultralytics not found or ModuleNotFoundError: No module named 'ultralytics'. Install ultralytics properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "ultralytics", "yolo", "module-not-found", "pip", "vision"]
weight: 5
---

# ImportError: ultralytics not found — ModuleNotFoundError Fix

An `ImportError: ultralytics not found` or `ModuleNotFoundError: No module named 'ultralytics'` means Python cannot locate the ultralytics package.

## What This Error Means

ultralytics is the YOLO (You Only Look Once) object detection library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: ultralytics not installed
from ultralytics import YOLO  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install ultralytics
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ultralytics
python -c "from ultralytics import YOLO; print('OK')"
```

## Related Errors

- {{< relref "importerror-opencv" >}} — ImportError: cv2
- {{< relref "importerror-pillow" >}} — ImportError: PIL/Pillow
- {{< relref "importerror-torch" >}} — ImportError: torch
