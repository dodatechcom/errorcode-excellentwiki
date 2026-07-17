---
title: "[Solution] Python ImportError: transformers not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: transformers not found or ModuleNotFoundError: No module named 'transformers'. Install transformers properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: transformers not found — ModuleNotFoundError Fix

An `ImportError: transformers not found` or `ModuleNotFoundError: No module named 'transformers'` means Python cannot locate the transformers package.

## What This Error Means

transformers is a library for state-of-the-art NLP by Hugging Face. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: transformers not installed
from transformers import pipeline  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install transformers

# With PyTorch support
pip install transformers[torch]

# With TensorFlow support
pip install transformers[tf-cpu]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install transformers
python -c "import transformers; print(transformers.__version__)"
```

## Related Errors

- {{< relref "importerror-torch" >}} — ImportError: torch
- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-langchain" >}} — ImportError: langchain
