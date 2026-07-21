---
title: "[Solution] ClickHouse Too Many Parts Error"
description: "Fix ClickHouse too many parts errors when MergeTree table accumulates excessive data parts"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Too Many Parts Error

Too many parts errors occur when a table has more active parts than ClickHouse allows per partition.

## Common Causes

- INSERT rate too high creating many small parts
- Batch size too small for INSERT operations
- Background merge falling behind insert rate
- Partition key creating too many partitions

## How to Fix

Check parts count:

```sql
SELECT database, table, partition, count() AS parts
FROM system.parts WHERE active
GROUP BY database, table, partition
HAVING parts > 100 ORDER BY parts DESC;
```

Force merge:

```sql
OPTIMIZE TABLE my_table PARTITION '2024-01' FINAL;
```

Adjust merge settings:

```sql
SET max_bytes_to_merge_at_max_space_in_pool = 161061273600;
```

## Examples

```sql
SELECT table, count() AS parts FROM system.parts
WHERE database = 'default' AND active
GROUP BY table ORDER BY parts DESC;
```
