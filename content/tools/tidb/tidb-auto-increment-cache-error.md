---
title: "TiDB Auto Increment Cache Error"
description: "AUTO_INCREMENT cache error"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
AUTO_INCREMENT cache is causing issues.

## Common Causes
- Cache size too large
- Cache exhaustion
- Manual value insertion

## How to Fix
```sql
-- Check auto increment
SHOW CREATE TABLE mytable;

-- Adjust cache size
SET @@auto_increment_increment = 1;
SET @@auto_increment_offset = 1;
```

## Examples
```sql
-- Check auto increment status
SELECT * FROM information_schema.tables WHERE table_name = 'mytable';
-- Use AUTO_RANDOM instead
CREATE TABLE mytable (id BIGINT AUTO_RANDOM PRIMARY KEY);
```

