---
title: "[Solution] CockroachDB Node Unavailable - Fix Cluster Node Issues"
description: "Fix CockroachDB node unavailable errors by checking node process status, restarting the service, verifying inter-node gossip protocol, and resolving clock skew"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB node unavailable error occurs when a node in the cluster is not responding to SQL requests or internal gossip. The client may see `node is not connected` or `node unavailable` errors depending on which node the query routes to.

## What This Error Means

CockroachDB distributes data across nodes using ranges. When a node becomes unavailable, ranges hosted on that node become temporarily unreachable until the cluster detects the failure and rebalances. The error indicates that the specific node your query was routed to (or that hosts the needed range) is not communicating with the cluster.

In a multi-node cluster, this may not affect all queries, only those that need data from ranges on the unavailable node.

## Why It Happens

- The node process crashed or was killed
- Network partition between nodes
- Disk failure or disk full on the node
- Node is restarting after a maintenance operation
- Gossip protocol has not converged after node rejoin
- Kubernetes pod eviction or OOM kill
- Clock skew between nodes exceeding the threshold

## How to Fix It

### 1. Check Node Status

```bash
cockroach node status --host=localhost:26257 --insecure
# Look for LIVE status on all nodes
```

### 2. Restart the Node

```bash
# If using systemd
sudo systemctl restart cockroachdb

# If using Docker
docker restart cockroach-node-1

# If using Kubernetes
kubectl rollout restart statefulset cockroachdb -n mynamespace
```

### 3. Check Node Logs

```bash
# Find the logs directory
tail -f /var/lib/cockroach/logs/cockroach.log
```

### 4. Verify Network Connectivity Between Nodes

```bash
# From node 1, test connectivity to node 2
telnet 10.0.1.6 26257
nc -zv 10.0.1.6 26257
```

### 5. Decommission and Rejoin a Dead Node

```bash
# If a node is permanently dead, decommission it
cockroach node decommission <node-id> --host=localhost:26257 --insecure

# Then add a new node
cockroach start \
  --join=10.0.1.5:26257,10.0.1.6:26257 \
  --host=0.0.0.0 \
  --store=path=/var/lib/cockroach/data
```

### 6. Check Disk Space

```bash
df -h /var/lib/cockroach/data
# If full, clean up or expand the volume
```

### 7. Monitor Cluster Health

```sql
-- From a healthy node
SELECT node_id, address, is_live FROM crdb_internal.gossip_nodes;
```

## Common Mistakes

- Not decommissioning a permanently dead node, which prevents range rebalancing
- Restarting all nodes simultaneously during a rolling deployment
- Not monitoring disk usage and running out of space during compaction
- Ignoring clock skew in virtualized environments (NTP must be configured)

## Related Pages

- [CockroachDB Connection Refused](/tools/cockroachdb/cockroach-connection-refused)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
- [CockroachDB Replication Error](/tools/cockroachdb/cockroach-replication-error)
