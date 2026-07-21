---
title: "[Solution] TimescaleDB Copy Error — How to Fix"
description: "Fix TimescaleDB COPY errors by resolving COPY failures on hypertables, fixing data format issues, and handling bulk load constraints"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Copy Error

TimescaleDB COPY errors occur when using the PostgreSQL COPY command to load data into hypertables fails due to format issues, constraint violations, or chunk creation failures.

## Why It Happens

- CSV format does not match the table schema
- Data types in the CSV file are incompatible
- NOT NULL constraint is violated during COPY
- Unique constraint violation occurs on duplicate data
- COPY exceeds memory for large files
- Time column is missing or in wrong format in the data

## Common Error Messages

```
ERROR: missing data for column
```

```
ERROR: invalid input syntax for type timestamp
```

```
ERROR: null value in column violates not-null constraint
```

```
ERROR: duplicate key value violates unique constraint
```

## How to Fix It

### 1. Fix CSV Format Issues

```bash
# Verify CSV format
head -5 data.csv

# Correct CSV with header
\copy sensor_data(time, device_id, value) FROM 'data.csv' CSV HEADER;

# CSV without header
\copy sensor_data(time, device_id, value) FROM 'data.csv' CSV;

# Tab-separated
\copy sensor_data FROM 'data.tsv' DELIMITER E'\t';
```

### 2. Handle NULL Values

```sql
-- Set NOT NULL columns with default values
-- In the CSV, use empty string and convert during COPY
\copy sensor_data(time, device_id, value) FROM 'data.csv' CSV HEADER;

-- Or preprocess the CSV
-- Replace empty values with defaults using sed
sed 's/,,/,0,/g' data.csv > data_clean.csv
\copy sensor_data(time, device_id, value) FROM 'data_clean.csv' CSV HEADER;
```

### 3. Fix Timestamp Format

```sql
-- Ensure timestamp format matches
-- PostgreSQL default: YYYY-MM-DD HH:MM:SS
-- ISO format: 2024-01-15T10:30:00Z

-- Copy with explicit format
COPY sensor_data(time, device_id, value)
FROM STDIN WITH (
  FORMAT csv,
  HEADER true,
  DELIMITER ','
);
```

### 4. Handle Constraint Violations

```sql
-- Use ON CONFLICT for COPY operations
-- First create a staging table
CREATE TEMPORARY TABLE staging_sensor LIKE sensor_data;

-- Copy to staging
\copy staging_sensor FROM 'data.csv' CSV HEADER;

-- Insert with conflict handling
INSERT INTO sensor_data
SELECT * FROM staging_sensor
ON CONFLICT (time, device_id)
DO UPDATE SET value = EXCLUDED.value;
```

## Common Scenarios

- **COPY fails with format error**: Verify CSV delimiters and quote characters match.
- **Timestamp parsing fails**: Ensure timestamps are in YYYY-MM-DD HH:MM:SS format.
- **COPY is slow on large files**: Split the file into smaller batches.

## Prevent It

- Validate CSV format before COPY operations
- Use staging tables for data with potential conflicts
- Monitor memory usage during large COPY operations

## Related Pages

- [TimescaleDB Insert Error](/tools/timescaledb/timescale-insert-error)
- [TimescaleDB Hypertable Error](/tools/timescaledb/timescale-hypertable-error)
- [TimescaleDB Chunk Create Error](/tools/timescaledb/timescale-chunk-create-error)
