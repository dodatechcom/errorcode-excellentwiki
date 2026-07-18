---
title: "[Solution] TimescaleDB Refresh Error — How to Fix"
description: "Fix TimescaleDB refresh errors by resolving continuous aggregate refresh failures, fixing materialized view refresh issues, and correcting policy intervals"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Refresh Error

TimescaleDB refresh errors occur when refreshing continuous aggregates, materialized views, or refresh policies fails. Regular refreshes keep aggregated data up-to-date.

## Why It Happens

- Refresh job is not scheduled or has been disabled
- Underlying data changes faster than refresh interval
- Refresh overlaps with other maintenance operations
- Continuous aggregate has been dropped but policy still exists
- Disk space is insufficient during refresh
- Refresh window is too large for available resources

## Common Error Messages

```
ERROR: refresh_continuous_aggregate failed
```

```
ERROR: continuous aggregate not found
```

```
ERROR: refresh policy not found
```

```
ERROR: concurrent refresh operation in progress
```

## How to Fix It

### 1. Manual Refresh

```sql
-- Refresh entire continuous aggregate
CALL refresh_continuous_aggregate('daily_summary', NULL, NULL);

-- Refresh specific time range
CALL refresh_continuous_aggregate('daily_summary',
  '2024-01-01'::timestamptz,
  '2024-01-02'::timestamptz);

-- Refresh materialized view (PostgreSQL built-in)
REFRESH MATERIALIZED VIEW CONCURRENTLY my_view;
```

### 2. Fix Refresh Policy

```sql
-- Check existing policies
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'refresh_continuous_aggregate';

-- Remove broken policy
SELECT remove_continuous_aggregate_policy('daily_summary');

-- Add new policy with correct intervals
SELECT add_continuous_aggregate_policy('daily_summary',
  start_offset => INTERVAL '7 days',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');

-- Check policy next run time
SELECT * FROM timescaledb_information.job_stats
WHERE hypertable_name = 'daily_summary';
```

### 3. Monitor Refresh Status

```sql
-- Check running jobs
SELECT * FROM timescaledb_information.jobs
WHERE proc_name LIKE 'refresh%';

-- Check job statistics
SELECT * FROM timescaledb_information.job_stats;

-- Check for failed refreshes
SELECT * FROM _timescaledb_internal.job_errors
ORDER BY start_time DESC LIMIT 10;
```

### 4. Optimize Refresh Performance

```sql
-- Set smaller refresh windows for large datasets
CALL refresh_continuous_aggregate('daily_summary',
  NOW() - INTERVAL '7 days',
  NOW() - INTERVAL '1 hour');

-- Increase schedule frequency during catch-up
SELECT alter_job(<job_id>, schedule_interval => '10 minutes');

-- Reset to normal after catch-up
SELECT alter_job(<job_id>, schedule_interval => '1 hour');
```

## Common Scenarios

- **Refresh falls behind ingestion**: Decrease `schedule_interval` or increase `end_offset`.
- **Refresh fails with disk full**: Ensure sufficient space for temporary files.
- **Policy not running**: Check that the job scheduler is active.

## Prevent It

- Monitor refresh lag with `_timescaledb_internal.job_stats`
- Set appropriate `start_offset` to avoid refreshing too much history
- Test refresh policies with production-like data volumes

## Related Pages

- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB Job Error](/tools/timescaledb/timescale-job-error)
- [TimescaleDB Policy Error](/tools/timescaledb/timescale-policy-error)
