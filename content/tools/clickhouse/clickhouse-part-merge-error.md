---
title: "[Solution] ClickHouse Part Merge Error"
description: "Fix ClickHouse part merge errors when background merge operations fail on MergeTree tables"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Part Merge Error

Part merge errors occur when ClickHouse background merge cannot combine data parts due to conflicts or resource issues.

## Common Causes

- Too many parts causing merge queue backlog
- Disk IO saturation preventing merge progress
- Merge conflict with concurrent INSERT operations
- Part size exceeding configured max merge size

## How to Fix

Check merge status:

```sql
SELECT * FROM system.merges;
```

Check parts count:

```sql
SELECT table, count() AS parts FROM system.parts WHERE active GROUP BY table ORDER BY parts DESC;
```

Force merge:

```sql
OPTIMIZE TABLE my_table FINAL;
```

## Examples

```sql
SELECT database, table, count() AS parts, sum(rows) AS total_rows
FROM system.parts WHERE active
GROUP BY database, table ORDER BY parts DESC;
```
