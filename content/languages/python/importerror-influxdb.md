---
title: "[Solution] Python ImportError: influxdb_client not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: influxdb_client not found or ModuleNotFoundError: No module named 'influxdb_client'. Install InfluxDB client properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "influxdb", "module-not-found", "pip", "time-series"]
weight: 5
---

# ImportError: influxdb_client not found — ModuleNotFoundError Fix

An `ImportError: influxdb_client not found` or `ModuleNotFoundError: No module named 'influxdb_client'` means Python cannot locate the influxdb-client package.

## What This Error Means

influxdb-client is the Python client for InfluxDB 2.x. The package is installed as `influxdb-client` but imported as `influxdb_client`.

## Common Causes

```python
# Cause 1: influxdb_client not installed
from influxdb_client import InfluxDBClient  # ModuleNotFoundError

# Cause 2: Installed wrong package name
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install influxdb-client
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install influxdb-client
python -c "from influxdb_client import InfluxDBClient; print('OK')"
```

## Related Errors

- {{< relref "importerror-pymongo" >}} — ImportError: pymongo
- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
