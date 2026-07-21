---
title: "[Solution] TimescaleDB Insert Error — How to Fix"
description: "Fix TimescaleDB insert errors by resolving INSERT failures on hypertables, fixing chunk creation issues, and handling constraint violations"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Insert Error

TimescaleDB insert errors occur when INSERT operations on hypertables fail due to chunk creation issues, constraint violations, or misconfigured partitioning.

## Why It Happens

- Time column value is NULL or missing
- INSERT violates a unique constraint across chunks
- Chunk creation fails due to disk space or permissions
- Data type mismatch between insert values and column types
- Insert timestamp is too old and falls outside valid range
- Hypertable is not yet created for the target table

## Common Error Messages

```
ERROR: null value in column "time" violates not-null constraint
```

```
ERROR: duplicate key value violates unique constraint
```

```
ERROR: could not create chunk
```

```
ERROR: time value is out of range
```

## How to Fix It

### 1. Ensure Time Column is Populated

```sql
-- Insert with explicit time value
INSERT INTO sensor_data (time, device_id, value)
VALUES (NOW(), 1, 25.5);

-- Use DEFAULT if time column has DEFAULT NOW()
ALTER TABLE sensor_data
  ALTER COLUMN time SET DEFAULT NOW();

INSERT INTO sensor_data (device_id, value)
VALUES (1, 25.5);
```

### 2. Fix Constraint Violations

```sql
-- Check unique constraints
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'sensor_data'::regclass;

-- Use ON CONFLICT to handle duplicates
INSERT INTO sensor_data (time, device_id, value)
VALUES (NOW(), 1, 25.5)
ON CONFLICT (time, device_id)
DO UPDATE SET value = EXCLUDED.value;
```

### 3. Fix Data Type Issues

```sql
-- Check column types
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'sensor_data';

-- Insert with correct types
INSERT INTO sensor_data (time, device_id, value)
VALUES ('2024-01-15 10:30:00+00'::TIMESTAMPTZ, 1, 25.5);
```

### 4. Use COPY for Bulk Inserts

```sql
-- Use COPY for better performance
\copy sensor_data FROM 'data.csv' CSV HEADER;

-- Or with specific columns
\copy sensor_data(time, device_id, value) FROM 'data.csv' CSV HEADER;
```

## Common Scenarios

- **Insert fails with NULL time**: Ensure the time column is always provided.
- **Duplicate key error**: Use ON CONFLICT clause or check for existing rows.
- **Bulk insert is slow**: Use COPY instead of individual INSERT statements.

## Prevent It

- Always include the time column in INSERT statements
- Use ON CONFLICT for idempotent inserts
- Use COPY for bulk data loading operations

## Related Pages

- [TimescaleDB Hypertable Error](/tools/timescaledb/timescale-hypertable-error)
- [TimescaleDB Chunk Create Error](/tools/timescaledb/timescale-chunk-create-error)
- [TimescaleDB Distributed Insert Error](/tools/timescaledb/timescale-distributed-insert-error)
