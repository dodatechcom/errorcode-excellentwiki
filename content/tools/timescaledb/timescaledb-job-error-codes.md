---
title: "TimescaleDB Job Error Codes"
description: "Job execution error codes"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Background job failing with specific error codes.

## Common Causes
- Database connection lost
- Insufficient privileges
- Resource exhaustion

## How to Fix
```sql
-- Check job errors
SELECT * FROM timescaledb_information.job_stats WHERE last_run_status = 'FAILED';

-- Manually run job
SELECT run_job(<job_id>);
```

## Examples
```sql
-- Get error details
SELECT job_id, last_run_status, last_run_error
FROM timescaledb_information.job_stats
WHERE last_run_status = 'FAILED';
-- Retry failed job
SELECT alter_job(<job_id>, scheduled => true);
```

