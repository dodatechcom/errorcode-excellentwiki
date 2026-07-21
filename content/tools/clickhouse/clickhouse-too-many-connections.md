---
title: "[Solution] ClickHouse Too Many Connections Error"
description: "How to fix ClickHouse connection limit errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Connection pool not releasing connections
- Too many concurrent clients
- max_concurrent_queries reached
- Connection leak in application

## How to Fix

Check connection count:

```sql
SELECT * FROM system.settings WHERE name = 'max_concurrent_queries';
SELECT count() FROM system.processes;
```

Kill idle queries:

```sql
KILL QUERY WHERE query_id NOT IN (SELECT query_id FROM system.processes WHERE is_initial_query = 1);
```

## Examples

```sql
SELECT count() FROM system.processes;
SELECT * FROM system.settings WHERE name LIKE '%concurrent%';
```
