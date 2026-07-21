---
title: "YugabyteDB Auto-Vacuum Error"
description: "Automatic vacuum operation failure"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
YugabyteDB auto-vacuum is failing or not running.

## Common Causes
- Vacuum worker process crashed
- Table too large for vacuum
- Insufficient disk space

## How to Fix
```sql
-- Check vacuum status
SELECT * FROM pg_stat_user_tables WHERE relname = 'mytable';

-- Manual vacuum
VACUUM mytable;
```

## Examples
```sql
-- Check vacuum settings
SHOW autovacuum_vacuum_threshold;
SHOW autovacuum_vacuum_scale_factor;
-- Run verbose vacuum
VACUUM (VERBOSE) mytable;
```

