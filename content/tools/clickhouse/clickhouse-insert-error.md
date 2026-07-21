---
title: "[Solution] ClickHouse Insert Error"
description: "How to fix ClickHouse INSERT errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Column count mismatch
- Wrong data type
- Table not found

## How to Fix

```sql
INSERT INTO mytable (id, name) VALUES (1, 'Alice');
```

## Examples

```sql
INSERT INTO mytable SELECT * FROM other_table;
```
