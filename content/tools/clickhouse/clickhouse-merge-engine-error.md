---
title: "[Solution] ClickHouse Merge Engine Error"
description: "Fix ClickHouse Merge table engine errors when merge operations on virtual tables fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Merge Engine Error

Merge engine errors occur when the Merge table engine cannot read from underlying tables.

## Common Causes

- Source table does not exist
- Source tables have different schemas
- Merge regex matching wrong tables
- Source table engine incompatible with Merge

## How to Fix

Check Merge table source:

```sql
SHOW CREATE TABLE merged_table;
```

Verify source tables exist:

```sql
SELECT name, engine FROM system.tables WHERE name LIKE 'logs_%';
```

Fix regex pattern:

```sql
CREATE TABLE merged_logs AS logs_january
ENGINE = Merge(default, '^logs_2024_');
```

## Examples

```sql
SELECT * FROM merged_table WHERE _table = 'logs_january';
```
