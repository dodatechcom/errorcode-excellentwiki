---
title: "[Solution] ClickHouse Too Many Partitions Error"
description: "How to fix ClickHouse partition count limit errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Partition key creating too many partitions
- High-cardinality partition key
- Daily partitioning on long time range

## How to Fix

Check partition count:

```sql
SELECT count() AS partitions FROM system.parts WHERE table = 'my_table' AND active;
```

Use less granular partitioning:

```sql
-- Instead of daily
PARTITION BY toYYYYMM(event_date)  -- Monthly
```

## Examples

```sql
SELECT partition, count() AS parts FROM system.parts WHERE table = 'my_table' AND active GROUP BY partition;
```
