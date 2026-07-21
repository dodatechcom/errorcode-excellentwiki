---
title: "[Solution] ClickHouse IN Function Error"
description: "How to fix ClickHouse IN function errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- IN list too large
- Type mismatch in IN
- IN subquery returning duplicates

## How to Fix

```sql
SELECT * FROM mytable WHERE id IN (1, 2, 3);
```

## Examples

```sql
SELECT * FROM mytable WHERE id IN (SELECT id FROM other_table);
```
