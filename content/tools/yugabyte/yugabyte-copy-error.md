---
title: "[Solution] YugabyteDB COPY Error — How to Fix"
description: "Fix YugabyteDB COPY errors by resolving COPY command failures, fixing data format issues, and handling bulk load problems on distributed tables"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB COPY Error

YugabyteDB COPY errors occur when using the PostgreSQL COPY command to load data into tables fails due to format, constraint, or distributed table issues.

## Why It Happens

- CSV format does not match the table schema
- Data types in the file are incompatible with columns
- NOT NULL constraint is violated during COPY
- Unique constraint violation occurs on duplicate data
- COPY on distributed tables has timeout issues
- File encoding is not UTF-8

## Common Error Messages

```
ERROR: missing data for column
```

```
ERROR: invalid input syntax for type
```

```
ERROR: null value violates not-null constraint
```

```
ERROR: duplicate key value violates unique constraint
```

## How to Fix It

### 1. Fix CSV Format

```bash
# Correct CSV with header
\copy my_table FROM 'data.csv' CSV HEADER;

# CSV without header
\copy my_table(col1, col2, col3) FROM 'data.csv' CSV;

# Tab-separated
\copy my_table FROM 'data.tsv' DELIMITER E'\t';
```

### 2. Handle NULL Values

```sql
-- Use staging table for data with NULLs
CREATE TEMPORARY TABLE staging LIKE my_table;

-- Copy to staging
\copy staging FROM 'data.csv' CSV HEADER;

-- Insert with NULL handling
INSERT INTO my_table
SELECT
  id,
  COALESCE(name, 'unknown'),
  COALESCE(value, 0)
FROM staging;
```

### 3. Fix Constraint Violations

```sql
-- Use ON CONFLICT for COPY operations
CREATE TEMPORARY TABLE staging LIKE my_table;
\copy staging FROM 'data.csv' CSV HEADER;

INSERT INTO my_table
SELECT * FROM staging
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name;
```

### 4. Optimize COPY Performance

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

- **COPY fails with format error**: Check CSV delimiters and header.
- **COPY is slow on large files**: Split into smaller chunks.
- **COPY violates constraints**: Use staging table with ON CONFLICT.

## Prevent It

- Validate CSV format before COPY
- Use staging tables for data with potential conflicts
- Test COPY with small datasets first

## Related Pages

- [YugabyteDB Import Error](/tools/yugabyte/yugabyte-import-error)
- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
- [YugabyteDB DML Error](/tools/yugabyte/yugabyte-dml-error)
