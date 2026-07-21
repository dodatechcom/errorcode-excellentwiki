---
title: "TimescaleDB Compression Algorithm"
description: "Compression algorithm error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Compression algorithm configuration or execution error.

## Common Causes
- Unsupported algorithm
- Algorithm parameters invalid
- Compression level too high

## How to Fix
```sql
-- Check compression settings
SELECT * FROM timescaledb_information.compression_settings WHERE hypertable_name = 'mytable';

-- Set compression algorithm
ALTER TABLE mytable SET (timescaledb.compress,
  timescaledb.compress_segmentby = 'device_id',
  timescaledb.compress_orderby = 'time DESC');
```

## Examples
```sql
-- Use specific compression settings
ALTER TABLE mytable SET (
  timescaledb.compress,
  timescaledb.compress_segmentby = 'device_id,location_id',
  timescaledb.compress_orderby = 'time DESC'
);
```

