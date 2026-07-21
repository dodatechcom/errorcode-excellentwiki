---
title: "[Solution] ClickHouse View Not Found Error"
description: "How to fix ClickHouse view not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- View deleted
- View name misspelled
- Wrong database specified

## How to Fix

List views:

```sql
SELECT name FROM system.tables WHERE engine IN ('View', 'MaterializedView');
```

## Examples

```sql
SHOW TABLES WHERE engine = 'View';
SHOW TABLES WHERE engine = 'MaterializedView';
```
