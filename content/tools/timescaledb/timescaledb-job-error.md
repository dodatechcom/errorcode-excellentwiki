---
title: "TimescaleDB Job Error"
description: "Background job execution failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TimescaleDB background job failed to execute.

## Common Causes
- Job configuration error
- Database connection issue
- Insufficient privileges

## How to Fix
```sql
-- Check job status
SELECT * FROM timescaledb_information.job_stats;

-- Manually run job
SELECT run_job(<job_id>);
```

## Examples
```sql
-- List all jobs
SELECT * FROM _timescaledb_config.bgw_job;
-- Check job errors
SELECT * FROM timescaledb_information.job_stats WHERE last_run_status = 'FAILED';
```

