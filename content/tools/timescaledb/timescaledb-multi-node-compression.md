---
title: "TimescaleDB Multi-Node Compression"
description: "Multi-node compression failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Compression in multi-node setup is failing.

## Common Causes
- Data node compression failed
- Access node coordination error
- Insufficient disk space on data node

## How to Fix
```sql
-- Check compression status on all nodes
SELECT * FROM timescaledb_information.compressed_hypertable_stats;

-- Enable compression on distributed hypertable
ALTER TABLE mytable SET (timescaledb.compress, timescaledb.compress_segmentby = 'device_id');
```

## Examples
```sql
-- Check distributed compression
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
-- Compress distributed chunks
SELECT compress_chunk('mytable', show_chunks => 'mytable', newer_than => INTERVAL '7 days');
```

