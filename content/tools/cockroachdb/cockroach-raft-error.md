---
title: "[Solution] CockroachDB Raft Error - Fix Raft Leader Election Failed"
description: "Fix CockroachDB Raft leader election failures. Resolve Raft consensus issues, leader leases, and range availability problems."
tools: ["cockroachdb"]
error-types: ["raft-error"]
severities: ["critical"]
weight: 5
---

This error means the Raft consensus protocol cannot elect or maintain a leader for a range. Raft is the distributed consensus algorithm that ensures data consistency.

## What This Error Means

When Raft leader election fails, you see:

```
ERROR: range has no lease holder; r1: leader lease required
# or
ERROR: raft: no leader
# or
Lease transfer failed: no live stores
```

Raft requires a majority of replicas to elect a leader. Without a leader, no reads or writes can be served for the affected range.

## Why It Happens

- A quorum of replicas is unavailable
- Network partitions isolated the range replicas
- The current leader node crashed
- Disk I/O is too slow for Raft heartbeats
- Too many nodes are down to form a quorum
- The Raft election timeout has been exceeded

## How to Fix It

### Check node status

```bash
cockroach node status --insecure
```

Ensure enough nodes are up to form quorum.

### Check range status

```sql
SELECT range_id, lease_holder, replicas, range_size
FROM [SHOW RANGES FROM TABLE my_table]
WHERE range_id = 1;
```

### Monitor Raft activity

```sql
SELECT * FROM crdb_internal.ranges
WHERE lease_holder IS NULL;
```

Ranges without a lease holder have leader election problems.

### Restart down nodes

```bash
sudo systemctl start cockroach
```

Recovering nodes restores quorum availability.

### Check for network partitions

```bash
cockroach node status --ranges --stats
```

Check range availability and replica distribution.

### Decommission permanently failed nodes

```bash
cockroach node decommission <node-id> --insecure
```

Removing failed nodes allows remaining nodes to form new quorums.

### Check disk performance

```bash
iostat -x 1 5
```

Slow disk I/O can cause Raft heartbeats to time out.

### Monitor Raft election timeouts

```sql
SHOW CLUSTER SETTING server.raft_election_timeout_ticks;
```

Default is 3 seconds. Increasing it helps with slow networks.

### Use leaseholder reads

```sql
SELECT * FROM my_table AS OF SYSTEM TIME follower_read_timestamp();
```

Follower reads avoid hitting the leader for reads.

### Check replica health

```sql
SELECT range_id, replicas, lease_holder
FROM [SHOW RANGES FROM DATABASE mydb]
WHERE lease_holder IS NULL;
```

## Common Mistakes

- Running fewer than 3 nodes, which cannot maintain quorum
- Not monitoring Raft leader election as a cluster health indicator
- Not decommissioning permanently failed nodes
- Assuming CockroachDB will automatically recover without intervention
- Not having nodes spread across failure domains

## Related Pages

- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
- [CockroachDB Gossip Error]({{< relref "/tools/cockroachdb/cockroach-gossip-error" >}}) -- gossip issues
