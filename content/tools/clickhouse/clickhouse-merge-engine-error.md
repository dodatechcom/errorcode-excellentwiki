---
title: "[Solution] ClickHouse Merge Engine Error"
description: "How to fix ClickHouse Merge table engine errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Source tables not found
- Source table schemas incompatible
- Merge expression wrong

## How to Fix

```sql
CREATE TABLE merged_table AS source_table1 ENGINE = Merge(currentDatabase(), 'source_');
```

## Examples

```sql
SHOW CREATE TABLE merged_table;
```
