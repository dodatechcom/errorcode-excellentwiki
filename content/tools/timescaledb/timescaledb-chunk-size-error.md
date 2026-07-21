---
title: "TimescaleDB Chunk Size Error"
description: "Chunk size configuration error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Chunk size configuration is incorrect for workload.

## Common Causes
- Chunk interval too small
- Too many chunks created
- Memory pressure from many chunks

## How to Fix
```sql
-- Check current chunk interval
SELECT * FROM timescaledb_information.dimensions WHERE hypertable_name = 'mytable';

-- Adjust chunk interval
SELECT set_chunk_time_interval('mytable', INTERVAL '7 days');
```

## Examples
```sql
-- Check chunk count
SELECT count(*) FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
-- Check average chunk size
SELECT avg(chunk_size) FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
```

