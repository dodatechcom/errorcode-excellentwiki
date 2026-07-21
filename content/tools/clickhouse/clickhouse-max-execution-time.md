---
title: "[Solution] ClickHouse Max Execution Time Error"
description: "How to fix ClickHouse query timeout errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query too complex or scanning too much data
- max_execution_time too low
- Full table scan on large table
- Stuck query blocking resources

## How to Fix

Increase timeout:

```sql
SET max_execution_time = 600;
```

Kill slow query:

```sql
KILL QUERY WHERE query_id = 'QUERY_ID';
```

## Examples

```sql
SELECT * FROM system.processes;
KILL QUERY WHERE query_id = 'abc-123-def';
SET max_execution_time = 300;
```
