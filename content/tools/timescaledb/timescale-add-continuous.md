---
title: "[Solution] TimescaleDB Add Continuous Aggregate Error — How to Fix"
description: "Fix TimescaleDB add continuous aggregate errors by correcting view definitions, resolving policy conflicts, and fixing materialization issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Add Continuous Aggregate Error

TimescaleDB add continuous aggregate errors occur when adding new continuous aggregates or modifying existing ones. Issues include definition errors, policy conflicts, and refresh failures.

## Why It Happens

- View definition uses functions not supported in continuous aggregates
- Policy conflicts with existing refresh schedules
- Real-time aggregation is not configured correctly
- Underlying hypertable is not properly configured
- GROUP BY columns are missing from SELECT
- Continuous aggregate name conflicts with existing view

## Common Error Messages

```
ERROR: continuous aggregate already exists
```

```
ERROR: function not supported
```

```
ERROR: GROUP BY clause missing required column
```

```
ERROR: invalid continuous aggregate definition
```

## How to Fix It

### 1. Create Correct Continuous Aggregate

```sql
-- Basic continuous aggregate
CREATE MATERIALIZED VIEW daily_summary
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 day', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp,
  COUNT(*) AS count
FROM sensor_data
GROUP BY bucket, sensor_id
WITH NO DATA;

-- With WHERE clause for filtering
CREATE MATERIALIZED VIEW active_sensors_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
WHERE status = 'active'
GROUP BY bucket, sensor_id
WITH NO DATA;
```

### 2. Add Refresh Policy

```sql
-- Add refresh policy
SELECT add_continuous_aggregate_policy('daily_summary',
  start_offset => INTERVAL '3 days',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');

-- Check policy is running
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'refresh_continuous_aggregate';

-- Disable policy temporarily
SELECT remove_continuous_aggregate_policy('daily_summary');
```

### 3. Configure Real-Time Aggregation

```sql
-- Enable real-time aggregation (default is ON)
ALTER MATERIALIZED VIEW daily_summary
SET (timescaledb.materialized_only = false);

-- This allows queries to combine materialized + real-time data
-- Query will show both historical materialized and recent unmaterialized data
SELECT * FROM daily_summary
WHERE bucket > NOW() - INTERVAL '1 day';
```

### 4. Fix Existing Continuous Aggregate

```sql
-- Drop and recreate with correct definition
DROP MATERIALIZED VIEW daily_summary;

-- Recreate with proper settings
CREATE MATERIALIZED VIEW daily_summary
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 day', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY bucket, sensor_id
WITH NO DATA;

-- Rebuild existing data
CALL refresh_continuous_aggregate('daily_summary', NULL, NULL);
```

## Common Scenarios

- **View definition has unsupported function**: Use only supported aggregates (AVG, SUM, COUNT, etc.).
- **Refresh policy not running**: Check job status and ensure TimescaleDB scheduler is active.
- **Real-time data is missing**: Enable real-time aggregation with `materialized_only = false`.

## Prevent It

- Test continuous aggregate definitions with sample data first
- Set up refresh policies immediately after creating the view
- Monitor refresh job status regularly

## Related Pages

- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB Refresh Error](/tools/timescaledb/timescale-refresh-error)
- [TimescaleDB Job Error](/tools/timescaledb/timescale-job-error)
