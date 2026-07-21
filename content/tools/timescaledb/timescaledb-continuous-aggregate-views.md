---
title: "TimescaleDB Continuous Aggregate Views"
description: "Continuous aggregate view error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Continuous aggregate view is returning incorrect results.

## Common Causes
- View definition error
- Data not refreshed
- Time bucket mismatch

## How to Fix
```sql
-- Check view definition
SELECT * FROM timescaledb_information.continuous_aggregates WHERE view_name = 'my_cagg';

-- Refresh view
CALL refresh_continuous_aggregate('my_cagg', '2024-01-01', '2024-01-02');
```

## Examples
```sql
-- Create proper continuous aggregate
CREATE MATERIALIZED VIEW my_cagg WITH (timescaledb.continuous) AS
  SELECT time_bucket('1 hour', time) AS bucket,
         device_id,
         AVG(value) AS avg_value,
         COUNT(*) AS sample_count
  FROM mytable
  GROUP BY bucket, device_id;
-- Query the view
SELECT * FROM my_cagg WHERE bucket > NOW() - INTERVAL '1 day';
```

