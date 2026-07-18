---
title: "[Solution] Cassandra Unavailable Error — How to Fix"
description: "Fix Cassandra unavailable errors by restoring replica availability, adjusting consistency levels, recovering dead nodes, and validating datacenter topology."
tools: ["cassandra"]
error-types: ["unavailable-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra unavailable error means the coordinator determined immediately that it cannot satisfy the request because not enough replicas are alive. Unlike a timeout, no attempt was made — the cluster knows upfront that the consistency level cannot be met.

## Why It Happens

The unavailable error is a fast-fail mechanism. Cassandra checks replica status before sending the request, and if the required number of replicas is not alive, it rejects the operation immediately.

- Nodes have been decommissioned or have crashed and are not replaced
- Network partitions isolate the coordinator from some replicas
- The replication factor is higher than the number of live nodes in the datacenter
- Nodes are in the process of bootstrapping and not yet serving traffic
- Gossip protocol has not converged and some nodes appear down to the coordinator
- The datacenter placement strategy does not match the actual node topology
- JMX or gossip failures cause nodes to be marked as down incorrectly

## Common Error Messages

```text
UnavailableException: Not enough replicas available for consistency level LOCAL_QUORUM at consistency LOCAL_QUORUM (2 required but only 1 alive)
```

The cluster needs two replicas but only one is available. This is the most common unavailable error.

```text
UnavailableException: Cannot achieve consistency level LOCAL_QUORUM because only 1 of 3 replicas are alive
```

The cluster explicitly states the replica count is insufficient for the consistency level.

```text
UnavailableException: Not enough replicas available for consistency level EACH_QUORUM at consistency EACH_QUORUM
```

Each datacenter must independently satisfy the consistency level. If any DC falls below the quorum threshold, the entire request fails.

```text
ReadTimeoutException: Not enough replicas responded (0 of 3) at consistency LOCAL_ONE
```

Even LOCAL_ONE cannot be satisfied. All replicas for the queried token range are down.

## How to Fix It

### 1. Check Node Status and Recover Dead Nodes

```bash
# View cluster status
nodetool status

# Look for DN (Down/Normal) or DN with UN (Up/Normal) transitions
# Example output:
# Datacenter: dc1
# ===============
# Status=Up/Down
# |/ State=Normal/Leaving/Joining/Moving
# --  Address    Load       Tokens  Owns (effective)  Host ID    Rack
# UN  10.0.1.1   256 GB     256     33.3%             abc-123    rack1
# DN  10.0.1.2   200 GB     256     33.3%             def-456    rack1
# UN  10.0.1.3   270 GB     256     33.3%             ghi-789    rack1
```

```bash
# Restart a downed node
sudo systemctl start cassandra

# If the node won't start, check logs
tail -100 /var/log/cassandra/system.log | grep -i "error\|exception"
```

### 2. Lower Consistency Level to Match Available Replicas

```java
// If only 1 replica is alive, use LOCAL_ONE
session.execute(
    SimpleStatement.builder("SELECT * FROM users WHERE id = ?")
        .addPositionalValue(userId)
        .setConsistencyLevel(ConsistencyLevel.LOCAL_ONE)
        .build()
);
```

```cql
-- Check current consistency and lower it
CONSISTENCY LOCAL_ONE;
SELECT * FROM users WHERE id = 12345;
```

### 3. Add Nodes to Meet Replication Requirements

```bash
# Bootstrap a new node
cockroach node init --insecure --host=10.0.1.4

# Or in Cassandra specifically:
# Start the new node with the same cluster name
cassandra -Dcassandra.cluster_name=my_cluster
```

```cql
-- Verify replication factor
DESCRIBE KEYSPACE my_keyspace;

-- If RF is 3 but only 2 nodes exist, temporarily reduce it
ALTER KEYSPACE my_keyspace WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'dc1': 2
};
```

### 4. Fix Gossip and Node Communication

```bash
# Reset gossip if nodes cannot see each other
nodetool resetossip

# Force a full cluster restart in order (seed nodes first)
# On each node, in order:
nodetool drain
sudo systemctl stop cassandra
sudo systemctl start cassandra

# Verify gossip state
nodetool gossipinfo
```

Ensure all nodes can communicate on port 7000 (or 7001 for TLS). Check that ` seeds ` in cassandra.yaml includes at least two reachable nodes.

## Common Scenarios

**Unavailable after a rolling restart.** If a node is restarted while others are still coming up, the cluster may not have enough replicas. Perform rolling restarts with sufficient wait time between nodes. Verify each node is `UN` before restarting the next.

**Unavailable on only one datacenter.** In a multi-DC setup, EACH_QUORUM requires every DC to meet quorum. If one DC has fewer nodes than the RF, it will always fail. Either reduce RF in that DC or add nodes.

**Unavailable after a network split.** After a split heals, nodes may not have the latest gossip state. Restart the gossip protocol with `nodetool resetgossip` or perform a full cluster restart starting with seed nodes.

## Prevent It

- Maintain at least 2n+1 nodes per datacenter where n is the desired replication factor, and monitor node count with automated alerts
- Use rack-aware placement across availability zones so that losing one AZ does not reduce replica count below quorum
- Configure node health checks in your orchestration layer to automatically replace failed nodes within 15 minutes
