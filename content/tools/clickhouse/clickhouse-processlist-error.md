---
title: "[Solution] ClickHouse Processlist Error"
description: "Fix ClickHouse processlist errors when system.processes shows stuck or zombie queries"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Processlist Error

Processlist errors occur when ClickHouse system.processes shows queries that appear stuck or unresponsive.

## Common Causes

- Query waiting on IO operation
- Query blocked by another query's lock
- Network timeout on distributed query
- Query consuming all available threads

## How to Fix

Check running queries:

```sql
SELECT query_id, user, elapsed, query FROM system.processes ORDER BY elapsed DESC;
```

Kill long-running query:

```sql
KILL QUERY WHERE query_id = 'stuck-query-id';
```

Check thread pool usage:

```sql
SELECT * FROM system.metric_log WHERE metric = 'QueryThread';
```

## Examples

```sql
SELECT query, elapsed, memory_usage, read_rows FROM system.processes
WHERE elapsed > 60 ORDER BY elapsed DESC;
```
