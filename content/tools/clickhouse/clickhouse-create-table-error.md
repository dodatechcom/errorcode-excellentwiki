---
title: "[Solution] ClickHouse Create Table Error"
description: "How to fix ClickHouse CREATE TABLE errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Table already exists
- Engine not specified
- Column type not supported

## How to Fix

```sql
CREATE TABLE IF NOT EXISTS mytable (id UInt64, name String) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SHOW CREATE TABLE mytable;
```
