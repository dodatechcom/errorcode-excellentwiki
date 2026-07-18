---
title: "[Solution] ScyllaDB Import Error — How to Fix"
description: "Fix ScyllaDB import errors by resolving SSTable loader issues, fixing CSV import failures, and correcting bulk data loading problems"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Import Error

ScyllaDB import errors occur when loading external data into ScyllaDB using SSTable loaders, COPY command, or bulk insert utilities.

## Why It Happens

- CSV data contains formatting errors or invalid characters
- Column types in import file do not match table schema
- SSTable loader encounters incompatible format
- Import file encoding is not UTF-8
- Too many concurrent inserts overwhelm the cluster
- Import data violates primary key constraints

## Common Error Messages

```
ImportError: Failed to parse CSV line
```

```
InvalidRequest: Column type mismatch during import
```

```
SSTableLoaderError: Unable to load SSTable
```

```
WriteTimeout: Import write timeout
```

## How to Fix It

### 1. Use COPY for CSV Import

```cql
-- Import CSV file into table
COPY users (id, name, email, created_at)
FROM '/tmp/users.csv'
WITH HEADER = true
AND DELIMITER = ','
AND QUOTE = '"'
AND NULL = 'NULL'
AND MAXBATCHSIZE = 20
AND ENGINE = 'ChunkedWriter';
```

### 2. Fix CSV Formatting Issues

```bash
# Ensure CSV is properly formatted
head -5 /tmp/users.csv

# Common fixes:
# 1. Add header row matching column names
# 2. Use proper quoting for values containing commas
# 3. Ensure consistent line endings (LF not CRLF)
# 4. Fix UTF-8 encoding issues

# Convert encoding if needed
iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv
```

### 3. Use SSTable Loader for Large Datasets

```bash
# Load SSTables from external source
sstableloader -d 10.0.0.1 /path/to/sstables/

# Load with specific consistency
sstableloader -d 10.0.0.1 -cl LOCAL_QUORUM /path/to/sstables/

# Load into specific keyspace
sstableloader -d 10.0.0.1 -ks mykeyspace -t mytable /path/to/sstables/
```

### 4. Bulk Import with Python

```python
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
import csv

cluster = Cluster(['10.0.0.1'])
session = cluster.connect('mykeyspace')

# Prepare insert statement
insert = session.prepare(
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?)"
)

# Bulk insert in batches
batch_size = 50
batch = BatchStatement()

with open('/tmp/users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        batch.add(insert, [row['id'], row['name'], row['email']])
        if (i + 1) % batch_size == 0:
            session.execute(batch)
            batch = BatchStatement()
            print(f"Imported {i + 1} rows")

# Execute remaining
if len(batch) > 0:
    session.execute(batch)

cluster.shutdown()
```

## Common Scenarios

- **CSV import fails on special characters**: Use proper quoting and escape characters.
- **SSTable loader fails with version mismatch**: Ensure SSTables are from compatible ScyllaDB version.
- **Import is too slow**: Use parallel imports and increase batch size.

## Prevent It

- Validate CSV data before importing
- Use `COPY` with `MAXBATCHSIZE` for large files
- Test imports on a staging environment first

## Related Pages

- [ScyllaDB Backup Error](/tools/scylladb/scylladb-backup-error)
- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB Schema Error](/tools/scylladb/scylladb-schema-error)
