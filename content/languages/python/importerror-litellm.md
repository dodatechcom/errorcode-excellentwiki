---
title: "[Solution] Python ImportError: litellm not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: litellm not found or ModuleNotFoundError: No module named 'litellm'. Install litellm properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: litellm not found — ModuleNotFoundError Fix

An `ImportError: litellm not found` or `ModuleNotFoundError: No module named 'litellm'` means Python cannot locate the litellm package.

## What This Error Means

litellm is a unified interface for LLM APIs. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: litellm not installed
import litellm  # ModuleNotFoundError: No module named 'litellm'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install litellm
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install litellm
python -c "import litellm; print(litellm.__version__)"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-langchain" >}} — ImportError: langchain
