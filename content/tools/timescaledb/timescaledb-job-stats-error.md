---
title: "TimescaleDB Job Stats Error"
description: "Job statistics collection error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Cannot collect or query job statistics.

## Common Causes
- Job stats table corrupted
- Statistics not enabled
- Query syntax error

## How to Fix
```sql
-- Check job stats
SELECT * FROM timescaledb_information.job_stats;

-- Check job configuration
SELECT * FROM _timescaledb_config.bgw_job;
```

## Examples
```sql
-- Get detailed job info
SELECT job_id, application_name, schedule_interval, max_runtime, max_retries
FROM _timescaledb_config.bgw_job;
-- Check last run
SELECT job_id, last_run_start, last_run_finish, last_run_status
FROM timescaledb_information.job_stats;
```

