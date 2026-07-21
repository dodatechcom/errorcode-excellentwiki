---
title: "TiDB Index Usage Error"
description: "Index usage statistics error"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Index usage statistics are incorrect.

## Common Causes
- Index usage disabled
- Statistics outdated
- Memory limit exceeded

## How to Fix
```sql
-- Check index usage
SELECT * FROM information_schema.tidb_index_usage WHERE table_name = 'mytable';

-- Analyze table
ANALYZE TABLE mytable;
```

## Examples
```sql
-- Check index usage stats
SELECT * FROM information_schema.tidb_index_usage ORDER BY access_count DESC LIMIT 10;
-- Reset index usage
FLUSH tidb_index_usage;
```

