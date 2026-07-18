---
title: "[Solution] ScyllaDB Gossip Error — How to Fix"
description: "Fix ScyllaDB gossip errors by resolving cluster membership failures, fixing endpoint state issues, and recovering from split-brain scenarios"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Gossip Error

ScyllaDB gossip errors occur when the gossip protocol fails to maintain cluster membership and node state information. Gossip is essential for cluster coordination.

## Why It Happens

- Gossip messages are blocked by firewall rules
- Node clock skew exceeds the allowed threshold
- Cluster has inconsistent seed node configuration
- Endpoint state is stale or corrupted
- Gossip stage is overwhelmed with too many nodes
- Network partition isolates nodes from each other

## Common Error Messages

```
GossipError: Gossip protocol failure
```

```
GossiperTimeout: Gossip to node 10.0.0.2 timed out
```

```
BootstrapFailure: Cannot bootstrap - existing cluster nodes unreachable
```

```
ClusterError: All seed nodes are down
```

## How to Fix It

### 1. Check Gossip Status

```bash
# View gossip information
nodetool gossipinfo

# Check cluster status
nodetool status

# Verify endpoint state
nodetool describecluster

# Check gossip stats
nodetool tpstats | grep -i gossip
```

### 2. Fix Seed Node Configuration

```yaml
# In scylla.yaml on ALL nodes, set identical seed list
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
      - seeds: "10.0.0.1,10.0.0.2,10.0.0.3"
```

```bash
# Restart all nodes one by one after seed config change
for node in 10.0.0.1 10.0.0.2 10.0.0.3; do
  ssh scylla@$node "sudo systemctl restart scylla-server"
  sleep 30
done
```

### 3. Fix Clock Synchronization

```bash
# Install and configure NTP
sudo apt install chrony
sudo systemctl enable chrony
sudo systemctl start chrony

# Check time sync status
chronyc tracking

# Ensure all nodes have synchronized clocks
for node in 10.0.0.1 10.0.0.2 10.0.0.3; do
  echo "Node $node time:"
  ssh scylla@$node "date"
done
```

### 4. Fix Firewall for Gossip

```bash
# Open gossip ports on all nodes
sudo ufw allow 7000/tcp    # Gossip
sudo ufw allow 7001/tcp    # SSL Gossip
sudo ufw allow 10000/tcp   # Scylla REST API
sudo ufw allow 9160/tcp    # Thrift
sudo ufw allow 9042/tcp    # CQL

# Verify gossip connectivity
for node in 10.0.0.2 10.0.0.3; do
  nc -zv $node 7000
done
```

## Common Scenarios

- **New node cannot join**: Verify seeds config matches on all nodes and gossip ports are open.
- **Cluster split after network partition**: Verify clocks are synchronized and network is restored.
- **Gossip overload with many nodes**: Increase gossip interval or reduce cluster size.

## Prevent It

- Keep seed node list consistent across all nodes
- Use NTP for clock synchronization on all nodes
- Monitor `nodetool gossipinfo` for stale endpoint states

## Related Pages

- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Cluster Error](/tools/scylladb/scylladb-cluster-error)
- [ScyllaDB Gossip Error](/tools/scylladb/scylladb-gossip-error)
