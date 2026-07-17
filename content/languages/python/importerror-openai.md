---
title: "[Solution] Python ImportError: openai not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: openai not found or ModuleNotFoundError: No module named 'openai'. Install openai properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "openai", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: openai not found — ModuleNotFoundError Fix

An `ImportError: openai not found` or `ModuleNotFoundError: No module named 'openai'` means Python cannot locate the openai package.

## What This Error Means

openai is the OpenAI Python client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: openai not installed
import openai  # ModuleNotFoundError: No module named 'openai'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install openai

# For a specific version
pip install openai==1.6.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install openai
python -c "import openai; print(openai.__version__)"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-langchain" >}} — ImportError: langchain
