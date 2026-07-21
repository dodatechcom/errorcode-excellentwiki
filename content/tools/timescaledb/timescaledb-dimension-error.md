---
title: "TimescaleDB Dimension Error"
description: "Hypertable dimension configuration error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Hypertable dimension configuration is incorrect.

## Common Causes
- Dimension column not indexed
- Too many dimensions
- Invalid partitioning

## How to Fix
```sql
-- Check dimensions
SELECT * FROM timescaledb_information.dimensions WHERE hypertable_name = 'mytable';

-- Add dimension
SELECT add_dimension('mytable', 'location_id', number_partitions => 4);
```

## Examples
```sql
-- Check dimension configuration
SELECT * FROM _timescaledb_catalog.dimension;
-- Remove dimension
SELECT remove_dimension('mytable', 'location_id');
```

