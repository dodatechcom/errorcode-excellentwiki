---
title: "[Solution] ClickHouse Replication Lag Error"
description: "How to fix ClickHouse replication lag errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replica falling behind on mutations
- ZooKeeper queue too deep
- Network issues between replicas
- Replica overloaded

## How to Fix

Check replication status:

```sql
SELECT * FROM system.replicas WHERE table = 'my_table';
```

Restart replica:

```sql
SYSTEM RESTART REPLICA my_table;
```

## Examples

```sql
SELECT database, table, future_parts, parts_to_check, queue_size FROM system.replicas;
```
