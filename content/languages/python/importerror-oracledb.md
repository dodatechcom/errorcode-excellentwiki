---
title: "[Solution] Python ImportError: oracledb not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: oracledb not found or ModuleNotFoundError: No module named 'oracledb'. Install oracledb properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "oracledb", "module-not-found", "pip", "oracle"]
weight: 5
---

# ImportError: oracledb not found — ModuleNotFoundError Fix

An `ImportError: oracledb not found` or `ModuleNotFoundError: No module named 'oracledb'` means Python cannot locate the oracledb package.

## What This Error Means

oracledb is the Oracle Database Python driver. It is the successor to cx_Oracle. It is not part of the standard library.

## Common Causes

```python
# Cause 1: oracledb not installed
import oracledb  # ModuleNotFoundError: No module named 'oracledb'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install oracledb

# For a specific version
pip install oracledb==2.0.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install oracledb
python -c "import oracledb; print(oracledb.__version__)"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-pymysql" >}} — ImportError: pymysql
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
