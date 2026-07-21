---
title: "[Solution] ClickHouse AggregatingMergeTree Error"
description: "How to fix ClickHouse AggregatingMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Aggregate function not matching column type
- State function not specified
- Merge function wrong

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, val AggregateFunction(avg, UInt64)) ENGINE = AggregatingMergeTree() ORDER BY id;
```

## Examples

```sql
SELECT id, avgMerge(val) FROM mytable GROUP BY id;
```
