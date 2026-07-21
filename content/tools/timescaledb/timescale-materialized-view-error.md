---
title: "[Solution] TimescaleDB Materialized View Error — How to Fix"
description: "Fix TimescaleDB materialized view errors by resolving refresh failures, fixing dependent view issues, and handling concurrent refresh conflicts"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Materialized View Error

TimescaleDB materialized view errors occur when creating, refreshing, or querying materialized views that depend on hypertables or use TimescaleDB-specific functions.

## Why It Happens

- Materialized view references a hypertable without proper time conditions
- REFRESH MATERIALIZED VIEW CONFLICTS with concurrent reads
- View definition uses functions not available in the current schema
- Materialized view depends on a dropped table
- Concurrent refresh requires a unique index
- Memory is insufficient for the refresh query

## Common Error Messages

```
ERROR: cannot refresh materialized view concurrently
```

```
ERROR: relation does not exist
```

```
ERROR: out of memory during materialized view refresh
```

```
ERROR: unique index required for concurrent refresh
```

## How to Fix It

### 1. Create Materialized View Correctly

```sql
-- Standard materialized view
CREATE MATERIALIZED VIEW sensor_summary AS
SELECT
  device_id,
  DATE_TRUNC('day', time) AS day,
  AVG(temperature) AS avg_temp,
  MAX(humidity) AS max_humidity
FROM sensor_data
WHERE time > NOW() - INTERVAL '30 days'
GROUP BY device_id, DATE_TRUNC('day', time);

-- Add unique index for concurrent refresh
CREATE UNIQUE INDEX idx_sensor_summary
ON sensor_summary (device_id, day);
```

### 2. Refresh Materialized View

```sql
-- Non-concurrent refresh (blocks reads)
REFRESH MATERIALIZED VIEW sensor_summary;

-- Concurrent refresh (allows reads during refresh)
REFRESH MATERIALIZED VIEW CONCURRENTLY sensor_summary;

-- Refresh with specific data
REFRESH MATERIALIZED VIEW sensor_summary
WHERE day >= '2024-01-01';
```

### 3. Fix Concurrent Refresh Issues

```sql
-- Ensure unique index exists
SELECT indexdef
FROM pg_indexes
WHERE tablename = 'sensor_summary';

-- Add unique index if missing
CREATE UNIQUE INDEX CONCURRENTLY idx_sensor_summary_unique
ON sensor_summary (device_id, day);
```

### 4. Use Continuous Aggregate Instead

```sql
-- For hypertable-backed views, use continuous aggregate
CREATE MATERIALIZED VIEW sensor_continuous_summary
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  device_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY bucket, device_id;

-- Add refresh policy
SELECT add_continuous_aggregate_policy('sensor_continuous_summary',
  start_offset => INTERVAL '3 hours',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour'
);
```

## Common Scenarios

- **Concurrent refresh fails**: Ensure a unique index exists on the materialized view.
- **Refresh is slow**: Consider using continuous aggregates instead of standard materialized views.
- **View shows stale data**: Schedule regular refreshes with pg_cron or continuous aggregate policies.

## Prevent It

- Create unique indexes on materialized views before using CONCURRENTLY
- Use continuous aggregates for time-series data instead of standard materialized views
- Schedule refresh during low-traffic periods

## Related Pages

- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB View Error](/tools/timescaledb/timescale-view-error)
- [TimescaleDB Refresh Error](/tools/timescaledb/timescale-refresh-error)
