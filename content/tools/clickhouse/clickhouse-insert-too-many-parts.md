---
title: "[Solution] ClickHouse Insert Too Many Parts"
description: "How to fix ClickHouse too many parts on insert"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Batch inserts too small
- Insert frequency too high
- Merge falling behind

## How to Fix

```xml
<merge_tree>
  <max_delay_to_insert>10</max_delay_to_insert>
</merge_tree>
```

## Examples

```sql
SELECT table, count() FROM system.parts GROUP BY table HAVING count() > 100;
```
