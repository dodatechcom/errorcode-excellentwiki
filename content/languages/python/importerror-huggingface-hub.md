---
title: "[Solution] Python ImportError: huggingface_hub not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: huggingface_hub not found or ModuleNotFoundError: No module named 'huggingface_hub'. Install huggingface-hub properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "huggingface-hub", "huggingface_hub", "module-not-found", "pip"]
weight: 5
---

# ImportError: huggingface_hub not found — ModuleNotFoundError Fix

An `ImportError: huggingface_hub not found` or `ModuleNotFoundError: No module named 'huggingface_hub'` means Python cannot locate the huggingface-hub package.

## What This Error Means

huggingface-hub is a client library for the Hugging Face Hub. The package is installed as `huggingface-hub` but imported as `huggingface_hub`.

## Common Causes

```python
# Cause 1: huggingface-hub not installed
from huggingface_hub import snapshot_download  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install huggingface-hub
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install huggingface-hub
python -c "from huggingface_hub import snapshot_download; print('OK')"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-sentence-transformers" >}} — ImportError: sentence_transformers
- {{< relref "importerror-tokenizers" >}} — ImportError: tokenizers
