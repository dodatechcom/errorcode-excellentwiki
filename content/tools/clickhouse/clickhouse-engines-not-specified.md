---
title: "[Solution] ClickHouse Engine Not Specified Error"
description: "How to fix ClickHouse missing engine specification errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ENGINE clause missing from CREATE TABLE
- Engine specified after ORDER BY
- Engine syntax wrong

## How to Fix

Specify engine correctly:

```sql
CREATE TABLE my_table (
  id UInt32,
  name String
) ENGINE = MergeTree()
ORDER BY id;
```

## Examples

```sql
SHOW CREATE TABLE my_table;
SELECT engine FROM system.tables WHERE name = 'my_table';
```
