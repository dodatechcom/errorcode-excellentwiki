---
title: "TimescaleDB Hypertable Chunk Fallback"
description: "Chunk creation fallback to default"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Chunk creation falling back to default behavior.

## Common Causes
- Custom chunk creation failed
- Insufficient resources
- Chunk creation timeout

## How to Fix
```sql
-- Check chunk creation settings
SELECT * FROM timescaledb_information.dimensions WHERE hypertable_name = 'mytable';

-- Manually create chunk
SELECT create_chunk('mytable', '2024-01-01', '2024-01-02');
```

## Examples
```sql
-- Check existing chunks
SELECT chunk_name, range_start, range_end FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
-- Create chunks proactively
SELECT create_chunk('mytable', CURRENT_DATE, CURRENT_DATE + INTERVAL '7 days');
```

