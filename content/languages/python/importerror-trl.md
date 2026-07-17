---
title: "[Solution] Python ImportError: trl not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: trl not found or ModuleNotFoundError: No module named 'trl'. Install trl properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: trl not found — ModuleNotFoundError Fix

An `ImportError: trl not found` or `ModuleNotFoundError: No module named 'trl'` means Python cannot locate the trl package.

## What This Error Means

trl is a library for Transformer Reinforcement Learning. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: trl not installed
from trl import SFTTrainer  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install trl
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install trl
python -c "import trl; print(trl.__version__)"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-peft" >}} — ImportError: peft
- {{< relref "importerror-accelerate" >}} — ImportError: accelerate
