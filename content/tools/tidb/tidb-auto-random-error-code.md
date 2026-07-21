---
title: "TiDB Auto Random Error Code"
description: "Auto random error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Auto random returning specific error code.

## Common Causes
- Shard bits too few
- Auto Random cache exhausted
- Primary key conflict

## How to Fix
```sql
-- Check AUTO_RANDOM settings
SHOW CREATE TABLE mytable;

-- Adjust shard bits
ALTER TABLE mytable ADD PRIMARY KEY (id AUTO_RANDOM(5, 31));
```

## Examples
```sql
-- Create table with AUTO_RANDOM
CREATE TABLE mytable (id BIGINT AUTO_RANDOM PRIMARY KEY, val TEXT);
-- Check shard distribution
SELECT id >> 32 AS shard, count(*) FROM mytable GROUP BY shard;
```

