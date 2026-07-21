---
title: "YugabyteDB Quota Error"
description: "Resource quota exceeded"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Resource quota has been exceeded.

## Common Causes
- Storage quota exceeded
- Connection quota exceeded
- Memory quota exceeded

## How to Fix
```bash
# Check quota usage
yb-admin list_tablets | wc -l

# Increase quota
yb-admin modify_table_placement_info
```

## Examples
```sql
-- Check storage usage
SELECT pg_database_size('mydb');
-- Check connection count
SELECT count(*) FROM pg_stat_activity;
```

