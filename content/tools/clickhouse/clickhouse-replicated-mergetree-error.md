---
title: "[Solution] ClickHouse Replicated MergeTree Error"
description: "Fix ClickHouse ReplicatedMergeTree errors when replicated table operations fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Replicated MergeTree Error

Replicated MergeTree errors occur when ReplicatedMergeTree engine cannot synchronize across replicas.

## Common Causes

- ZooKeeper node missing for table
- Replication path conflict between tables
- Replica ID mismatch in cluster config
- Table creation without proper ZooKeeper path

## How to Fix

Check replication path:

```sql
SELECT name, engine, metadata_path FROM system.tables WHERE engine = 'ReplicatedMergeTree';
```

Verify ZooKeeper path exists:

```sql
SELECT * FROM system.zookeeper WHERE path = '/clickhouse/tables/{cluster}/my_table';
```

Reset replication:

```sql
SYSTEM RESTART REPLICA my_table;
```

## Examples

```sql
CREATE TABLE my_table (id UInt64, name String)
ENGINE = ReplicatedMergeTree('/clickhouse/tables/{cluster}/my_table/replica', '{replica}')
ORDER BY id;
```
