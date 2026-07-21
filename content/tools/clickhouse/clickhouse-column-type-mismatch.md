---
title: "[Solution] ClickHouse Column Type Mismatch"
description: "How to fix ClickHouse column type mismatch errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Inserting wrong data type into column
- Implicit type conversion failing
- Function returning wrong type

## How to Fix

Check column types:

```sql
DESCRIBE TABLE my_table;
```

Cast types explicitly:

```sql
SELECT CAST('2024-01-01' AS Date);
SELECT toUInt32('123');
SELECT toString(42);
```

## Examples

```sql
DESCRIBE TABLE my_table;
SELECT toTypeName(column_name) FROM my_table LIMIT 1;
```
