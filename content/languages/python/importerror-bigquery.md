---
title: "[Solution] Python ImportError: google.cloud.bigquery not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: google.cloud.bigquery not found. Install google-cloud-bigquery properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: google.cloud.bigquery not found — ModuleNotFoundError Fix

An `ImportError: google.cloud.bigquery not found` or `ModuleNotFoundError: No module named 'google.cloud.bigquery'` means Python cannot locate the google-cloud-bigquery package.

## What This Error Means

google-cloud-bigquery is the Google BigQuery client library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: google-cloud-bigquery not installed
from google.cloud import bigquery  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install google-cloud-bigquery

# With all optional dependencies
pip install google-cloud-bigquery[bqstorage,pandas,pyarrow]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install google-cloud-bigquery
python -c "from google.cloud import bigquery; print('OK')"
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
- {{< relref "importerror-pyspark" >}} — ImportError: pyspark
