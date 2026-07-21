---
title: "[Solution] ClickHouse MergeTree Error"
description: "How to fix ClickHouse MergeTree engine errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Missing ORDER BY clause
- PRIMARY KEY and ORDER BY mismatch
- Partition expression invalid
- MergeTree settings incompatible

## How to Fix

```sql
CREATE TABLE my_table (
  id UInt32,
  event_date Date
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(event_date)
ORDER BY (event_date, id);
```

## Examples

```sql
SELECT * FROM system.merges WHERE table = 'my_table';
SELECT * FROM system.parts WHERE table = 'my_table' AND active;
```
