---
title: "[Solution] ClickHouse LowCardinality Error"
description: "How to fix ClickHouse LowCardinality errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Too many distinct values for LowCardinality
- LowCardinality with Nullable
- Performance degradation

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, status LowCardinality(String)) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SELECT DISTINCT status FROM mytable;
```
