---
title: "[Solution] Python ImportError: auto_gptq not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: auto_gptq not found or ModuleNotFoundError: No module named 'auto_gptq'. Install auto-gptq properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "autogptq", "auto_gptq", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: auto_gptq not found — ModuleNotFoundError Fix

An `ImportError: auto_gptq not found` or `ModuleNotFoundError: No module named 'auto_gptq'` means Python cannot locate the auto-gptq package.

## What This Error Means

auto-gptq is a GPTQ quantization library. The package is installed as `auto-gptq` but imported as `auto_gptq`.

## Common Causes

```python
# Cause 1: auto-gptq not installed
from auto_gptq import AutoGPTQForCausalLM  # ModuleNotFoundError

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install auto-gptq
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install auto-gptq
python -c "from auto_gptq import AutoGPTQForCausalLM; print('OK')"
```

## Related Errors

- {{< relref "importerror-awq" >}} — ImportError: awq
- {{< relref "importerror-bnb" >}} — ImportError: bitsandbytes
- {{< relref "importerror-eetq" >}} — ImportError: eetq
