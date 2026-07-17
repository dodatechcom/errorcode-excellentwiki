---
title: "[Solution] Python ImportError: sentence_transformers not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sentence_transformers not found. Install sentence-transformers properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: sentence_transformers not found — ModuleNotFoundError Fix

An `ImportError: sentence_transformers not found` or `ModuleNotFoundError: No module named 'sentence_transformers'` means Python cannot locate the sentence-transformers package.

## What This Error Means

sentence-transformers is a library for computing sentence, text, and image embeddings. The package is installed as `sentence-transformers`.

## Common Causes

```python
# Cause 1: sentence-transformers not installed
from sentence_transformers import SentenceTransformer  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install sentence-transformers
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install sentence-transformers
python -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-huggingface-hub" >}} — ImportError: huggingface_hub
- {{< relref "importerror-tokenizers" >}} — ImportError: tokenizers
