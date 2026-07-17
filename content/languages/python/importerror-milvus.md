---
title: "[Solution] Python ImportError: pymilvus not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pymilvus not found or ModuleNotFoundError: No module named 'pymilvus'. Install pymilvus properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pymilvus not found — ModuleNotFoundError Fix

An `ImportError: pymilvus not found` or `ModuleNotFoundError: No module named 'pymilvus'` means Python cannot locate the pymilvus package.

## What This Error Means

pymilvus is the Python SDK for Milvus vector database. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pymilvus not installed
from pymilvus import connections  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pymilvus
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pymilvus
python -c "import pymilvus; print(pymilvus.__version__)"
```

## Related Errors

- {{< relref "importerror-chromadb" >}} — ImportError: chromadb
- {{< relref "importerror-qdrant" >}} — ImportError: qdrant
- {{< relref "importerror-pinecone" >}} — ImportError: pinecone
