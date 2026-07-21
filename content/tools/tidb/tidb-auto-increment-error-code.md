---
title: "TiDB Auto Increment Error Code"
description: "Auto increment error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Auto increment returning specific error code.

## Common Causes
- Auto Increment cache too large
- Manual value insertion
- Table truncate without resetting

## How to Fix
```sql
-- Check auto increment
SHOW CREATE TABLE mytable;

-- Reset auto increment
ALTER TABLE mytable AUTO_INCREMENT = 1;
```

## Examples
```sql
-- Use AUTO_RANDOM for distributed
CREATE TABLE mytable (id BIGINT AUTO_RANDOM PRIMARY KEY, val TEXT);
-- Check auto increment status
SELECT * FROM information_schema.tables WHERE table_name = 'mytable';
```

