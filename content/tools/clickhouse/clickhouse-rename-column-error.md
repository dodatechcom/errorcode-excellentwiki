---
title: "[Solution] ClickHouse Rename Column Error"
description: "How to fix ClickHouse column rename errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Column referenced in view
- Column in partition key
- Replication conflict

## How to Fix

```sql
ALTER TABLE mytable RENAME COLUMN old_name TO new_name;
```

## Examples

```sql
DESCRIBE TABLE mytable;
```
