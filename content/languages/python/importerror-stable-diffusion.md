---
title: "[Solution] Python ImportError: diffusers not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: diffusers not found or ModuleNotFoundError: No module named 'diffusers'. Install diffusers properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "diffusers", "stable-diffusion", "module-not-found", "pip", "image"]
weight: 5
---

# ImportError: diffusers not found — ModuleNotFoundError Fix

An `ImportError: diffusers not found` or `ModuleNotFoundError: No module named 'diffusers'` means Python cannot locate the diffusers package.

## What This Error Means

diffusers is a Hugging Face library for diffusion models (Stable Diffusion). It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: diffusers not installed
from diffusers import StableDiffusionPipeline  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install diffusers

# With torch support
pip install diffusers[torch]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install diffusers
python -c "from diffusers import StableDiffusionPipeline; print('OK')"
```

## Related Errors

- {{< relref "importerror-pillow" >}} — ImportError: PIL/Pillow
- {{< relref "importerror-opencv" >}} — ImportError: cv2
- {{< relref "importerror-torch" >}} — ImportError: torch
