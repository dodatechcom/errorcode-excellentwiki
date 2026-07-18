---
title: "[Solution] CockroachDB Node Error — How to Fix"
description: "Fix CockroachDB node failure errors by recovering crashed nodes, decommissioning failed nodes, rebalancing ranges, and restoring cluster health."
tools: ["cockroachdb"]
error-types: ["node-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB node error occurs when a node in the cluster becomes unavailable, fails to respond to requests, or enters an unhealthy state. Node failures are expected in distributed systems, but the cluster must handle them gracefully to maintain availability.

## Why It Happens

CockroachDB nodes can fail for many reasons, from simple process crashes to hardware failures. The cluster automatically rebalances data away from failed nodes, but the failure itself can trigger errors during the transition.

- The node process crashed due to OOM, panic, or unhandled error
- The node's disk is full and cannot accept new writes
- Network partitions isolate the node from the rest of the cluster
- The node is being decommissioned and data is being moved
- Clock skew between nodes causes Raft leader elections to fail
- The node's CPU is exhausted and it cannot respond to heartbeats
- The node is stuck in a restart loop due to corrupted data
- A hardware failure (disk, NIC, memory) makes the node unresponsive

## Common Error Messages

```text
ERROR: node unavailable: node <node_id> is not responding to heartbeats
```

A node has stopped responding to cluster heartbeats. It may be crashed or partitioned.

```text
ERROR: range unavailable: could not find range descriptor for range <range_id>
```

The range's replicas are all on failed nodes. The range is temporarily unavailable.

```text
ERROR: node <node_id> has been decommissioned
```

The node was decommissioned and can no longer serve traffic.

```text
ERROR: connection refused to node <node_id> at <address>:26257
```

The node is not accepting connections on the SQL port.

## How to Fix It

### 1. Check Node Status

```bash
# Check all nodes in the cluster
cockroach node status --host=localhost:26257 --insecure

# Look for nodes with status "false" (unavailable)
# id | address  | build  | started_at            | ... | is_live
# 1  | 10.0.1.1 | v23.1  | 2024-01-15 10:00:00   | ... | true
# 2  | 10.0.1.2 | v23.1  | 2024-01-15 10:00:00   | ... | false
# 3  | 10.0.1.3 | v23.1  | 2024-01-15 10:00:00   | ... | true
```

### 2. Recover a Crashed Node

```bash
# Check if the process is running
ps aux | grep cockroach

# Check the logs for the crash reason
tail -200 /var/log/cockroachdb/cockroach.log | grep -i "error\|panic\|fatal"

# If OOM killed, check memory usage
free -h

# Restart the node
sudo systemctl start cockroachdb

# Verify the node rejoined the cluster
cockroach node status --host=localhost:26257 --insecure
```

### 3. Fix Disk Full Issues

```bash
# Check disk usage
df -h /var/lib/cockroach

# Find large files
du -sh /var/lib/cockroach/* | sort -rh | head -10

# Remove old log files
sudo find /var/log/cockroachdb -name "*.log" -mtime +7 -delete

# If using a separate data directory, expand the disk
# or move the store to a larger disk
```

```sql
-- Check store status from SQL
SELECT store_id, range_count, live_bytes, used_bytes 
FROM crdb_internal.ranges_no_leases;
```

### 4. Decommission a Permanently Failed Node

```bash
# Decommission the failed node (requires the node to be reachable)
cockroach node decommission <node_id> --host=localhost:26257 --insecure

# If the node is not reachable, force decommission
cockroach node decommission --host=localhost:26257 --insecure --self

# Verify decommission completed
cockroach node status --host=localhost:26257 --insecure
```

```sql
-- Check decommission status
SELECT node_id, address, draining, decommissioning, is_live
FROM crdb_internal.gossip_nodes;
```

### 5. Add a Replacement Node

```bash
# Start a new node with the same data directory
cockroach start \
  --insecure \
  --listen-addr=0.0.0.0:26257 \
  --http-addr=0.0.0.0:8080 \
  --join=10.0.1.1:26257,10.0.1.3:26257 \
  --store=path=/var/lib/cockroach/data \
  --attrs=dc1

# The new node will automatically receive ranges from the cluster
# Monitor range rebalancing
cockroach node status --host=localhost:26257 --insecure
```

### 6. Fix Clock Skew

```bash
# Check clock synchronization
sudo chronyc tracking

# Ensure NTP is running
sudo systemctl status chrony

# CockroachDB requires clocks to be within 500ms of each other
# If skew is too high, the node may be rejected by the cluster
```

## Common Scenarios

**Single-node cluster crashes.** A single-node cluster loses all data availability when the node goes down. Use at least 3 nodes for production to survive a single node failure.

**Node fails during rolling upgrade.** If a node crashes during upgrade, the remaining nodes handle the traffic. Wait for the node to recover and complete the upgrade, then proceed to the next node.

**Node stuck in decommissioning state.** A node that cannot reach the cluster may be stuck decommissioning. Force decommission with `cockroach node decommission --force` from a healthy node.

## Prevent It

- Use at least 3 nodes in production to survive single-node failures without data unavailability
- Monitor node health with CockroachDB's Prometheus metrics and alert when a node becomes unavailable
- Use hardware RAID and redundant power supplies to reduce the impact of individual hardware failures
