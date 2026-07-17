---
title: "[Solution] Python ImportError: sqlmodel not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sqlmodel not found or ModuleNotFoundError: No module named 'sqlmodel'. Install SQLModel properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: sqlmodel not found — ModuleNotFoundError Fix

An `ImportError: sqlmodel not found` or `ModuleNotFoundError: No module named 'sqlmodel'` means Python cannot locate the SQLModel package.

## What This Error Means

SQLModel is a library for interacting with SQL databases from Python code, built on SQLAlchemy and Pydantic. It is not part of the standard library.

## Common Causes

```python
# Cause 1: sqlmodel not installed
from sqlmodel import SQLModel  # ModuleNotFoundError: No module named 'sqlmodel'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install sqlmodel
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install sqlmodel
python -c "from sqlmodel import SQLModel; print('OK')"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
- {{< relref "importerror-alembic" >}} — ImportError: alembic
