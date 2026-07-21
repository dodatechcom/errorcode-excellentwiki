---
title: "TimescaleDB Chunk Error"
description: "Chunk creation or access failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot create or access chunks in hypertable.

## Common Causes
- Chunk size too small
- Disk full
- Chunk creation interval mismatch

## How to Fix
```sql
-- Check chunk configuration
SELECT * FROM timescaledb_information.dimensions WHERE hypertable_name = 'mytable';

-- Adjust chunk interval
SELECT set_chunk_time_interval('mytable', INTERVAL '1 day');
```

## Examples
```sql
-- List chunks
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
-- Manually create chunk
SELECT create_chunk('mytable', '2024-01-01', '2024-01-02');
```

