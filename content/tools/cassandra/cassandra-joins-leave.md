---
title: "[Solution] Cassandra Joins Leave Error - Fix Node Failed to Join or Leave Cluster"
description: "Fix Cassandra node join and leave failures. Resolve bootstrap, decommission, and cluster membership issues during scaling."
tools: ["cassandra"]
error-types: ["joins-leave"]
severities: ["error"]
weight: 5
---

This error means a Cassandra node failed to join or leave the cluster during scaling operations. Bootstrap and decommission processes are sensitive to cluster health.

## What This Error Means

When a node join or leave fails, you see:

```
BootstrapFailedException: Bootstrap failed
# or
IllegalStateException: Cannot decommission node while other nodes are bootstrapping
# or
NoHostAvailableException: Unable to contact any seeds
```

Adding or removing nodes requires careful coordination. Failures can leave the cluster in an inconsistent state.

## Why It Happens

- The node cannot contact seed nodes during bootstrap
- Another node is already bootstrapping (only one at a time allowed)
- The cluster does not have enough capacity to stream data to the new node
- A decommission is attempted while other nodes are down
- The node is not properly configured with the correct cluster name
- Network bandwidth is insufficient for data streaming

## How to Fix It

### Check cluster status before adding nodes

```bash
nodetool status
```

All existing nodes must be Up and Normal before adding a new node.

### Bootstrap a new node

```bash
# Start the new node with the same cluster_name
# It will automatically bootstrap and stream data
sudo systemctl start cassandra
nodetool status
```

### Monitor bootstrap progress

```bash
nodetool netstats
```

This shows streaming progress between nodes.

### Decommission a node properly

```bash
nodetool decommission
```

Only decommission nodes that are Up and Normal. Never decommission the last node.

### Handle failed bootstrap

```bash
# If bootstrap fails, reset the node
sudo systemctl stop cassandra
rm -rf /var/lib/cassandra/data/*
rm -rf /var/lib/cassandra/commitlog/*
rm -rf /var/lib/cassandra/saved_caches/*
sudo systemctl start cassandra
```

### Check cluster configuration

```yaml
# cassandra.yaml
cluster_name: 'my-cluster'
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
      - seeds: "10.0.0.1,10.0.0.2"
```

All nodes must have the same cluster name and seed list.

### Add one node at a time

```bash
# Wait for node 1 to finish streaming
nodetool status
# Then add node 2
```

Never bootstrap multiple nodes simultaneously.

### Increase streaming throughput

```yaml
# cassandra.yaml
stream_throughput_outbound_megabits_per_sec: 200
inter_dc_stream_throughput_outbound_megabits_per_sec: 200
```

### Handle decommission with nodes down

```bash
# Bring the down node back up first
sudo systemctl start cassandra
nodetool status
# Then decommission
nodetool decommission
```

## Common Mistakes

- Adding multiple nodes simultaneously, which only one bootstrap can happen at a time
- Decommissioning a node while other nodes are down
- Not monitoring bootstrap progress and assuming it will complete quickly
- Forgetting to update the seed list when adding new nodes
- Not having sufficient network bandwidth for data streaming

## Related Pages

- [Cassandra Gossip Error]({{< relref "/tools/cassandra/cassandra-gossip-error" >}}) -- gossip issues
- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- availability issues
- [Cassandra Nodetool Error]({{< relref "/tools/cassandra/cassandra-nodetool-error" >}}) -- management tool issues
