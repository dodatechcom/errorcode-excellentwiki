---
title: "TiDB Statement Error Code"
description: "Statement error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Statement returning specific error code.

## Common Causes
- SQL syntax error
- Type conversion error
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
SELECT * FROM information_schema.slow_query WHERE query LIKE '%error%' ORDER BY query_time DESC;
-- Check statement digest
SELECT digest_text, sum(exec_count) FROM information_schema.statements_summary GROUP BY digest_text ORDER BY sum(exec_count) DESC LIMIT 10;
```

