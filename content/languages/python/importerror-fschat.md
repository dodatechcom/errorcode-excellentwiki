---
title: "[Solution] Python ImportError: fastchat not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: fastchat not found or ModuleNotFoundError: No module named 'fastchat'. Install fastchat properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: fastchat not found — ModuleNotFoundError Fix

An `ImportError: fastchat not found` or `ModuleNotFoundError: No module named 'fastchat'` means Python cannot locate the fastchat package.

## What This Error Means

fastchat is an open platform for training, serving, and evaluating LLM chatbots. The package is installed as `fschat` but imported as `fastchat`.

## Common Causes

```python
# Cause 1: fschat not installed
from fastchat.model import load_model  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install fastchat  # Wrong! Should be fschat
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install fschat

# NOT: pip install fastchat
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install fschat
python -c "from fastchat.model import load_model; print('OK')"
```

## Related Errors

- {{< relref "importerror-vllm" >}} — ImportError: vllm
- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-accelerate" >}} — ImportError: accelerate
