---
title: "[Solution] ClickHouse Column Alter Error"
description: "How to fix ClickHouse ALTER COLUMN errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Column referenced in materialized view
- Column in partition key
- Wrong data type for alter

## How to Fix

```sql
ALTER TABLE mytable MODIFY COLUMN col_name String DEFAULT '';
```

## Examples

```sql
DESCRIBE TABLE mytable;
```
