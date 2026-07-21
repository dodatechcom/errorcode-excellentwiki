---
title: "[Solution] ClickHouse Partition Pruning Error"
description: "How to fix ClickHouse partition pruning errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query not using partition key
- Partition key not in WHERE clause
- Query planner not pruning

## How to Fix

```sql
EXPLAIN SELECT * FROM mytable WHERE toYYYYMM(date) = '202401';
```

## Examples

```sql
SELECT * FROM mytable WHERE date >= '2024-01-01' AND date < '2024-02-01';
```
