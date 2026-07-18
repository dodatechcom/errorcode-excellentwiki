---
title: "[Solution] TimescaleDB Continuous Aggregate Error — How to Fix"
description: "Fix TimescaleDB continuous aggregate errors by resolving materialization failures, fixing refresh issues, and handling view definition problems"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Continuous Aggregate Error

TimescaleDB continuous aggregate errors occur when creating, refreshing, or querying continuous aggregates, which are incrementally maintained materialized views.

## Why It Happens

- View definition uses unsupported functions
- Refresh policy interval is too aggressive
- Underlying data has been dropped before refresh
- Group by column is not in the view definition
- Continuous aggregate already exists when creating
- WITH NO DATA option is missing for initial creation

## Common Error Messages

```
ERROR: continuous aggregate already exists
```

```
ERROR: continuous aggregate refresh failed
```

```
ERROR: function not supported in continuous aggregate
```

```
ERROR: cannot refresh continuous aggregate with dropped chunks
```

## How to Fix It

### 1. Create Continuous Aggregate

```sql
-- Create a continuous aggregate
CREATE MATERIALIZED VIEW sensor_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp,
  MAX(temperature) AS max_temp,
  MIN(temperature) AS min_temp,
  COUNT(*) AS sample_count
FROM sensor_data
GROUP BY bucket, sensor_id
WITH NO DATA;

-- Refresh the view
CALL refresh_continuous_aggregate('sensor_hourly', NULL, NULL);
```

### 2. Fix Refresh Issues

```sql
-- Add a refresh policy
SELECT add_continuous_aggregate_policy('sensor_hourly',
  start_offset => INTERVAL '3 hours',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');

-- Manually refresh a time range
CALL refresh_continuous_aggregate('sensor_hourly',
  '2024-01-01'::timestamptz,
  '2024-01-02'::timestamptz);

-- Check refresh status
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'refresh_continuous_aggregate';
```

### 3. Fix View Definition

```sql
-- Check if a function is supported
SELECT * FROM timescaledb_information.continuous_aggregates
WHERE view_name = 'sensor_hourly';

-- Drop and recreate with correct definition
DROP MATERIALIZED VIEW sensor_hourly;

CREATE MATERIALIZED VIEW sensor_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY bucket, sensor_id
WITH NO DATA;
```

### 4. Handle Dropped Chunks

```sql
-- If chunks are dropped, refresh may fail
-- Set a policy that respects chunk retention
SELECT add_continuous_aggregate_policy('sensor_hourly',
  start_offset => INTERVAL '7 days',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');

-- Drop raw data after aggregate is built
SELECT drop_chunks('sensor_data', older_than => INTERVAL '30 days');
```

## Common Scenarios

- **Refresh fails with dropped chunks**: Ensure aggregate covers a shorter window than raw data retention.
- **Aggregate is stale**: Check that the refresh policy is running and intervals are correct.
- **Unsupported function in view**: Use only supported aggregate functions (AVG, SUM, COUNT, etc.).

## Prevent It

- Create continuous aggregates before dropping raw data
- Set appropriate refresh policies with sufficient offset
- Monitor refresh job status in `timescaledb_information.jobs`

## Related Pages

- [TimescaleDB Refresh Error](/tools/timescaledb/timescale-refresh-error)
- [TimescaleDB View Error](/tools/timescaledb/timescale-view-error)
- [TimescaleDB Job Error](/tools/timescaledb/timescale-job-error)
