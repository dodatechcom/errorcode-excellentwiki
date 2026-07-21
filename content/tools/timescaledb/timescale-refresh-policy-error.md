---
title: "[Solution] TimescaleDB Refresh Policy Error — How to Fix"
description: "Fix TimescaleDB refresh policy errors by resolving continuous aggregate refresh failures, fixing policy scheduling, and handling refresh window issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Refresh Policy Error

TimescaleDB refresh policy errors occur when continuous aggregate refresh policies fail to execute, produce incorrect results, or are misconfigured with overlapping time windows.

## Why It Happens

- Refresh window overlaps with the previous refresh
- Schedule interval is too short for the data volume
- Source data does not exist for the refresh window
- Background worker is not running
- Refresh policy configuration has invalid offset values
- Materialized view query fails during refresh

## Common Error Messages

```
ERROR: refresh policy overlap detected
```

```
ERROR: continuous aggregate refresh failed
```

```
ERROR: invalid refresh policy parameters
```

```
WARNING: refresh job skipped due to overlap
```

## How to Fix It

### 1. Check Refresh Policy Status

```sql
-- View refresh policies
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'continuous_agg_refresh';

-- Check job run history
SELECT * FROM timescaledb_information.job_stats
WHERE job_id IN (
  SELECT job_id FROM _timescaledb_config.bgw_job
  WHERE proc_name = 'continuous_agg_refresh'
);
```

### 2. Configure Refresh Policy Correctly

```sql
-- Add refresh policy with correct offsets
SELECT add_continuous_aggregate_policy('hourly_avg',
  start_offset => INTERVAL '3 hours',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour'
);

-- Remove existing policy first if needed
SELECT remove_continuous_aggregate_policy('hourly_avg');
```

### 3. Manually Refresh to Fix Gaps

```sql
-- Manually refresh a specific time range
CALL refresh_continuous_aggregate('hourly_avg',
  '2024-01-01'::TIMESTAMPTZ,
  '2024-01-02'::TIMESTAMPTZ
);

-- Refresh from a specific time to now
CALL refresh_continuous_aggregate('hourly_avg',
  '2024-01-15'::TIMESTAMPTZ,
  NULL
);
```

### 4. Fix Background Worker

```sql
-- Check worker status
SELECT * FROM pg_stat_activity
WHERE application_name LIKE '%continuous_agg%';

-- Restart workers
SELECT _timescaledb_internal.stop_background_workers();
SELECT _timescaledb_internal.start_background_workers();
```

## Common Scenarios

- **Refresh policy not running**: Ensure the background worker is active.
- **Gaps in materialized data**: Run manual refresh for the missing time range.
- **Policy overlaps with itself**: Increase the schedule interval relative to the refresh window.

## Prevent It

- Set start_offset larger than schedule_interval to avoid overlaps
- Monitor refresh job status regularly
- Test refresh policies with small data volumes first

## Related Pages

- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB Policy Error](/tools/timescaledb/timescale-policy-error)
- [TimescaleDB Job Error](/tools/timescaledb/timescale-job-error)
