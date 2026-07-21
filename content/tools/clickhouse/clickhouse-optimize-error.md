---
title: "[Solution] ClickHouse Optimize Error"
description: "How to fix ClickHouse OPTIMIZE TABLE errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Table locked by merge
- OPTIMIZE on replicated table needs coordination
- Too many parts to merge

## How to Fix

```sql
OPTIMIZE TABLE mytable FINAL;
```

## Examples

```sql
SELECT table, count(), sum(rows) FROM system.parts WHERE active GROUP BY table;
```
