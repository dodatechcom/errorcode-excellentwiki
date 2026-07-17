---
title: "[Solution] Python ImportError: qdrant not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: qdrant not found or ModuleNotFoundError: No module named 'qdrant'. Install qdrant properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: qdrant not found — ModuleNotFoundError Fix

An `ImportError: qdrant not found` or `ModuleNotFoundError: No module named 'qdrant'` means Python cannot locate the qdrant-client package.

## What This Error Means

qdrant-client is the Python client for Qdrant vector database. The package is installed as `qdrant-client` but imported as `qdrant`.

## Common Causes

```python
# Cause 1: qdrant-client not installed
from qdrant_client import QdrantClient  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install qdrant-client
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install qdrant-client
python -c "from qdrant_client import QdrantClient; print('OK')"
```

## Related Errors

- {{< relref "importerror-chromadb" >}} — ImportError: chromadb
- {{< relref "importerror-pinecone" >}} — ImportError: pinecone
- {{< relref "importerror-weaviate" >}} — ImportError: weaviate
