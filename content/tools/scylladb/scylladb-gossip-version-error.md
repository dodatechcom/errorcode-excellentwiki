---
title: "[Solution] ScyllaDB Gossip Version Mismatch Error — How to Fix"
description: "Fix ScyllaDB gossip version mismatch errors when nodes running different versions cannot communicate"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Gossip Version Mismatch Error

Gossip version mismatch errors occur when ScyllaDB nodes running incompatible versions cannot exchange gossip protocol messages, preventing cluster operation.

## Why It Happens

- Mixed-version cluster after a partial upgrade
- New node joined with an older ScyllaDB version
- Gossip generation number conflicts between versions
- Feature flag differences prevent protocol handshake
- Rolling upgrade was interrupted before completion

## Common Error Messages

```
Gossip: version mismatch with peer node2: expected 9, got 8
```

```
ERROR: Unable to gossip with node3: protocol version incompatible
```

```
gossip: feature check failed for node4: missing required features
```

## How to Fix It

### 1. Check Cluster Versions

```bash
nodetool describecluster
nodetool status
```

### 2. Complete the Upgrade

```bash
# Upgrade remaining nodes to matching version
sudo apt-get update && sudo apt-get install scylla
sudo systemctl restart scylla-server
```

### 3. Downgrade if Needed

```bash
# Stop the incompatible node
sudo systemctl stop scylla-server

# Install matching version
sudo apt-get install scylla=4.6.0-0.20230101.abc12345678
sudo systemctl start scylla-server
```

### 4. Force Gossip Protocol Version

```yaml
# In scylla.yaml (advanced, use with caution)
force_gossip_generation: 1
```

## Examples

```
$ nodetool describecluster
Cluster Name: my_cluster
Partitioner: org.apache.cassandra.dht.Murmur3Partitioner
Snitch: org.apache.cassandra.locator.DynamicEndpointSnitch

Node1: 5.2.0
Node2: 5.2.0
Node3: 4.6.0 -- version mismatch
```

## Prevent It

- Use Scylla Manager for rolling upgrades
- Verify all nodes run compatible versions before joining
- Monitor cluster version consistency

## Related Pages

- [ScyllaDB Gossip Error](/tools/scylladb/scylladb-gossip-error)
- [ScyllaDB Gossiper Error](/tools/scylladb/scylladb-gossiper-error)
- [ScyllaDB Schema Version Mismatch](/tools/scylladb/scylladb-schema-version-mismatch)
