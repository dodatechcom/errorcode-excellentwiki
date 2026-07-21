---
title: "TiDB DDL Resume Error Code"
description: "DDL resume error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL resume returning specific error code.

## Common Causes
- DDL not paused
- Resume not supported for job type
- Job already completed

## How to Fix
```sql
-- Check DDL status
SHOW DDL JOBS;

-- Resume DDL
ADMIN RESUME DDL JOBS <job_id>;
```

## Examples
```sql
-- Check paused DDL
SHOW DDL JOBS WHERE state = 'paused';
-- Resume specific DDL
ADMIN RESUME DDL JOBS 100;
```

