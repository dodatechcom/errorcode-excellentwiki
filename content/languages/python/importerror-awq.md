---
title: "[Solution] Python ImportError: awq not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: awq not found or ModuleNotFoundError: No module named 'awq'. Install autoawq properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: awq not found — ModuleNotFoundError Fix

An `ImportError: awq not found` or `ModuleNotFoundError: No module named 'awq'` means Python cannot locate the autoawq package.

## What This Error Means

autoawq is an AWQ (Activation-aware Weight Quantization) library. It requires CUDA.

## Common Causes

```python
# Cause 1: autoawq not installed
from awq import AutoAWQForCausalLM  # ModuleNotFoundError

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install autoawq
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install autoawq
python -c "from awq import AutoAWQForCausalLM; print('OK')"
```

## Related Errors

- {{< relref "importerror-autogptq" >}} — ImportError: auto_gptq
- {{< relref "importerror-bnb" >}} — ImportError: bitsandbytes
- {{< relref "importerror-eetq" >}} — ImportError: eetq
