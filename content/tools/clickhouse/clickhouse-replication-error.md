---
title: "[Solution] ClickHouse Replication Error"
description: "Fix ClickHouse replication errors when ReplicatedMergeTree cannot sync data between replicas"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Replication Error

Replication errors occur when ClickHouse replicas cannot synchronize data due to ZooKeeper issues or configuration problems.

## Common Causes

- ZooKeeper session expired
- Replica falls too far behind and needs manual sync
- Replication path mismatch between replicas
- Data corruption on one replica

## How to Fix

Check replication status:

```sql
SELECT * FROM system.replicas;
```

Check ZooKeeper connection:

```sql
SELECT * FROM system.zookeeper WHERE path = '/clickhouse';
```

Restart replication:

```sql
SYSTEM RESTART REPLICA my_table;
```

## Examples

```sql
SELECT database, table, is_leader, is_readonly, future_parts, parts_to_check
FROM system.replicas;
```
