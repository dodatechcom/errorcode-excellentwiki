---
title: "[Solution] ClickHouse Nullable Error"
description: "How to fix ClickHouse Nullable column errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Nullable not supported for engine
- Nullable increasing memory usage
- Nullable with LowCardinality

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, name Nullable(String)) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SELECT * FROM mytable WHERE name IS NOT NULL;
```
