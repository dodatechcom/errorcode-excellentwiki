---
title: "[Solution] Python ImportError: groq not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: groq not found or ModuleNotFoundError: No module named 'groq'. Install groq properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "groq", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: groq not found — ModuleNotFoundError Fix

An `ImportError: groq not found` or `ModuleNotFoundError: No module named 'groq'` means Python cannot locate the groq package.

## What This Error Means

groq is the Groq Python client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: groq not installed
from groq import Groq  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install groq
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install groq
python -c "import groq; print(groq.__version__)"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-mistral" >}} — ImportError: mistralai
