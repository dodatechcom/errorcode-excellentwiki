---
title: "[Solution] ClickHouse Type Mismatch Error"
description: "Fix ClickHouse type mismatch errors when inserting or comparing incompatible types"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Type Mismatch Error

Type mismatch errors occur when inserting or comparing values of incompatible data types.

## Common Causes

- Inserting string into numeric column
- Comparing DateTime with String
- Implicit type conversion not possible
- Array element type mismatch

## How to Fix

Cast types explicitly:

```sql
INSERT INTO my_table SELECT toString(id), name FROM source_table;
```

Check column types:

```sql
SELECT name, type FROM system.columns WHERE table = 'my_table';
```

Use type conversion functions:

```sql
SELECT toDate(event_time) AS date, toInt32(amount) AS amount FROM events;
```

## Examples

```sql
SELECT * FROM my_table WHERE CAST(value AS String) = 'test';
```
