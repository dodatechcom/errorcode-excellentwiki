---
title: "TimescaleDB Compression Error"
description: "Chunk compression failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TimescaleDB chunk compression is failing.

## Common Causes
- Insufficient disk space
- Compression algorithm error
- Chunk in use

## How to Fix
```sql
-- Check compression status
SELECT * FROM timescaledb_information.compressed_hypertable_stats;

-- Enable compression
ALTER TABLE mytable SET (timescaledb.compress, timescaledb.compress_segmentby = 'device_id');
```

## Examples
```sql
-- Compress chunks
SELECT compress_chunk('mytable', show_chunks => 'mytable', newer_than => INTERVAL '7 days');
-- Check compression ratio
SELECT * FROM timescaledb_information.compressed_hypertable_stats WHERE hypertable_name = 'mytable';
```

