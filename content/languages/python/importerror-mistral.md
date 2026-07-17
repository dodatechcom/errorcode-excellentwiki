---
title: "[Solution] Python ImportError: mistralai not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: mistralai not found or ModuleNotFoundError: No module named 'mistralai'. Install mistralai properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "mistral", "mistralai", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: mistralai not found — ModuleNotFoundError Fix

An `ImportError: mistralai not found` or `ModuleNotFoundError: No module named 'mistralai'` means Python cannot locate the mistralai package.

## What This Error Means

mistralai is the Mistral AI Python client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: mistralai not installed
from mistralai.client import MistralClient  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install mistralai
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install mistralai
python -c "import mistralai; print('OK')"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-groq" >}} — ImportError: groq
