---
title: "TiDB Statement Error"
description: "SQL statement execution failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
SQL statement is failing to execute.

## Common Causes
- Syntax error
- Type mismatch
- Function not supported

## How to Fix
```sql
-- Check statement errors
SELECT * FROM information_schema.statements_summary WHERE digest_text LIKE '%error%';

-- Check TiDB version
SELECT tidb_version();
```

## Examples
```sql
-- Check slow queries
SELECT * FROM information_schema.slow_query ORDER BY query_time DESC LIMIT 10;
-- Check statement summary
SELECT * FROM information_schema.statements_summary ORDER BY exec_count DESC LIMIT 10;
```

