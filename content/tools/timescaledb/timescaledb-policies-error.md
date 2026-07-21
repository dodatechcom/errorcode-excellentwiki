---
title: "TimescaleDB Policies Error"
description: "Policy execution failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TimescaleDB background policies are failing.

## Common Causes
- Policy configuration error
- Database connection issue
- Insufficient privileges

## How to Fix
```sql
-- List all policies
SELECT * FROM timescaledb_information.policies;

-- Check job status
SELECT * FROM timescaledb_information.job_stats;
```

## Examples
```sql
-- Add compression policy
SELECT add_compression_policy('mytable', INTERVAL '7 days');
-- Add retention policy
SELECT add_retention_policy('mytable', INTERVAL '30 days');
-- Check policy status
SELECT * FROM timescaledb_information.policies WHERE hypertable_name = 'mytable';
```

