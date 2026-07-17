---
title: "[Solution] Python ImportError: llama_index not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: llama_index not found or ModuleNotFoundError: No module named 'llama_index'. Install llama-index properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "llama-index", "llama_index", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: llama_index not found — ModuleNotFoundError Fix

An `ImportError: llama_index not found` or `ModuleNotFoundError: No module named 'llama_index'` means Python cannot locate the llama-index package.

## What This Error Means

llama-index is a framework for building LLM applications. The package is installed as `llama-index` but imported as `llama_index`.

## Common Causes

```python
# Cause 1: llama-index not installed
from llama_index import VectorStoreIndex  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install llama_index  # Wrong! Should be llama-index
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install llama-index

# NOT: pip install llama_index
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install llama-index
python -c "import llama_index; print(llama_index.__version__)"
```

## Related Errors

- {{< relref "importerror-langchain" >}} — ImportError: langchain
- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-transformers" >}} — ImportError: transformers
