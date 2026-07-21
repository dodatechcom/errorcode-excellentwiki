---
title: "[Solution] ClickHouse Delete Error"
description: "How to fix ClickHouse DELETE errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Table is MergeTree (no DELETE without ALTER)
- Mutation already running
- Condition matches no rows

## How to Fix

```sql
ALTER TABLE mytable DELETE WHERE id = 1;
```

## Examples

```sql
SELECT * FROM system.mutations WHERE table = 'mytable';
```
