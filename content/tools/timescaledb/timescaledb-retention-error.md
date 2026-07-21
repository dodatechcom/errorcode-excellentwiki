---
title: "TimescaleDB Retention Error"
description: "Data retention policy failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Retention policy not removing old data.

## Common Causes
- Policy not scheduled
- Time column not indexed
- Policy interval too large

## How to Fix
```sql
-- Check retention policies
SELECT * FROM timescaledb_information.policies WHERE proc_name = 'retention';

-- Add retention policy
SELECT add_retention_policy('mytable', INTERVAL '90 days');
```

## Examples
```sql
-- Remove old data manually
SELECT drop_chunks('mytable', older_than => INTERVAL '90 days');
-- Check retained data
SELECT min(time), max(time) FROM mytable;
```

