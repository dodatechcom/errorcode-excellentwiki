---
title: "[Solution] ClickHouse Cannot Insert Error"
description: "How to fix ClickHouse insert operation failures"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Data format mismatch
- Too many columns in insert
- Table is read-only (replicated table)
- Insert size exceeds limits

## How to Fix

Check insert limits:

```sql
SELECT * FROM system.settings WHERE name LIKE '%max_insert%';
```

Use correct format:

```sql
INSERT INTO my_table (col1, col2) FORMAT TabSeparated VALUES (1, 'a');
```

## Examples

```sql
INSERT INTO my_table FORMAT JSONEachRow {"col1": 1, "col2": "a"};
SELECT * FROM system.settings WHERE name LIKE '%max_block_size%';
```
