---
title: "[Solution] ClickHouse Lightweight Delete Error"
description: "How to fix ClickHouse lightweight delete errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Lightweight delete not supported for table engine
- Delete predicate too broad
- Delete causing excessive parts

## How to Fix

Use lightweight delete:

```sql
ALTER TABLE my_table DELETE WHERE id = 42;
```

Check delete status:

```sql
SELECT * FROM system.mutations WHERE table = 'my_table';
```

## Examples

```sql
ALTER TABLE my_table DELETE WHERE event_date = '2024-01-01';
SELECT * FROM system.mutations WHERE table = 'my_table' AND is_done = 0;
```
