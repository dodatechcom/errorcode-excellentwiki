---
title: "[Solution] ClickHouse Table TTL Error"
description: "How to fix ClickHouse table TTL configuration errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TTL expression references non-existent column
- TTL set on engine that does not support it
- TTL delete too aggressive
- TTL not yet enforced (waiting for merge)

## How to Fix

Set TTL:

```sql
ALTER TABLE my_table MODIFY TTL event_date + INTERVAL 30 DAY;
```

Check TTL status:

```sql
SELECT table, ttl FROM system.parts WHERE active AND table = 'my_table';
```

## Examples

```sql
ALTER TABLE my_table MODIFY TTL event_date + INTERVAL 90 DAY DELETE;
SELECT * FROM system.parts WHERE table = 'my_table' AND ttl <= now();
```
