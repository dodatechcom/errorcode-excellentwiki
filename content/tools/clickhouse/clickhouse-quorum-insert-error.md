---
title: "[Solution] ClickHouse Quorum INSERT Error"
description: "Fix ClickHouse quorum INSERT errors when synchronous replication writes fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Quorum INSERT Error

Quorum INSERT errors occur when synchronous replication cannot write to the required number of replicas.

## Common Causes

- Not enough replicas available for quorum
- Replica lag exceeding quorum timeout
- ZooKeeper unable to coordinate quorum
- Network partition between replicas

## How to Fix

Check replica status:

```sql
SELECT database, table, is_leader, is_readonly, future_parts, queue_size
FROM system.replicas;
```

Increase quorum timeout:

```sql
INSERT INTO my_table SETTINGS inserts_with_quorum_timeout = 60000;
```

Check ZooKeeper quorum nodes:

```sql
SELECT * FROM system.zookeeper WHERE path LIKE '/clickhouse/tables/%/replicas';
```

## Examples

```sql
INSERT INTO my_table VALUES (1, 'test') SETTINGS insert_quorum = 2;
```
