---
title: "[Solution] ClickHouse Enum Error"
description: "How to fix ClickHouse Enum type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Enum value not defined
- Inserting invalid enum value
- Enum type mismatch

## How to Fix

```sql
CREATE TABLE mytable (status Enum8('active' = 1, 'inactive' = 2)) ENGINE = MergeTree() ORDER BY tuple();
```

## Examples

```sql
SELECT CAST('active' AS Enum8('active' = 1, 'inactive' = 2));
```
