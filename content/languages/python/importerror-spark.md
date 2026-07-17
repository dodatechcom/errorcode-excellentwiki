---
title: "[Solution] Python ImportError: pyspark not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pyspark not found or ModuleNotFoundError: No module named 'pyspark'. Install PySpark properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pyspark not found — ModuleNotFoundError Fix

An `ImportError: pyspark not found` or `ModuleNotFoundError: No module named 'pyspark'` means Python cannot locate the PySpark package.

## What This Error Means

PySpark is the Python API for Apache Spark. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pyspark not installed
from pyspark.sql import SparkSession  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pyspark

# For a specific version
pip install pyspark==3.5.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pyspark
python -c "import pyspark; print(pyspark.__version__)"
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
- {{< relref "importerror-dbt" >}} — ImportError: dbt
