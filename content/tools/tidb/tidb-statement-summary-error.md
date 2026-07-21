---
title: "TiDB Statement Summary Error"
description: "Statement summary data error"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Statement summary data is incorrect or incomplete.

## Common Causes
- Statement summary disabled
- Memory limit exceeded
- Flush interval too long

## How to Fix
```sql
-- Check statement summary settings
SHOW GLOBAL VARIABLES LIKE 'tidb_enable_stmt_summary%';

-- Enable statement summary
SET GLOBAL tidb_enable_stmt_summary = 1;
```

## Examples
```sql
-- Check statement summary data
SELECT * FROM information_schema.statements_summary ORDER BY exec_count DESC LIMIT 10;
-- Reset statement summary
FLUSH STATEMENTS_SUMMARY;
```

