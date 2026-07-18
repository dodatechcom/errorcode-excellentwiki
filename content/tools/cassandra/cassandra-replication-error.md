---
title: "[Solution] Cassandra Replication Error — How to Fix"
description: "Fix Cassandra replication errors by resolving replica placement issues, tuning replication factor, recovering from node failures, and correcting datacenter topology."
tools: ["cassandra"]
error-types: ["replication-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra replication error occurs when the replication subsystem cannot maintain the expected number of copies for a given keyspace. Replication is foundational to Cassandra's availability model, and failures here affect durability and fault tolerance.

## Why It Happens

Cassandra replicates data across nodes according to the replication strategy defined in each keyspace. Errors arise when the actual replica placement cannot match the configured replication factor.

- The replication factor exceeds the number of live nodes in a datacenter
- Node failures reduce available replicas below the required count
- Token ranges are unevenly distributed, causing some partitions to have fewer replicas
- Network partitions prevent replicas from staying synchronized
- Nodes are added or removed without proper bootstrap or decommission procedures
- NetworkTopologyStrategy is misconfigured with incorrect datacenter names
- Gossip protocol reports stale node status, causing incorrect replica placement decisions

## Common Error Messages

```text
UnavailableException: Not enough replicas for CONSISTENCY LEVEL LOCAL_QUORUM at consistency LOCAL_QUORUM (3 required but only 2 alive)
```

The replication factor is 3 but only 2 replicas are alive for some token ranges. Consistency cannot be achieved.

```text
ReadTimeoutException: Block for LOCAL_QUORUM was not timely, but 1 response(s) were received
```

Replica responses are delayed because some replicas are on unhealthy nodes or across slow network links.

```text
WriteTimeoutException: Timed out waiting for replica responses — only 1 of 3 replicas acknowledged
```

Two replicas failed to acknowledge the write. The replication factor may exceed available capacity.

```text
InvalidRequestException: Unable to fulfill replication strategy because insufficient nodes are available
```

There are not enough nodes to satisfy the replication factor. This happens during cluster scaling operations.

## How to Fix It

### 1. Verify Replication Factor Matches Available Nodes

```cql
-- Check replication settings for all keyspaces
DESCRIBE KEYSPACE my_keyspace;

-- Example output:
-- CREATE KEYSPACE my_keyspace WITH replication = {
--     'class': 'NetworkTopologyStrategy',
--     'dc1': 3,
--     'dc2': 3
-- };

-- Check how many nodes are in each datacenter
SELECT datacenter, count(*) as node_count
FROM system.local;

-- If RF is 3 but dc1 only has 2 nodes, reduce it
ALTER KEYSPACE my_keyspace WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'dc1': 2,
    'dc2': 3
};
```

### 2. Recover Failed Nodes

```bash
# Check node status
nodetool status

# Restart a downed node
sudo systemctl start cassandra

# If the node is permanently lost, replace it
# 1. Decommission the old node (if possible)
nodetool decommission

# 2. Add a replacement node with the same rack and datacenter
# Start the new node with -Dcassandra.rack=rack1 -Dcassandra.dc=dc1

# 3. Run repair to rebuild missing replicas
nodetool repair -pr my_keyspace my_table
```

### 3. Fix Token Distribution

```bash
# Check token ownership per node
nodetool ring

# Look for uneven distribution:
# Node 1: 10.0.1.1  owns 256 tokens  owns 40% of data
# Node 2: 10.0.1.2  owns 256 tokens  owns 35% of data
# Node 3: 10.0.1.3  owns 256 tokens  owns 25% of data

# Use vnodes (virtual nodes) for automatic balance
# In cassandra.yaml:
num_tokens: 16  # or use allocate_tokens_for_local_replication_factor
```

```bash
# If using vnodes, trigger automatic rebalancing
nodetool cleanup my_keyspace

# For very uneven distributions, bootstrap a new node
# This will steal tokens from existing nodes
```

### 4. Fix Datacenter Topology

```yaml
# cassandra.yaml — ensure correct datacenter and rack names
# Node in datacenter 1:
cassandra	dc1
rack	rack1

# Node in datacenter 2:
cassandra	dc2
rack	rack1
```

```bash
# Verify topology with nodetool
nodetool status

# Check gossip for datacenter information
nodetool gossipinfo
```

```cql
-- Ensure NetworkTopologyStrategy datacenter names match actual node topology
ALTER KEYSPACE my_keyspace WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'dc1': 3
};
-- The 'dc1' here must match the dc reported by nodetool status
```

### 5. Run Anti-Entropy Repair

```bash
# Full repair of all tables in a keyspace
nodetool repair -pr my_keyspace

# Repair specific table
nodetool repair -pr my_keyspace my_table

# Parallel repair for faster execution
nodetool repair -pr --full my_keyspace
```

Repair ensures all replicas have the same data. Run repair at least once per GC grace seconds period (default 10 days).

## Common Scenarios

**Replication factor mismatch after adding a new datacenter.** When adding dc2, ensure the RF for dc2 is set to at least 1 in all keyspaces. Otherwise, data written to dc1 will not replicate to dc2. Run `nodetool rebuild dc2` to stream existing data to the new DC.

**Replica count drops during rolling restart.** Each node restart temporarily removes its replicas. If the RF is 3 and you restart nodes one at a time, you briefly have RF=2. Perform restarts quickly and verify each node is UN before restarting the next.

**Datacenter name typo causes replication failure.** If the datacenter name in cassandra.yaml (`dc1`) does not match the keyspace replication config (`dc1` vs `DC1`), replication silently fails. Cassandra datacenter names are case-sensitive.

## Prevent It

- Always maintain at least RF+1 nodes per datacenter and monitor node count with alerts when it drops below threshold
- Use NetworkTopologyStrategy for all production keyspaces to ensure proper multi-datacenter replication
- Schedule regular anti-entropy repairs with Reaper to catch and fix replica inconsistencies before they cause availability issues
