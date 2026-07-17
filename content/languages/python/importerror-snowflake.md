---
title: "[Solution] Python ImportError: snowflake.connector not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: snowflake.connector not found or ModuleNotFoundError: No module named 'snowflake'. Install snowflake-connector-python properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: snowflake.connector not found — ModuleNotFoundError Fix

An `ImportError: snowflake.connector not found` or `ModuleNotFoundError: No module named 'snowflake'` means Python cannot locate the snowflake-connector-python package.

## What This Error Means

snowflake-connector-python is the Snowflake Connector for Python. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: snowflake-connector-python not installed
import snowflake.connector  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install snowflake-connector-python
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install snowflake-connector-python
python -c "import snowflake.connector; print('OK')"
```

## Related Errors

- {{< relref "importerror-pymysql" >}} — ImportError: pymysql
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
