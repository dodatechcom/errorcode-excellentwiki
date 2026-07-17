---
title: "[Solution] Python ImportError: unsloth not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: unsloth not found or ModuleNotFoundError: No module named 'unsloth'. Install unsloth properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "unsloth", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: unsloth not found — ModuleNotFoundError Fix

An `ImportError: unsloth not found` or `ModuleNotFoundError: No module named 'unsloth'` means Python cannot locate the unsloth package.

## What This Error Means

unsloth is a library for fast LLM fine-tuning. It requires CUDA and specific GPU support.

## Common Causes

```python
# Cause 1: unsloth not installed
from unsloth import FastLanguageModel  # ModuleNotFoundError

# Cause 2: CUDA not available
# unsloth requires GPU with CUDA support
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install unsloth
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install unsloth
python -c "from unsloth import FastLanguageModel; print('OK')"
```

## Related Errors

- {{< relref "importerror-peft" >}} — ImportError: peft
- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-deepspeed" >}} — ImportError: deepspeed
