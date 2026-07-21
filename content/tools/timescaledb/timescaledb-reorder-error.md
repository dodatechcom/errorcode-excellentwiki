---
title: "TimescaleDB Reorder Error"
description: "Chunk reorder operation failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot reorder chunk indexes.

## Common Causes
- Chunk too large
- Insufficient disk space
- Concurrent operations

## How to Fix
```sql
-- Check chunk sizes
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable' ORDER BY chunk_name;

-- Reorder chunk
CALL reorder_chunk('mytable', 'mytable_time_idx', 100);
```

## Examples
```sql
-- Check reorder status
SELECT * FROM _timescaledb_internal._compressed_hypertable_stats;
-- Manual reorder
CALL reorder_chunk('mytable', 'mytable_time_idx');
```

