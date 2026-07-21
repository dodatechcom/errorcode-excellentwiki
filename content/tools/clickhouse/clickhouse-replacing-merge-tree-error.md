---
title: "[Solution] ClickHouse Replacing MergeTree Error"
description: "How to fix ClickHouse ReplacingMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Version column not specified
- Deduplication not working
- Merge not cleaning old rows

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, name String, ver UInt32) ENGINE = ReplacingMergeTree(ver) ORDER BY id;
```

## Examples

```sql
SELECT * FROM mytable FINAL;
```
