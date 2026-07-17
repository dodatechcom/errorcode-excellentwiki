---
title: "[Solution] Python ImportError: sqlalchemy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sqlalchemy not found or ModuleNotFoundError: No module named 'sqlalchemy'. Install SQLAlchemy properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: sqlalchemy not found — ModuleNotFoundError Fix

An `ImportError: sqlalchemy not found` or `ModuleNotFoundError: No module named 'sqlalchemy'` means Python cannot locate the SQLAlchemy package.

## What This Error Means

SQLAlchemy is a popular SQL toolkit and ORM for Python. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: SQLAlchemy not installed
import sqlalchemy  # ModuleNotFoundError: No module named 'sqlalchemy'

# Cause 2: Installed for wrong Python version
python3.11 -c "import sqlalchemy"  # ModuleNotFoundError

# Cause 3: Virtual environment doesn't have SQLAlchemy
```

## How to Fix

### Fix 1: Install SQLAlchemy with pip

```bash
pip install sqlalchemy

# For a specific version
pip install sqlalchemy==2.0.23

# With async support
pip install sqlalchemy[asyncio]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install sqlalchemy
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

### Fix 3: Install with conda

```bash
conda install sqlalchemy
```

## Related Errors

- {{< relref "importerror-pymysql" >}} — ImportError: pymysql
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-sqlmodel" >}} — ImportError: sqlmodel
