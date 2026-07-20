---
title: "[Solution] Redis CLUSTERDOWN Cluster Is Down"
description: "How to fix Redis CLUSTERDOWN error when the cluster is in a down state"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Cluster has unassigned slots due to node failure
- Too many master nodes are down
- Cluster state is `fail`
- Minimum number of nodes not met

## How to Fix

Check cluster state:

```bash
redis-cli CLUSTER INFO
```

Check node status:

```bash
redis-cli CLUSTER NODES
```

Bring failed nodes back online:

```bash
sudo systemctl start redis@7001
```

Reassign slots if node is permanently removed:

```bash
redis-cli CLUSTER FORGET <node-id>
```

Force cluster rebuild:

```bash
redis-cli --cluster fix <host>:<port>
```

## Examples

```bash
# Check cluster health
redis-cli CLUSTER INFO | grep cluster_state

# View all nodes
redis-cli CLUSTER NODES | grep -v connected

# Repair cluster
redis-cli --cluster fix 127.0.0.1:7001
```
