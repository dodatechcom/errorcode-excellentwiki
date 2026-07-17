---
title: "[Solution] Python ImportError: weaviate not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: weaviate not found or ModuleNotFoundError: No module named 'weaviate'. Install weaviate properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: weaviate not found — ModuleNotFoundError Fix

An `ImportError: weaviate not found` or `ModuleNotFoundError: No module named 'weaviate'` means Python cannot locate the weaviate package.

## What This Error Means

weaviate is the Weaviate Python client for vector search. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: weaviate not installed
import weaviate  # ModuleNotFoundError: No module named 'weaviate'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install weaviate-client
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install weaviate-client
python -c "import weaviate; print(weaviate.__version__)"
```

## Related Errors

- {{< relref "importerror-chromadb" >}} — ImportError: chromadb
- {{< relref "importerror-pinecone" >}} — ImportError: pinecone
- {{< relref "importerror-qdrant" >}} — ImportError: qdrant
