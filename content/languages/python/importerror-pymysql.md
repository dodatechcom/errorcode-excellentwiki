---
title: "[Solution] Python ImportError: pymysql not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pymysql not found or ModuleNotFoundError: No module named 'pymysql'. Install PyMySQL properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "pymysql", "module-not-found", "pip", "mysql"]
weight: 5
---

# ImportError: pymysql not found — ModuleNotFoundError Fix

An `ImportError: pymysql not found` or `ModuleNotFoundError: No module named 'pymysql'` means Python cannot locate the PyMySQL package.

## What This Error Means

PyMySQL is a pure Python MySQL client. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pymysql not installed
import pymysql  # ModuleNotFoundError: No module named 'pymysql'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pymysql

# For a specific version
pip install pymysql==1.1.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pymysql
python -c "import pymysql; print(pymysql.__version__)"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-oracledb" >}} — ImportError: oracledb
