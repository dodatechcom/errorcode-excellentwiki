---
title: "[Solution] ClickHouse Deduplication Error"
description: "Fix ClickHouse deduplication errors when ReplacingMergeTree removes wrong rows"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Deduplication Error

Deduplication errors occur when ReplacingMergeTree incorrectly deduplicates rows during merge.

## Common Causes

- Version column not properly configured
- Duplicate rows with same sorting key but different data
- FINAL query missing for exact deduplication
- Merge not yet completed for latest data

## How to Fix

Check deduplication settings:

```sql
SELECT name, engine, sorting_key, version_column
FROM system.tables WHERE engine = 'ReplacingMergeTree';
```

Query with FINAL for deduplicated results:

```sql
SELECT * FROM my_table FINAL ORDER BY id;
```

Force merge for deduplication:

```sql
OPTIMIZE TABLE my_table FINAL;
```

## Examples

```sql
SELECT id, name, version FROM my_table FINAL WHERE id = 1;
```
