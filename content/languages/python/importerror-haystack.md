---
title: "[Solution] Python ImportError: haystack not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: haystack not found or ModuleNotFoundError: No module named 'haystack'. Install haystack-ai properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: haystack not found — ModuleNotFoundError Fix

An `ImportError: haystack not found` or `ModuleNotFoundError: No module named 'haystack'` means Python cannot locate the haystack-ai package.

## What This Error Means

haystack is a framework for building NLP applications. The package is installed as `haystack-ai` but imported as `haystack`.

## Common Causes

```python
# Cause 1: haystack-ai not installed
from haystack import Pipeline  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install haystack-ai
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install haystack-ai
python -c "import haystack; print(haystack.__version__)"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-langchain" >}} — ImportError: langchain
- {{< relref "importerror-openai" >}} — ImportError: openai
