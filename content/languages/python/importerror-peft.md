---
title: "[Solution] Python ImportError: peft not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: peft not found or ModuleNotFoundError: No module named 'peft'. Install peft properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: peft not found — ModuleNotFoundError Fix

An `ImportError: peft not found` or `ModuleNotFoundError: No module named 'peft'` means Python cannot locate the peft package.

## What This Error Means

peft (Parameter-Efficient Fine-Tuning) is a library by Hugging Face. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: peft not installed
from peft import get_peft_model  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install peft
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install peft
python -c "from peft import get_peft_model; print('OK')"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-trl" >}} — ImportError: trl
- {{< relref "importerror-accelerate" >}} — ImportError: accelerate
