---
title: "[Solution] Python ImportError: bitsandbytes not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: bitsandbytes not found or ModuleNotFoundError: No module named 'bitsandbytes'. Install bitsandbytes properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: bitsandbytes not found — ModuleNotFoundError Fix

An `ImportError: bitsandbytes not found` or `ModuleNotFoundError: No module named 'bitsandbytes'` means Python cannot locate the bitsandbytes package.

## What This Error Means

bitsandbytes is a library for quantization and training of LLMs. It requires CUDA.

## Common Causes

```python
# Cause 1: bitsandbytes not installed
import bitsandbytes as bnb  # ModuleNotFoundError

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install bitsandbytes
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install bitsandbytes
python -c "import bitsandbytes; print(bitsandbytes.__version__)"
```

## Related Errors

- {{< relref "importerror-autogptq" >}} — ImportError: auto_gptq
- {{< relref "importerror-awq" >}} — ImportError: awq
- {{< relref "importerror-peft" >}} — ImportError: peft
