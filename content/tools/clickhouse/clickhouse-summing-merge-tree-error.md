---
title: "[Solution] ClickHouse SummingMergeTree Error"
description: "How to fix ClickHouse SummingMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Sum columns not specified
- Sum producing wrong values
- Non-numeric column in sum

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, value UInt64) ENGINE = SummingMergeTree() ORDER BY id;
```

## Examples

```sql
SELECT id, sum(value) FROM mytable GROUP BY id;
```
