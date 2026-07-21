---
title: "[Solution] ClickHouse Replica Recovery Error"
description: "Fix ClickHouse replica recovery errors when a replica cannot resync after downtime"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Replica Recovery Error

Replica recovery errors occur when a ClickHouse replica cannot recover its replication state after being offline.

## Common Causes

- Replica missed too many mutations
- ZooKeeper log rotated before replica caught up
- Data corruption requiring clone from another replica
- Replication queue stuck with broken entries

## How to Fix

Check replica queue:

```sql
SELECT database, table, queue_size, inserts_in_queue, merges_in_queue
FROM system.replicas WHERE is_readonly = 1;
```

Reset replica:

```sql
SYSTEM RESTART REPLICA my_table;
```

Clone replica:

```sql
SYSTEM RESTORE REPLICA my_table;
```

## Examples

```sql
SELECT database, table, absolute_delay, queue_size
FROM system.replicas WHERE absolute_delay > 60;
```
