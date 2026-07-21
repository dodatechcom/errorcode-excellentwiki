---
title: "[Solution] ClickHouse Wrong Column Name Error"
description: "How to fix ClickHouse column name not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Column name misspelled
- Column does not exist in table
- Case sensitivity issue
- Column in wrong table

## How to Fix

List columns:

```sql
DESCRIBE TABLE my_table;
SHOW COLUMNS FROM my_table;
```

## Examples

```sql
DESCRIBE TABLE my_table;
SHOW CREATE TABLE my_table;
SELECT name, type FROM system.columns WHERE table = 'my_table';
```
