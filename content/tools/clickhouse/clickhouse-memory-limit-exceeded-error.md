---
title: "[Solution] ClickHouse Memory Limit Exceeded Error"
description: "Fix ClickHouse memory limit exceeded errors when queries consume too much RAM"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Memory Limit Exceeded Error

Memory limit exceeded errors occur when a query requires more memory than the configured limit.

## Common Causes

- Query processing too many rows in memory
- GROUP BY on high-cardinality column without disk spilling
- Large hash JOIN operations
- Unbounded array or string operations

## How to Fix

Check memory limit:

```sql
SELECT name, value FROM system.settings WHERE name = 'max_memory_usage';
```

Increase per-query memory:

```sql
SET max_memory_usage = 10000000000;
```

Enable external aggregation:

```sql
SET max_bytes_before_external_group_by = 5000000000;
```

Monitor memory usage:

```sql
SELECT query, memory_usage, peak_memory_usage FROM system.processes;
```

## Examples

```sql
SELECT user_id, count() FROM events GROUP BY user_id
SETTINGS max_bytes_before_external_group_by = 5000000000;
```
