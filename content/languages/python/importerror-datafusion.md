---
title: "[Solution] Python ImportError: datafusion not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: datafusion not found or ModuleNotFoundError: No module named 'datafusion'. Install datafusion properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "datafusion", "module-not-found", "pip", "query-engine"]
weight: 5
---

# ImportError: datafusion not found — ModuleNotFoundError Fix

An `ImportError: datafusion not found` or `ModuleNotFoundError: No module named 'datafusion'` means Python cannot locate the datafusion package.

## What This Error Means

datafusion is a query engine for Apache Arrow. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: datafusion not installed
import datafusion  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install datafusion
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install datafusion
python -c "import datafusion; print(datafusion.__version__)"
```

## Related Errors

- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
- {{< relref "importerror-sqlglot" >}} — ImportError: sqlglot
- {{< relref "importerror-ibis" >}} — ImportError: ibis
