---
title: "[Solution] ClickHouse CollapsingMergeTree Error"
description: "How to fix ClickHouse CollapsingMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Sign column not specified
- Sign values not 1 or -1
- Order key wrong

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, val UInt64, sign Int8) ENGINE = CollapsingMergeTree(sign) ORDER BY id;
```

## Examples

```sql
SELECT * FROM mytable FINAL;
```
