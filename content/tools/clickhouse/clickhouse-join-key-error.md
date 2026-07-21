---
title: "[Solution] ClickHouse Join Key Error"
description: "Fix ClickHouse JOIN key errors when join conditions reference wrong columns"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Join Key Error

Join key errors occur when ClickHouse JOIN operations have mismatched or invalid key columns.

## Common Causes

- Join key columns with different data types
- Missing index on join key column
- Join producing Cartesian product
- JOIN ON clause referencing wrong table alias

## How to Fix

Check column types:

```sql
SELECT name, type FROM system.columns WHERE table IN ('table_a', 'table_b');
```

Ensure type matching:

```sql
SELECT a.id, b.name
FROM table_a AS a
INNER JOIN table_b AS b ON a.id = toUInt64(b.a_id);
```

Add indexes for join keys:

```sql
CREATE INDEX idx_a_id ON table_a (id) TYPE minmax GRANULARITY 4;
```

## Examples

```sql
SELECT a.*, b.name FROM orders AS a
INNER JOIN users AS b ON a.user_id = b.id;
```
