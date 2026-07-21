---
title: "[Solution] ClickHouse Async Insert Error"
description: "How to fix ClickHouse asynchronous insert errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Async insert queue full
- Async inserts disabled
- Timeout waiting for batch

## How to Fix

Enable async inserts:

```sql
SET async_insert = 1;
SET wait_for_async_insert = 1;
```

## Examples

```sql
SET async_insert = 1;
SET async_insert_busy_timeout_ms = 200;
INSERT INTO my_table SELECT * FROM source_table;
```
