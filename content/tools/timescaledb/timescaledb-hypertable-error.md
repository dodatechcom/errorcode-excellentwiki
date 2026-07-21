---
title: "TimescaleDB Hypertable Error"
description: "Hypertable creation or operation failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot create or operate on a TimescaleDB hypertable.

## Common Causes
- Table already a hypertable
- Missing primary key
- Invalid partitioning column

## How to Fix
```sql
-- Check if table is already a hypertable
SELECT * FROM timescaledb_information.hypertables WHERE hypertable_name = 'mytable';

-- Create hypertable
SELECT create_hypertable('mytable', 'time');
```

## Examples
```sql
-- Create hypertable with partitioning
SELECT create_hypertable('mytable', 'time', chunk_time_interval => INTERVAL '1 day');
-- Add space partitioning
SELECT add_dimension('mytable', 'device_id', number_partitions => 4);
```

