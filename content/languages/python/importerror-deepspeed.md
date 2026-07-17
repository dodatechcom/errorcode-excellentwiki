---
title: "[Solution] Python ImportError: deepspeed not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: deepspeed not found or ModuleNotFoundError: No module named 'deepspeed'. Install deepspeed properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: deepspeed not found — ModuleNotFoundError Fix

An `ImportError: deepspeed not found` or `ModuleNotFoundError: No module named 'deepspeed'` means Python cannot locate the deepspeed package.

## What This Error Means

deepspeed is a deep learning optimization library. It requires CUDA and specific GPU support.

## Common Causes

```python
# Cause 1: deepspeed not installed
import deepspeed  # ModuleNotFoundError

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install deepspeed
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install deepspeed
python -c "import deepspeed; print(deepspeed.__version__)"
```

## Related Errors

- {{< relref "importerror-peft" >}} — ImportError: peft
- {{< relref "importerror-accelerate" >}} — ImportError: accelerate
- {{< relref "importerror-unsloth" >}} — ImportError: unsloth
