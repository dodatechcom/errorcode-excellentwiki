---
title: "[Solution] Python ImportError: alembic not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: alembic not found or ModuleNotFoundError: No module named 'alembic'. Install alembic properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: alembic not found — ModuleNotFoundError Fix

An `ImportError: alembic not found` or `ModuleNotFoundError: No module named 'alembic'` means Python cannot locate the alembic package.

## What This Error Means

alembic is a database migration tool for SQLAlchemy. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: alembic not installed
from alembic import command  # ModuleNotFoundError: No module named 'alembic'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install alembic
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install alembic
python -c "import alembic; print(alembic.__version__)"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-sqlmodel" >}} — ImportError: sqlmodel
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
