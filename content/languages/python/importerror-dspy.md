---
title: "[Solution] Python ImportError: dspy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: dspy not found or ModuleNotFoundError: No module named 'dspy'. Install dspy properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "dspy", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: dspy not found — ModuleNotFoundError Fix

An `ImportError: dspy not found` or `ModuleNotFoundError: No module named 'dspy'` means Python cannot locate the dspy package.

## What This Error Means

dspy is a framework for programming with language models. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: dspy not installed
import dspy  # ModuleNotFoundError: No module named 'dspy'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install dspy-ai
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install dspy-ai
python -c "import dspy; print('OK')"
```

## Related Errors

- {{< relref "importerror-langchain" >}} — ImportError: langchain
- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-transformers" >}} — ImportError: transformers
