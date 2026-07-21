---
title: "TiDB DDL Pause Error Code"
description: "DDL pause error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL pause returning specific error code.

## Common Causes
- DDL job not running
- Pause not supported for job type
- Concurrent DDL conflict

## How to Fix
```sql
-- Check DDL jobs
SHOW DDL JOBS;

-- Pause DDL
ADMIN PAUSE DDL JOBS <job_id>;
```

## Examples
```sql
-- Check DDL status
SHOW DDL JOB QUERIES <job_id>;
-- Resume DDL
ADMIN RESUME DDL JOBS <job_id>;
```

