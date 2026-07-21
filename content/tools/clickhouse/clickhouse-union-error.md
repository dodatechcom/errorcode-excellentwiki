---
title: "[Solution] ClickHouse Union Error"
description: "How to fix ClickHouse UNION errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Column count mismatch
- Column type mismatch
- UNION ALL vs UNION distinction

## How to Fix

```sql
SELECT id, name FROM table_a UNION ALL SELECT id, name FROM table_b;
```

## Examples

```sql
SELECT id, name FROM table_a UNION DISTINCT SELECT id, name FROM table_b;
```
