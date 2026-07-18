---
title: "[Solution] CockroachDB Snapshot Error - Fix Snapshot Transfer Failed"
description: "Fix CockroachDB snapshot transfer failures. Resolve snapshot streaming, range replication, and snapshot-related errors."
tools: ["cockroachdb"]
error-types: ["snapshot-error"]
severities: ["error"]
weight: 5
---

This error means a Raft snapshot transfer between nodes failed. Snapshots are used to bring new replicas up to date and are critical for range replication.

## What This Error Means

When snapshot transfers fail, you see:

```
ERROR: snapshot failed: snapshot sending failed
# or
ERROR: raft: snapshot fails during replication
# or
snapshot not accepted: store is draining
```

Snapshots transfer the full state of a range to a new replica. Failed snapshots prevent ranges from being replicated to new nodes.

## Why It Happens

- The target node is too busy to accept snapshots
- Network bandwidth between nodes is insufficient
- The snapshot is too large for available disk space
- The sending node is under heavy load
- Store rebalancing is disabled
- The snapshot queue is full

## How to Fix It

### Check snapshot status

```sql
SELECT * FROM crdb_internal.ranges
WHERE lease_holder = node_id
AND range_size > 5000000000;
```

Large ranges take longer to snapshot.

### Increase snapshot throughput

```sql
SHOW CLUSTER SETTING server.sending.recovery.snapshot_rate;
```

Increase the rate to speed up transfers.

### Monitor snapshot queue

```sql
SELECT * FROM crdb_internal.node_metrics
WHERE name LIKE '%snapshot%';
```

### Check disk space on target

```bash
df -h /var/lib/cockroach/
```

Snapshots need temporary disk space on the target node.

### Add capacity to the cluster

```bash
cockroach start --join=node1:26257 --insecure --store=path=/new/disk/cockroach
```

Adding nodes distributes the snapshot load.

### Rebalance ranges manually

```sql
ALTER TABLE my_table RELOCATE TO node_id;
```

### Monitor snapshot transfers

```bash
curl http://localhost:8080/_status/raft
```

Check the Raft status for snapshot activity.

### Increase store capacity

```sql
SHOW CLUSTER SETTING server.store_capacity.disabled;
```

Ensure store capacity checks are enabled.

### Check for slow stores

```sql
SELECT store_id, capacity, available
FROM crdb_internal.kv_store_status;
```

### Use replication zones for large tables

```sql
ALTER RANGE CONFIGURE ZONE USING num_replicas = 3;
```

## Common Mistakes

- Not monitoring snapshot queue depth
- Assuming snapshots are instantaneous for large ranges
- Not having sufficient network bandwidth between nodes
- Running nodes with insufficient disk space for snapshot staging
- Not checking store health before adding new nodes

## Related Pages

- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
- [CockroachDB Range Split]({{< relref "/tools/cockroachdb/cockroach-range-split" >}}) -- range issues
