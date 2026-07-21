---
title: "YugabyteDB DDL Error Code"
description: "DDL error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL returning specific error code.

## Common Causes
- Table already exists
- Column type not supported
- Schema change in progress

## How to Fix
```sql
-- Check DDL status
SELECT * FROM information_schema.tables WHERE table_name = 'mytable';

-- Safe DDL
CREATE TABLE IF NOT EXISTS mytable (id INT PRIMARY KEY);
```

## Examples
```sql
-- Check schema changes
SELECT * FROM pg_stat_progress_create_index;
-- Cancel DDL
SELECT pg_cancel_backend(<pid>);
```

