---
title: "[Solution] ClickHouse Insert Deduplication Error"
description: "How to fix ClickHouse insert deduplication errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Duplicate block detected
- insert_deduplicate too aggressive
- Same data inserted twice

## How to Fix

Check dedup settings:

```sql
SELECT * FROM system.settings WHERE name LIKE '%dedup%';
```

Disable dedup for specific insert:

```sql
INSERT INTO my_table SETTINGS insert_deduplicate = 0 VALUES (1, 'a');
```

## Examples

```sql
SELECT * FROM system.settings WHERE name LIKE '%dedup%';
```
