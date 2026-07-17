---
title: "[Solution] Python ImportError: sqlglot not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sqlglot not found or ModuleNotFoundError: No module named 'sqlglot'. Install sqlglot properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "sqlglot", "module-not-found", "pip", "sql"]
weight: 5
---

# ImportError: sqlglot not found — ModuleNotFoundError Fix

An `ImportError: sqlglot not found` or `ModuleNotFoundError: No module named 'sqlglot'` means Python cannot locate the sqlglot package.

## What This Error Means

sqlglot is a SQL parser, transpiler, and optimizer. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: sqlglot not installed
import sqlglot  # ModuleNotFoundError: No module named 'sqlglot'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install sqlglot
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install sqlglot
python -c "import sqlglot; print(sqlglot.__version__)"
```

## Related Errors

- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-ibis" >}} — ImportError: ibis
- {{< relref "importerror-datafusion" >}} — ImportError: datafusion
