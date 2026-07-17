---
title: "[Solution] Python ImportError: chromadb not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: chromadb not found or ModuleNotFoundError: No module named 'chromadb'. Install chromadb properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "chromadb", "module-not-found", "pip", "vector-db"]
weight: 5
---

# ImportError: chromadb not found — ModuleNotFoundError Fix

An `ImportError: chromadb not found` or `ModuleNotFoundError: No module named 'chromadb'` means Python cannot locate the chromadb package.

## What This Error Means

chromadb is an AI-native open-source embedding database. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: chromadb not installed
import chromadb  # ModuleNotFoundError: No module named 'chromadb'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install chromadb
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install chromadb
python -c "import chromadb; print(chromadb.__version__)"
```

## Related Errors

- {{< relref "importerror-pinecone" >}} — ImportError: pinecone
- {{< relref "importerror-weaviate" >}} — ImportError: weaviate
- {{< relref "importerror-qdrant" >}} — ImportError: qdrant
