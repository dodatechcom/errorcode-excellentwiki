---
title: "[Solution] ClickHouse Too Many Parts Error"
description: "How to fix ClickHouse too many parts errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Too many small inserts creating many parts
- Merge cannot keep up with inserts
- Part merge settings too restrictive
- High write throughput

## How to Fix

Batch inserts:

```sql
-- Insert in larger batches every 1000 rows or every second
```

Check part count:

```sql
SELECT count() FROM system.parts WHERE table = 'my_table' AND active;
```

## Examples

```sql
SELECT count() AS part_count, sum(rows) AS total_rows FROM system.parts WHERE table = 'my_table' AND active;
SELECT * FROM system.merges WHERE table = 'my_table';
```
