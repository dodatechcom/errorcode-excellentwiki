---
title: "[Solution] TiDB TiFlash Replica Sync Error — How to Fix"
description: "Fix TiDB TiFlash replica synchronization errors when replicas cannot catch up with the leader"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TiFlash Replica Sync Error

TiFlash replica sync errors occur when TiFlash replicas cannot synchronize data from TiKV leader regions, causing stale reads and replication lag.

## Why It Happens

- TiFlash node is overloaded and cannot process snapshots
- Network bandwidth between TiKV and TiFlash is insufficient
- Too many regions are being synced simultaneously
- TiFlash storage is full and cannot accept new data
- Raft learner falls too far behind the leader

## Common Error Messages

```
TiFlash replica sync: learner is too far behind leader
```

```
error: TiFlash replica not available for query
```

```
tikv: snapshot send failed to TiFlash
```

## How to Fix It

### 1. Check TiFlash Replica Status

```sql
SELECT * FROM information_schema.tiflash_replica;
SHOW TABLE TABLE_NAME REPLICA;
```

### 2. Set Replica Count

```sql
ALTER TABLE mydb.mytable SET TIFLASH REPLICA 2;
```

### 3. Monitor Sync Progress

```bash
curl -s http://tiflash:9090/metrics | grep tiflash_proxy_raftstore_region_count
```

### 4. Increase TiFlash Resources

```bash
# Check TiFlash resource usage
curl -s http://tiflash:9090/metrics | grep tiflash_system_current_metric
```

## Examples

```
$ SELECT * FROM information_schema.tiflash_replica;
+-----------+----------------+--------------+----------------+
| DB_NAME   | TABLE_NAME     | REPLICA_COUNT | AVAILABLE     |
+-----------+----------------+--------------+----------------+
| mydb      | orders         | 2            | true          |
| mydb      | events         | 2            | false         |
+-----------+----------------+--------------+----------------+
```

## Prevent It

- Monitor TiFlash sync lag and set alerts
- Ensure sufficient resources on TiFlash nodes
- Use appropriate replica counts based on query needs

## Related Pages

- [TiDB TiFlash Replica Error](/tools/tidb/tidb-tiflash-replica-error)
- [TiDB TiFlash Error](/tools/tidb/tidb-tiflash-error)
- [TiDB TiFlash Network Error](/tools/tidb/tidb-tiflash-network-error)
