---
title: "TimescaleDB Compression OrderBy"
description: "OrderBy compression configuration error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
OrderBy compression configuration is causing errors.

## Common Causes
- OrderBy column not indexed
- OrderBy column changes
- Compression not enabled

## How to Fix
```sql
-- Check compression settings
SELECT * FROM timescaledb_information.compression_settings WHERE hypertable_name = 'mytable';

-- Set orderby
ALTER TABLE mytable SET (timescaledb.compress, timescaledb.compress_orderby = 'time DESC');
```

## Examples
```sql
-- Check compression settings
SELECT * FROM timescaledb_information.compression_settings;
-- Update orderby
ALTER TABLE mytable SET (timescaledb.compress_orderby = 'device_id, time DESC');
```

