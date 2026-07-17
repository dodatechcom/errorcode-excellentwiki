---
title: "[Solution] Python ImportError: psycopg2 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: psycopg2 not found or ModuleNotFoundError: No module named 'psycopg2'. Install psycopg2 properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "psycopg2", "module-not-found", "pip", "postgresql"]
weight: 5
---

# ImportError: psycopg2 not found — ModuleNotFoundError Fix

An `ImportError: psycopg2 not found` or `ModuleNotFoundError: No module named 'psycopg2'` means Python cannot locate the psycopg2 package.

## What This Error Means

psycopg2 is the most popular PostgreSQL adapter for Python. It requires libpq-dev to be installed on the system.

## Common Causes

```python
# Cause 1: psycopg2 not installed
import psycopg2  # ModuleNotFoundError: No module named 'psycopg2'

# Cause 2: Missing system dependencies (libpq-dev)
# pip install psycopg2 fails with compilation errors
```

## How to Fix

### Fix 1: Install with pip

```bash
# Install system dependencies first (Ubuntu/Debian)
sudo apt-get install libpq-dev python3-dev

# Then install psycopg2
pip install psycopg2

# Or use psycopg2-binary (no system dependencies needed)
pip install psycopg2-binary
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install psycopg2-binary
python -c "import psycopg2; print(psycopg2.__version__)"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-pymysql" >}} — ImportError: pymysql
- {{< relref "importerror-oracledb" >}} — ImportError: oracledb
