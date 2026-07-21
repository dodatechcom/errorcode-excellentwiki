---
title: "[Solution] TiDB Lightning Error — How to Fix"
description: "Fix TiDB Lightning import errors by resolving CSV parsing failures, fixing checkpoint conflicts, and handling engine write timeouts"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Lightning Error

TiDB Lightning errors occur during the data import process when parsing source files, writing to engines, or uploading data to TiKV fails.

## Why It Happens

- CSV file format does not match the table schema
- Checkpoint file is corrupted or inconsistent with current import
- TiKV import engine write exceeds timeout
- Source data file is not UTF-8 encoded
- Duplicate primary keys in the source data
- Region size is too small for the data being imported

## Common Error Messages

```
ERROR: CSV syntax error near line N
```

```
ERROR: checkpoint does not match
```

```
ERROR: engine write timeout
```

```
ERROR: table already exists in checkpoint
```

## How to Fix It

### 1. Fix CSV Parsing Errors

```toml
# lightning.toml - correct CSV settings
[mydumper]
# Specify CSV separator
csv-separator = ","
# Include header row
csv-header = true
# Quote character
csv-quote = '"'
# Escape character
csv-backslash-escape = true
```

```bash
# Validate CSV before importing
head -5 /data/import/orders.csv

# Check for bad rows
awk -F',' '{if(NF != expected_fields) print NR": "$0}' orders.csv
```

### 2. Fix Checkpoint Issues

```toml
# lightning.toml
[checkpoint]
# Enable checkpoints
enable = true
# Use file-based checkpoint
driver = "file"
# Schema name for checkpoint
schema = "tidb_lightning_checkpoint"
```

```sql
-- Clear stuck checkpoint
DROP DATABASE IF EXISTS tidb_lightning_checkpoint;

-- Or remove checkpoint file
rm -f /tmp/tidb_lightning_checkpoint.pb
```

### 3. Resolve Engine Write Timeout

```toml
# lightning.toml
[import]
# Increase timeout for engine writes
engine-write-timeout = "600s"
# Number of concurrent engines
num-concurrent-engines = 4
# KV write batch size
kv-write-batch-size = 16777216
```

### 4. Fix Encoding Issues

```bash
# Convert files to UTF-8
iconv -f GBK -t UTF-8 source.csv > source_utf8.csv

# Validate encoding
file source.csv
# Expected: CSV text, UTF-8 Unicode text
```

## Common Scenarios

- **Import fails at line N**: Check the CSV format at that line for missing or extra delimiters.
- **Lightning restart fails**: Clear the checkpoint and re-import from the beginning.
- **TiKV import region error**: Increase region size or decrease concurrency.

## Prevent It

- Validate source data format before starting import
- Enable and regularly back up checkpoints
- Use `tidb-lightning-ctl --check-table-versions` to verify imports

## Related Pages

- [TiDB Import Error](/tools/tidb/tidb-import-error)
- [TiDB BR Error](/tools/tidb/tidb-br-error)
- [TiDB Restore Error](/tools/tidb/tidb-restore-error)
