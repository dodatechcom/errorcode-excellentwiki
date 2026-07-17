---
title: "[Solution] Python ImportError: tokenizers not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: tokenizers not found or ModuleNotFoundError: No module named 'tokenizers'. Install tokenizers properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "tokenizers", "module-not-found", "pip", "nlp"]
weight: 5
---

# ImportError: tokenizers not found — ModuleNotFoundError Fix

An `ImportError: tokenizers not found` or `ModuleNotFoundError: No module named 'tokenizers'` means Python cannot locate the tokenizers package.

## What This Error Means

tokenizers is a fast tokenizer library by Hugging Face. It requires Rust to compile from source.

## Common Causes

```python
# Cause 1: tokenizers not installed
from tokenizers import Tokenizer  # ModuleNotFoundError

# Cause 2: Rust not installed (compilation fails)
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install tokenizers
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install tokenizers
python -c "from tokenizers import Tokenizer; print('OK')"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-huggingface-hub" >}} — ImportError: huggingface_hub
- {{< relref "importerror-sentence-transformers" >}} — ImportError: sentence_transformers
