---
title: "[Solution] ClickHouse Drop Table Error"
description: "How to fix ClickHouse DROP TABLE errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Table referenced by view
- Table has active mutations
- Insufficient permissions

## How to Fix

```sql
DROP TABLE IF EXISTS mytable;
```

## Examples

```sql
SHOW TABLES;
```
