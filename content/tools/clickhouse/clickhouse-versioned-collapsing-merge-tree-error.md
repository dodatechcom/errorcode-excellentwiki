---
title: "[Solution] ClickHouse VersionedCollapsingMergeTree Error"
description: "How to fix ClickHouse VersionedCollapsingMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Version column type wrong
- Sign column type wrong
- Merge order wrong

## How to Fix

```sql
CREATE TABLE mytable (id UInt64, val UInt64, sign Int8, ver UInt32) ENGINE = VersionedCollapsingMergeTree(sign, ver) ORDER BY id;
```

## Examples

```sql
SELECT * FROM mytable FINAL;
```
