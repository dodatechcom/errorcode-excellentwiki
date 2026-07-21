---
title: "TimescaleDB Continuous Aggregate Error"
description: "Continuous aggregate refresh failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Continuous aggregate cannot be refreshed or created.

## Common Causes
- Materialized view definition error
- Refresh policy misconfigured
- Data range not covered

## How to Fix
```sql
-- Check continuous aggregate
SELECT * FROM timescaledb_information.continuous_aggregates;

-- Refresh manually
CALL refresh_continuous_aggregate('my_cagg', NULL, NULL);
```

## Examples
```sql
-- Create continuous aggregate
CREATE MATERIALIZED VIEW my_cagg WITH (timescaledb.continuous) AS
  SELECT time_bucket('1 hour', time) AS bucket,
         device_id,
         AVG(value) AS avg_value
  FROM mytable
  GROUP BY bucket, device_id;

-- Add refresh policy
SELECT add_continuous_aggregate_policy('my_cagg',
  start_offset => INTERVAL '1 hour',
  end_offset => INTERVAL '5 minutes',
  schedule_interval => INTERVAL '1 hour');
```

