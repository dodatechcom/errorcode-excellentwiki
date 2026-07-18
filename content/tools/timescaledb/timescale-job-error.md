---
title: "[Solution] TimescaleDB Job Error — How to Fix"
description: "Fix TimescaleDB job errors by resolving scheduler failures, fixing job configuration, and recovering from stuck background tasks"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Job Error

TimescaleDB job errors occur when background tasks (compression, refresh, retention, reorder) fail or become stuck. Jobs are managed by the TimescaleDB scheduler.

## Why It Happens

- Job scheduler is not running
- Job failed and is in retry state
- Job execution exceeds timeout limits
- Job configuration has invalid parameters
- Concurrent job execution conflicts
- Job depends on a dropped hypertable

## Common Error Messages

```
ERROR: job execution failed
```

```
ERROR: scheduler not running
```

```
ERROR: job not found
```

```
ERROR: job timeout exceeded
```

## How to Fix It

### 1. Check Job Status

```sql
-- List all jobs
SELECT * FROM timescaledb_information.jobs;

-- Check job statistics
SELECT * FROM timescaledb_information.job_stats;

-- Check for failed jobs
SELECT * FROM _timescaledb_internal.job_errors
ORDER BY start_time DESC LIMIT 10;
```

### 2. Fix Stuck Jobs

```sql
-- Manually run a stuck job
CALL run_job(<job_id>);

-- Delete a stuck job
SELECT delete_job(<job_id>);

-- Alter job schedule
SELECT alter_job(<job_id>, schedule_interval => '10 minutes');

-- Disable a job temporarily
SELECT alter_job(<job_id>, schedule_interval => NULL);
```

### 3. Configure Job Parameters

```sql
-- Add compression policy with custom settings
SELECT add_compression_policy('sensor_data',
  compress_after => INTERVAL '7 days',
  if_not_exists => TRUE);

-- Add retention policy
SELECT add_retention_policy('sensor_data',
  drop_after => INTERVAL '30 days');

-- Add refresh policy
SELECT add_continuous_aggregate_policy('daily_summary',
  start_offset => INTERVAL '3 days',
  end_offset => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');
```

### 4. Monitor Job Execution

```sql
-- Check running jobs
SELECT * FROM timescaledb_information.jobs
WHERE next_start <= NOW();

-- Check job history
SELECT * FROM _timescaledb_internal.job_stat_history
ORDER BY start_time DESC LIMIT 20;

-- Check for long-running jobs
SELECT * FROM pg_stat_activity
WHERE query LIKE '%timescaledb%';
```

## Common Scenarios

- **Job keeps failing**: Check job parameters and underlying data consistency.
- **Job not running on schedule**: Verify scheduler is enabled and job is active.
- **Multiple jobs conflict**: Stagger job schedules to avoid overlap.

## Prevent It

- Monitor job status with `timescaledb_information.job_stats`
- Set appropriate timeouts for long-running jobs
- Regularly check for failed jobs in `_timescaledb_internal.job_errors`

## Related Pages

- [TimescaleDB Policy Error](/tools/timescaledb/timescale-policy-error)
- [TimescaleDB Refresh Error](/tools/timescaledb/timescale-refresh-error)
- [TimescaleDB Compression Error](/tools/timescaledb/timescale-compression-error)
