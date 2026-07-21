---
title: "[Solution] ClickHouse Distributed Subquery Error"
description: "How to fix ClickHouse distributed subquery errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Distributed table used in subquery
- Data not available on all shards
- Network timeout during distributed query

## How to Fix

Use local tables in subqueries:

```sql
SELECT * FROM distributed_table WHERE id IN (SELECT id FROM local_table);
```

## Examples

```sql
SELECT * FROM system.distributed WHERE table = 'my_table';
```
