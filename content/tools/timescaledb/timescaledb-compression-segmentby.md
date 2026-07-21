---
title: "TimescaleDB Compression SegmentBy"
description: "SegmentBy compression error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
SegmentBy compression configuration is causing errors.

## Common Causes
- SegmentBy column not indexed
- Too many segments
- SegmentBy column changes frequently

## How to Fix
```sql
-- Check segmentby settings
SELECT * FROM timescaledb_information.compression_settings WHERE hypertable_name = 'mytable';

-- Update segmentby
ALTER TABLE mytable SET (timescaledb.compress_segmentby = 'device_id');
```

## Examples
```sql
-- Check segment count
SELECT count(DISTINCT device_id) FROM mytable;
-- Optimize segmentby for low cardinality
ALTER TABLE mytable SET (timescaledb.compress_segmentby = 'region,device_type');
```

