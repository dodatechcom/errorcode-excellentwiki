---
title: "[Solution] ClickHouse Schema Error"
description: "Fix ClickHouse schema errors when table schema changes cause query failures"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Schema Error

Schema errors occur when ClickHouse table schema changes cause downstream query failures.

## Common Causes

- Column added but not present in INSERT statement
- Column type changed causing implicit cast failure
- Schema migration partially applied
- Schema difference between replicas

## How to Fix

Check current schema:

```sql
DESCRIBE TABLE my_table;
```

Check schema history:

```sql
SELECT * FROM system.mutations WHERE table = 'my_table';
```

Fix schema mismatch:

```sql
ALTER TABLE my_table ADD COLUMN new_col String DEFAULT '' AFTER existing_col;
```

## Examples

```sql
SELECT database, table, name, type, default_kind
FROM system.columns WHERE table = 'my_table' ORDER BY position;
```
