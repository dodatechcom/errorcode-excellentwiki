---
title: "TiDB DDL Cancel Error Code"
description: "DDL cancel error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL cancel returning specific error code.

## Common Causes
- DDL job completed
- Cancel not supported
- Job already cancelled

## How to Fix
```sql
-- Check DDL jobs
SHOW DDL JOBS;

-- Cancel DDL
ADMIN CANCEL DDL JOBS <job_id>;
```

## Examples
```sql
-- Check DDL status
SHOW DDL JOBS WHERE job_id = 100;
-- Cancel specific DDL
ADMIN CANCEL DDL JOBS 100;
```

