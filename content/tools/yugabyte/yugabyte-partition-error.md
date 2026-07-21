---
title: "YugabyteDB Partition Error"
description: "Hash or range partition failure"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Table partitioning is failing or misconfigured.

## Common Causes
- Partition key mismatch
- Too many partitions
- Partition bounds error

## How to Fix
```sql
-- Check table partitioning
\d+ mytable

-- Create table with proper partitioning
CREATE TABLE mytable (
  id INT,
  created_at TIMESTAMP
) PARTITION BY RANGE (created_at);
```

## Examples
```sql
-- Check partition info
SELECT * FROM pg_class WHERE relname = 'mytable';
-- Create partition
CREATE TABLE mytable_2024_01 PARTITION OF mytable
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

