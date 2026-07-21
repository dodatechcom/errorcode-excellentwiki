---
title: "[Solution] ClickHouse UUID Type Error"
description: "How to fix ClickHouse UUID type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- UUID format wrong
- UUID not generated
- UUID collision

## How to Fix

```sql
SELECT generateUUIDv4();
```

## Examples

```sql
CREATE TABLE mytable (id UUID DEFAULT generateUUIDv4(), name String) ENGINE = MergeTree() ORDER BY id;
```
