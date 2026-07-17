---
title: "[Solution] Python ImportError: langchain not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: langchain not found or ModuleNotFoundError: No module named 'langchain'. Install langchain properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "langchain", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: langchain not found — ModuleNotFoundError Fix

An `ImportError: langchain not found` or `ModuleNotFoundError: No module named 'langchain'` means Python cannot locate the langchain package.

## What This Error Means

langchain is a framework for developing applications powered by LLMs. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: langchain not installed
from langchain.llms import OpenAI  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install langchain

# With community packages
pip install langchain-community
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install langchain
python -c "import langchain; print(langchain.__version__)"
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
- {{< relref "importerror-transformers" >}} — ImportError: transformers
