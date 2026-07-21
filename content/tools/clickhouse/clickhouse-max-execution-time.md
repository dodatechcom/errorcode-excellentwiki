---
title: "[Solution] ClickHouse Max Execution Time Error"
description: "Fix ClickHouse query timeout errors when queries exceed max_execution_time limit"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Max Execution Time Error

Max execution time errors occur when queries run longer than the configured timeout limit.

## Common Causes

- Query scanning too many rows without filters
- Missing primary key or index usage
- Complex JOIN operations on large tables
- GROUP BY on high-cardinality column

## How to Fix

Check current timeout:

```sql
SELECT name, value FROM system.settings WHERE name = 'max_execution_time';
```

Set query timeout:

```sql
SET max_execution_time = 60;
SELECT * FROM large_table WHERE date > today() - 30;
```

Optimize query with filters:

```sql
SELECT * FROM events WHERE event_date = today() LIMIT 1000;
```

## Examples

```sql
SELECT count() FROM huge_table WHERE status = 'active';
```
