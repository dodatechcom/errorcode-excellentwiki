---
title: "[Solution] ClickHouse Kill Query Error"
description: "Fix ClickHouse kill query errors when KILL QUERY command fails to stop running queries"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Kill Query Error

Kill query errors occur when the KILL QUERY command cannot stop a running query.

## Common Causes

- Query already completed before kill
- Killing query in different session without permission
- Query ID mismatch
- Query running in SYSTEM operations

## How to Fix

List running queries:

```sql
SELECT query_id, user, query, elapsed FROM system.processes;
```

Kill specific query:

```sql
KILL QUERY WHERE query_id = 'query-id-here';
```

Kill all queries for user:

```sql
KILL QUERY WHERE user = 'problematic_user';
```

## Examples

```sql
SELECT query_id, elapsed, memory_usage FROM system.processes ORDER BY elapsed DESC;
```
