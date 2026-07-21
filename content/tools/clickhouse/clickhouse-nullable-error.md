---
title: "[Solution] ClickHouse Nullable Error"
description: "Fix ClickHouse Nullable type errors when using Nullable columns in operations"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Nullable Error

Nullable type errors occur when ClickHouse operations cannot handle NULL values in Nullable columns.

## Common Causes

- Nullable column used in ORDER BY
- Nullable column in primary key
- Aggregate function receiving only NULL values
- Nullable array containing non-array type

## How to Fix

Avoid Nullable in primary key:

```sql
-- Nullable not allowed in ORDER BY
CREATE TABLE t (id UInt64, name String DEFAULT '') ENGINE = MergeTree() ORDER BY id;
```

Use COALESCE for NULL handling:

```sql
SELECT id, COALESCE(name, 'unknown') AS name FROM my_table;
```

Check Nullable columns:

```sql
SELECT name, type, is_nullable FROM system.columns WHERE table = 'my_table';
```

## Examples

```sql
SELECT id, if(name IS NOT NULL, name, 'N/A') AS name FROM my_table;
```
