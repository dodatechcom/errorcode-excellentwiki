---
title: "TiDB DDL Error Code"
description: "DDL error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL operation returning specific error code.

## Common Causes
- Table already exists
- Column type not supported
- Index conflict

## How to Fix
```sql
-- Check DDL errors
SHOW DDL JOBS WHERE state = 'failed';

-- Check table structure
SHOW CREATE TABLE mytable;
```

## Examples
```sql
-- Check DDL job details
SHOW DDL JOB QUERIES <job_id>;
-- Retry failed DDL
ALTER TABLE mytable ADD COLUMN newcol INT;
```

