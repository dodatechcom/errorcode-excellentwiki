---
title: "TimescaleDB Continuous Aggregate Compression"
description: "Continuous aggregate compression error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Continuous aggregate compression is failing.

## Common Causes
- Compression not enabled on CAGG
- SegmentBy configuration error
- Data not in expected format

## How to Fix
```sql
-- Check CAGG compression settings
SELECT * FROM timescaledb_information.compression_settings WHERE hypertable_name = 'my_cagg';

-- Enable compression on CAGG
ALTER MATERIALIZED VIEW my_cagg SET (timescaledb.compress, timescaledb.compress_segmentby = 'device_id');
```

## Examples
```sql
-- Check CAGG compression
SELECT * FROM timescaledb_information.compression_settings WHERE hypertable_name = 'my_cagg';
-- Compress CAGG chunks
SELECT compress_chunk('my_cagg', show_chunks => 'my_cagg', newer_than => INTERVAL '7 days');
```

