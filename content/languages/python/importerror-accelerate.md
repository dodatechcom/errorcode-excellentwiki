---
title: "[Solution] Python ImportError: accelerate not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: accelerate not found or ModuleNotFoundError: No module named 'accelerate'. Install accelerate properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "accelerate", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: accelerate not found — ModuleNotFoundError Fix

An `ImportError: accelerate not found` or `ModuleNotFoundError: No module named 'accelerate'` means Python cannot locate the accelerate package.

## What This Error Means

accelerate is a library by Hugging Face for running transformers with mixed precision and distributed training.

## Common Causes

```python
# Cause 1: accelerate not installed
from accelerate import Accelerator  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install accelerate
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install accelerate
python -c "from accelerate import Accelerator; print('OK')"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-peft" >}} — ImportError: peft
- {{< relref "importerror-deepspeed" >}} — ImportError: deepspeed
