---
title: "TimescaleDB Continuous Aggregate Policies"
description: "Continuous aggregate policy configuration error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Continuous aggregate refresh or compression policy is misconfigured.

## Common Causes
- Policy interval too frequent
- Overlapping refresh windows
- Missing compression settings

## How to Fix
```sql
-- Check CAGG policies
SELECT * FROM timescaledb_information.policies WHERE hypertable_name = 'my_cagg';

-- Add refresh policy
SELECT add_continuous_aggregate_policy('my_cagg',
  start_offset => INTERVAL '1 hour',
  end_offset => INTERVAL '5 minutes',
  schedule_interval => INTERVAL '1 hour');
```

## Examples
```sql
-- Check CAGG settings
SELECT * FROM timescaledb_information.continuous_aggregates WHERE view_name = 'my_cagg';
-- Remove policy
SELECT remove_continuous_aggregate_policy('my_cagg');
```

