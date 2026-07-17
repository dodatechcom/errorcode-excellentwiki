---
title: "[Solution] CockroachDB Replication Error - Fix Under-Replicated Ranges"
description: "Fix CockroachDB range under-replicated errors by adding new cluster nodes to provide capacity, rebalancing data ranges, and verifying the replication factor"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB replication error occurs when ranges have fewer replicas than the configured replication factor. The cluster reports ranges as under-replicated, which means data durability is at risk if a node fails.

## What This Error Means

CockroachDB automatically replicates data across nodes using the replication factor (default 3). When a node goes down or data cannot be replicated, ranges become under-replicated. The error appears in `SHOW RANGES`, `crdb_internal.ranges`, or as warnings in the admin UI.

Under-replicated ranges indicate that the cluster does not have enough copies of some data to survive an additional node failure. CockroachDB will automatically rebalance when a new node joins, but until then, the data is at risk.

## Why It Happens

- A node went down and ranges cannot be fully replicated
- Cluster has fewer nodes than the replication factor
- Network partition preventing replica creation on remote nodes
- Disk space exhaustion preventing replica writes
- Decommissioning a node without adding a replacement
- Hotspot ranges that cannot be split further

## How to Fix It

### 1. Check Under-Replicated Ranges

```sql
SELECT range_id, array_length(replicas, 1) AS replica_count
FROM crdb_internal.ranges
WHERE array_length(replicas, 1) < 3
ORDER BY replica_count;
```

### 2. Add a New Node to the Cluster

```bash
cockroach start \
  --join=10.0.1.5:26257,10.0.1.6:26257 \
  --host=0.0.0.0 \
  --store=path=/var/lib/cockroach/data \
  --insecure
```

### 3. Verify Replication Factor

```sql
SHOW ZONE CONFIGURATION FOR DATABASE mydb;
-- Default is 3 replicas
```

### 4. Check Node Status

```bash
cockroach node status --host=localhost:26257 --insecure
# Ensure all expected nodes show LIVE
```

### 5. Monitor Rebalancing

```sql
-- Check if ranges are being rebalanced
SELECT range_id, replicas, lease_holder
FROM crdb_internal.ranges
WHERE array_length(replicas, 1) < 3;
```

### 6. Fix Zone Configuration

```sql
-- Ensure replication factor matches cluster size
ALTER DATABASE mydb CONFIGURE ZONE USING num_replicas = 3;
```

### 7. Decommission Safely

```bash
# Before removing a node, ensure enough replicas exist
cockroach node decommission <node-id> \
  --host=localhost:26257 \
  --insecure \
  --wait=all
```

## Common Mistakes

- Decommissioning a node in a 3-node cluster with replication factor 3 (no fault tolerance)
- Not monitoring `crdb_internal.ranges` for under-replicated ranges after node failures
- Assuming CockroachDB will automatically add nodes (it only rebalances, not adds)
- Setting replication factor higher than the number of available nodes

## Related Pages

- [CockroachDB Node Unavailable](/tools/cockroachdb/cockroach-node-unavailable)
- [CockroachDB Certificate Error](/tools/cockroachdb/cockroach-certificate-error)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
