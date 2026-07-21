---
title: "[Solution] ClickHouse Memory Limit Exceeded"
description: "How to fix ClickHouse memory limit exceeded errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query requires more memory than allowed
- max_memory_usage too low
- Large JOIN or GROUP BY operation
- Too many concurrent queries

## How to Fix

Increase memory for query:

```sql
SET max_memory_usage = 10000000000;
```

Use GROUP BY with external sorting:

```sql
SET max_bytes_before_external_group_by = 10000000000;
```

## Examples

```sql
SET max_memory_usage = 20000000000;
SELECT count() FROM big_table GROUP BY high_cardinality_column;
SELECT * FROM system.settings WHERE name LIKE '%max_memory%';
```
