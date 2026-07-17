---
title: "[Solution] Python ImportError: pinecone not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pinecone not found or ModuleNotFoundError: No module named 'pinecone'. Install pinecone properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pinecone not found — ModuleNotFoundError Fix

An `ImportError: pinecone not found` or `ModuleNotFoundError: No module named 'pinecone'` means Python cannot locate the pinecone package.

## What This Error Means

pinecone is the Pinecone Python client for vector database. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pinecone not installed
import pinecone  # ModuleNotFoundError: No module named 'pinecone'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pinecone-client
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pinecone-client
python -c "import pinecone; print(pinecone.__version__)"
```

## Related Errors

- {{< relref "importerror-chromadb" >}} — ImportError: chromadb
- {{< relref "importerror-weaviate" >}} — ImportError: weaviate
- {{< relref "importerror-qdrant" >}} — ImportError: qdrant
