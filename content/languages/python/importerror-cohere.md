---
title: "[Solution] Python ImportError: cohere not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: cohere not found or ModuleNotFoundError: No module named 'cohere'. Install cohere properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "cohere", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: cohere not found — ModuleNotFoundError Fix

An `ImportError: cohere not found` or `ModuleNotFoundError: No module named 'cohere'` means Python cannot locate the cohere package.

## What This Error Means

cohere is the Cohere Python client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: cohere not installed
import cohere  # ModuleNotFoundError: No module named 'cohere'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install cohere
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install cohere
python -c "import cohere; print(cohere.__version__)"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-langchain" >}} — ImportError: langchain
