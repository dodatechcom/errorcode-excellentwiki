---
title: "[Solution] ScyllaDB Node Decommission Error — How to Fix"
description: "Fix ScyllaDB node decommission errors when a node cannot gracefully leave the cluster"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Node Decommission Error

Node decommission errors occur when a ScyllaDB node fails to transfer its data to other nodes before leaving the cluster.

## Why It Happens

- Other nodes are too busy to accept streaming data
- Network bandwidth is insufficient for data transfer
- Node has too much data for the decommission timeout
- Target nodes have insufficient disk space
- Streaming session was interrupted by network failure

## Common Error Messages

```
error: decommission failed: unable to stream data to other nodes
```

```
Decommission: streaming failed after 10 minutes
```

```
error: node decommission interrupted, node is in an inconsistent state
```

## How to Fix It

### 1. Check Node Status Before Decommission

```bash
nodetool status
nodetool info
```

### 2. Reduce Streaming Throughput

```bash
nodetool setstreamthroughput -t 100
```

### 3. Retry Decommission

```bash
# If decommission fails, check node state
nodetool status
# If node is partially decommissioned, use removenode
nodetool removenode <host-id>
```

### 4. Free Space on Target Nodes

```bash
# Ensure target nodes have enough space
ssh node2 "df -h /var/lib/scylla/data"
```

## Examples

```
$ nodetool decommission
[2024-01-15 10:30:00] Starting decommission
[2024-01-15 10:35:00] Streaming data to node1: 50% complete
[2024-01-15 10:40:00] Decommission completed successfully
```

## Prevent It

- Ensure all nodes are healthy before decommission
- Schedule decommission during low-traffic periods
- Monitor streaming progress during decommission

## Related Pages

- [ScyllaDB Node Decommission Error](/tools/scylladb/scylladb-node-decommission-error)
- [ScyllaDB Decommission Failed](/tools/scylladb/scylladb-decommission-failed)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
