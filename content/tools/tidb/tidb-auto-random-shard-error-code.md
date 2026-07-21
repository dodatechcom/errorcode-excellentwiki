---
title: "TiDB Auto Random Shard Error Code"
description: "Auto random shard error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Auto random shard returning specific error code.

## Common Causes
- Too many shards
- Shard bits too few
- High write concurrency

## How to Fix
```sql
-- Check shard configuration
SHOW CREATE TABLE mytable;

-- Increase shard bits
ALTER TABLE mytable DROP PRIMARY KEY, ADD PRIMARY KEY (id AUTO_RANDOM(8, 31));
```

## Examples
```sql
-- Monitor shard distribution
SELECT id >> 32 AS shard, count(*) FROM mytable GROUP BY shard ORDER BY shard;
-- Check shard bits
SHOW CREATE TABLE mytable;
```

