---
title: "[Solution] Python ImportError: eetq not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: eetq not found or ModuleNotFoundError: No module named 'eetq'. Install eetq properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "eetq", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: eetq not found — ModuleNotFoundError Fix

An `ImportError: eetq not found` or `ModuleNotFoundError: No module named 'eetq'` means Python cannot locate the eetq package.

## What This Error Means

eetq is an efficient quantization library. It requires CUDA and specific GPU support.

## Common Causes

```python
# Cause 1: eetq not installed
import eetq  # ModuleNotFoundError: No module named 'eetq'

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install eetq
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install eetq
python -c "import eetq; print('OK')"
```

## Related Errors

- {{< relref "importerror-autogptq" >}} — ImportError: auto_gptq
- {{< relref "importerror-awq" >}} — ImportError: awq
- {{< relref "importerror-bnb" >}} — ImportError: bitsandbytes
