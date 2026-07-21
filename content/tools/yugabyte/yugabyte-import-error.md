---
title: "[Solution] YugabyteDB Import Error — How to Fix"
description: "Fix YugabyteDB import errors by resolving data import failures, fixing CSV/SQL import issues, and handling bulk load problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Import Error

YugabyteDB import errors occur when importing data from CSV, SQL dumps, or other formats fails due to format, constraint, or connectivity issues.

## Why It Happens

- CSV format does not match the table schema
- Data types in the file are incompatible with table columns
- Import violates unique or NOT NULL constraints
- Import exceeds timeout for large files
- Connection drops during bulk import
- Import file encoding is not UTF-8

## Common Error Messages

```
ERROR: missing data for column
```

```
ERROR: invalid input syntax for type
```

```
ERROR: duplicate key violates unique constraint
```

```
ERROR: connection lost during import
```

## How to Fix It

### 1. Fix CSV Import

```bash
# Import CSV with correct format
\copy my_table FROM 'data.csv' CSV HEADER;

# Import with specific columns
\copy my_table(id, name, value) FROM 'data.csv' CSV HEADER;
```

### 2. Fix SQL Dump Import

```bash
# Import SQL dump
psql -h yugabyte -p 5433 -U yugabyte -d mydb -f dump.sql

# Import with specific options
psql -h yugabyte -p 5433 -U yugabyte -d mydb \
  --set ON_ERROR_STOP=off -f dump.sql
```

### 3. Fix Encoding Issues

```bash
# Convert file to UTF-8
iconv -f GBK -t UTF-8 data.csv > data_utf8.csv

# Check file encoding
file data.csv
```

### 4. Optimize Bulk Import

```bash
# Split large files for faster import
split -l 100000 data.csv chunk_

# Import each chunk
for f in chunk_*; do
  psql -h yugabyte -p 5433 -U yugabyte -d mydb \
    -c "\copy my_table FROM '$f' CSV HEADER"
done
```

## Common Scenarios

- **Import fails with format error**: Check CSV delimiters and header row.
- **Import is slow**: Split large files and import in parallel.
- **Connection drops during import**: Use --set ON_ERROR_STOP=off to continue.

## Prevent It

- Validate data format before import
- Use staging tables for large imports
- Test import with small datasets first

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
- [YugabyteDB DML Error](/tools/yugabyte/yugabyte-dml-error)
