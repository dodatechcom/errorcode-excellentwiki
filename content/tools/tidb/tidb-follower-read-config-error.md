---
title: "[Solution] TiDB Follower Read Error — How to Fix"
description: "Fix TiDB follower read errors when reading from follower replicas fails or returns stale data"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Follower Read Error

Follower read errors occur when TiDB cannot read from follower replicas, falling back to leader reads and causing increased latency or failures.

## Why It Happens

- Follower replicas are not available
- Follower read is not enabled for the table
- Follower is too far behind the leader (stale read)
- Network partition prevents follower access
- Follower read timeout is too short

## Common Error Messages

```
follower read: follower is unavailable, falling back to leader
```

```
error: follower read failed, replica not found
```

```
follower read: data is too stale, exceeding acceptable lag
```

## How to Fix It

### 1. Enable Follower Read

```sql
SET tidb_read_staleness = '-5s';
SET tidb_enable_noop_functions = ON;
```

### 2. Check Follower Availability

```bash
pd-ctl region <region_id>
```

### 3. Use Correct Syntax

```sql
-- Read from follower
SELECT /*+ READ_FROM_REPLICA() */ * FROM mytable WHERE id = 1;

-- Enable globally
SET SESSION tidb_read_staleness = '-5s';
```

### 4. Monitor Follower Lag

```bash
curl -s http://tikv:20180/metrics | grep tikv_raftstore_leader_follow_count
```

## Examples

```
mysql> SELECT /*+ READ_FROM_REPLICA() */ * FROM users WHERE id = 1;
+----+-------+
| id | name  |
+----+-------+
| 1  | Alice |
+----+-------+
1 row in set (0.001 sec)
```

## Prevent It

- Monitor follower replication lag
- Ensure all TiKV nodes have healthy followers
- Use follower reads for read-heavy workloads

## Related Pages

- [TiDB Follower Read Error](/tools/tidb/tidb-follower-read-error)
- [TiDB Stale Read Error](/tools/tidb/tidb-stale-read-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
