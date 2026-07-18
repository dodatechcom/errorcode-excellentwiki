---
title: "[Solution] ClickHouse Replication Error — How to Fix"
description: "Fix ClickHouse replication errors including ZooKeeper connection issues, sync failures, replica lag, and data inconsistency between nodes"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Replication Error

ClickHouse replication errors occur when replicated tables (ReplicatedMergeTree family) cannot synchronize data between replicas. This is caused by ZooKeeper issues, network partitions, disk failures, or configuration problems.

## Why It Happens

- ZooKeeper cluster is down or unreachable
- The replica cannot read or write to ZooKeeper
- Network partition between replicas
- Disk space is full on one replica
- The replica's replication path does not match the ZooKeeper path
- A merge conflict occurs between replicas
- The replica is too far behind and cannot catch up

## Common Error Messages

```
Code: 242. DB::Exception: Table mydb.mytable is readonly
```

```
Code: 225. DB::Exception: All attempts to insert into replicated table failed
```

```
DB::Exception: ZooKeeper session has expired
```

```
Code: 47. DB::Exception: Replica does not have part
```

## How to Fix It

### 1. Check ZooKeeper Status

```bash
# Check if ZooKeeper is running
echo ruok | nc localhost 2181

# Check ClickHouse ZooKeeper connection
clickhouse-client --query "SELECT * FROM system.zookeeper WHERE path = '/'"

# Check replication status
clickhouse-client --query "SELECT * FROM system.replicas FORMAT Vertical"
```

### 2. Fix Read-Only Replica

```sql
-- Check why replica is readonly
SELECT database, table, is_readonly, absolute_delay, queue_size
FROM system.replicas
WHERE is_readonly = 1;

-- Force a sync
SYSTEM RESTART REPLICA mydb.mytable;

-- Or reset the replica
SYSTEM RESET REPLICA mydb.mytable;
```

### 3. Fix ZooKeeper Session Expiry

```bash
# Check ZooKeeper logs
tail -f /var/log/zookeeper/zookeeper.log

# Restart ZooKeeper
sudo systemctl restart zookeeper

# After ZooKeeper restarts, check ClickHouse replicas
clickhouse-client --query "SELECT database, table, is_readonly FROM system.replicas"
```

### 4. Fix Replica Sync Issues

```sql
-- Check replication queue
SELECT database, table, type, num_tries, last_exception
FROM system.replication_queue
WHERE num_tries > 3;

-- Check part distribution across replicas
SELECT database, table, partition, count()
FROM system.parts
WHERE active = 1
GROUP BY database, table, partition
ORDER BY count() DESC;
```

## Common Scenarios

- **ZooKeeper cluster restart causes readonly replicas**: Wait for ZooKeeper to recover, then `SYSTEM RESTART REPLICA`.
- **Replica lag after bulk insert**: Normal after large inserts. Monitor `absolute_delay` metric.
- **Network partition causes split brain**: Ensure only one partition is active. Use `SYSTEM RESTART REPLICA` to resync.

## Prevent It

- Run ZooKeeper cluster with at least 3 nodes for high availability
- Monitor `system.replicas` for `is_readonly` and `absolute_delay`
- Set up alerts for ZooKeeper session expiry in ClickHouse logs

## Related Pages

- [ClickHouse Zookeeper Error](/tools/clickhouse/clickhouse-zookeeper-error)
- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Merge Error](/tools/clickhouse/clickhouse-merge-error)
