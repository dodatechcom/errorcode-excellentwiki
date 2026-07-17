---
title: "[Solution] Python ImportError: pymongo not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pymongo not found or ModuleNotFoundError: No module named 'pymongo'. Install PyMongo properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "pymongo", "module-not-found", "pip", "mongodb"]
weight: 5
---

# ImportError: pymongo not found — ModuleNotFoundError Fix

An `ImportError: pymongo not found` or `ModuleNotFoundError: No module named 'pymongo'` means Python cannot locate the PyMongo package.

## What This Error Means

PyMongo is the official MongoDB driver for Python. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pymongo not installed
import pymongo  # ModuleNotFoundError: No module named 'pymongo'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pymongo

# For a specific version
pip install pymongo==4.6.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pymongo
python -c "import pymongo; print(pymongo.version)"
```

## Related Errors

- {{< relref "testcontainers-mongodb" >}} — MongoDBContainer startup failed
- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
