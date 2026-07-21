---
title: "[Solution] ClickHouse Column Not Found Error"
description: "Fix ClickHouse column not found errors when queries reference non-existent columns"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Column Not Found Error

Column not found errors occur when a query references a column that does not exist in the table.

## Common Causes

- Column renamed in table schema
- Typo in column name
- Query referencing wrong table
- Column added by migration not yet applied

## How to Fix

Check table schema:

```sql
DESCRIBE TABLE my_table;
```

Check system columns:

```sql
SELECT name, type, default_kind FROM system.columns
WHERE table = 'my_table' AND database = 'default';
```

Add missing column:

```sql
ALTER TABLE my_table ADD COLUMN new_column String DEFAULT '';
```

## Examples

```sql
SELECT * FROM system.columns WHERE table = 'events' AND name LIKE '%time%';
```
