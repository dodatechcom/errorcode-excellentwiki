---
title: "[Solution] ClickHouse Update Error"
description: "How to fix ClickHouse ALTER UPDATE errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Column not found
- Wrong data type for update
- Table is read-only

## How to Fix

```sql
ALTER TABLE mytable UPDATE name = 'Bob' WHERE id = 1;
```

## Examples

```sql
SELECT * FROM mytable WHERE id = 1;
```
