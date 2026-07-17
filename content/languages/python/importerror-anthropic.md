---
title: "[Solution] Python ImportError: anthropic not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: anthropic not found or ModuleNotFoundError: No module named 'anthropic'. Install anthropic properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: anthropic not found — ModuleNotFoundError Fix

An `ImportError: anthropic not found` or `ModuleNotFoundError: No module named 'anthropic'` means Python cannot locate the anthropic package.

## What This Error Means

anthropic is the Anthropic Python client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: anthropic not installed
import anthropic  # ModuleNotFoundError: No module named 'anthropic'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install anthropic
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install anthropic
python -c "import anthropic; print(anthropic.__version__)"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-langchain" >}} — ImportError: langchain
