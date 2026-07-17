---
title: "[Solution] Python ImportError: dbt not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: dbt not found or ModuleNotFoundError: No module named 'dbt'. Install dbt properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: dbt not found — ModuleNotFoundError Fix

An `ImportError: dbt not found` or `ModuleNotFoundError: No module named 'dbt'` means Python cannot locate the dbt package.

## What This Error Means

dbt (data build tool) is a data transformation tool. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: dbt not installed
# Command: dbt --version
# ModuleNotFoundError: No module named 'dbt'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
# Install dbt core
pip install dbt-core

# Install specific adapter (e.g., PostgreSQL)
pip install dbt-postgres

# Install specific adapter (e.g., Snowflake)
pip install dbt-snowflake
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install dbt-core dbt-postgres
dbt --version
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-pyspark" >}} — ImportError: pyspark
