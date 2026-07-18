---
title: "[Solution] ScyllaDB Node Error — How to Fix"
description: "Fix ScyllaDB node errors by recovering from node failures, resolving gossip issues, and rejoining nodes to the cluster"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Node Error

ScyllaDB node errors occur when a node in the cluster goes down, becomes unreachable, or fails to join the cluster. Node health is critical for cluster availability.

## Why It Happens

- ScyllaDB process crashed or was OOM killed
- Node cannot communicate with other nodes (gossip failure)
- Node runs out of disk space and stops accepting writes
- Clock skew causes node to be marked down
- Network partition isolates the node
- Configuration error prevents startup

## Common Error Messages

```
NodeDown: Node 10.0.0.2 is down
```

```
GossiperTimeout: Cannot reach node 10.0.0.2
```

```
UnavailabilityError: Not enough live nodes to satisfy consistency
```

```
BootstrapFailure: Failed to join cluster
```

## How to Fix It

### 1. Check Node Status

```bash
# Check cluster status
nodetool status

# UN = Up/Normal, DN = Down/Normal, UL = Up/Leaving
# DL = Down/Leaving, UJ = Up/Joining, DJ = Down/Joining

# Check node information
nodetool info

# Check gossip status
nodetool gossipinfo
```

### 2. Recover Down Node

```bash
# Check if ScyllaDB process is running
sudo systemctl status scylla-server

# Restart ScyllaDB
sudo systemctl restart scylla-server

# Check logs for crash reason
sudo journalctl -u scylla-server -n 200 --no-pager

# Check for OOM kills
dmesg | grep -i oom
```

### 3. Remove Dead Node from Cluster

```bash
# Decommission a dead node (run on live node)
nodetool removenode <host-id>

# Get the host ID
nodetool status | grep DN

# After removing, run repair to rebalance
nodetool repair mykeyspace
```

### 4. Bootstrap New Node

```bash
# Start new node with correct configuration
# In scylla.yaml:
# listen_address: 10.0.0.4
# rpc_address: 0.0.0.0
# seeds: "10.0.0.1,10.0.0.2"

# Start ScyllaDB
sudo systemctl start scylla-server

# Monitor bootstrap progress
watch -n 5 'nodetool status'

# Check streaming progress
nodetool netstats
```

## Common Scenarios

- **Node keeps restarting**: Check logs for configuration errors or disk issues.
- **New node won't join**: Verify seeds, listen_address, and network connectivity.
- **Cluster reports node down but node is up**: Check firewall rules for gossip ports.

## Prevent It

- Use systemd to auto-restart ScyllaDB on failure
- Monitor node health with `nodetool status` and Prometheus
- Keep at least 3 nodes for proper redundancy

## Related Pages

- [ScyllaDB Gossip Error](/tools/scylladb/scylladb-gossip-error)
- [ScyllaDB Replication Error](/tools/scylladb/scylladb-replication-error)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
