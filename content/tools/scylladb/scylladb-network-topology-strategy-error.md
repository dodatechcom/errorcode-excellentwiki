---
title: "[Solution] ScyllaDB Network Topology Strategy Error — How to Fix"
description: "Fix ScyllaDB NetworkTopologyStrategy errors when replication across data centers fails or is misconfigured"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Network Topology Strategy Error

NetworkTopologyStrategy errors occur when ScyllaDB cannot satisfy replication requirements across multiple data centers due to insufficient nodes or configuration issues.

## Why It Happens

- Not enough nodes in a data center to meet replication factor
- Data center names in keyspace definition do not match actual DC names
- Network partition isolates a data center
- Gossip has not propagated DC information to all nodes
- Rack topology is incorrectly configured

## Common Error Messages

```
Not enough nodes for replication strategy
```

```
UnreplicatedKeyspaceException: replication factor 3 for DC dc2 but only 1 node
```

```
error: keyspace mykeyspace has no replicas in datacenter us-east-2
```

## How to Fix It

### 1. Verify Data Center Configuration

```bash
nodetool status
nodetool describecluster | grep "Datacenter"
```

### 2. Check Keyspace Replication

```cql
DESCRIBE KEYSPACE mykeyspace;
```

### 3. Fix DC Name Mismatch

```cql
-- If actual DC is "us-east-1" but keyspace says "dc1"
ALTER KEYSPACE mykeyspace WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'us-east-1': 3,
  'us-west-2': 3
};
```

### 4. Add Nodes to Undersized DC

```bash
# Start new node in the target DC
scylla --dc-name us-west-2 --rack-name rack1
```

## Examples

```
$ nodetool status
Datacenter: us-east-1
===============
Status=Up/Down
--  Address    DC
UN  10.0.0.1  us-east-1
UN  10.0.0.2  us-east-1
UN  10.0.0.3  us-east-1

Datacenter: us-west-2
===============
UN  10.1.0.1  us-west-2
-- insufficient nodes for RF=3
```

## Prevent It

- Always verify DC names match before creating keyspaces
- Ensure each DC has enough nodes for the replication factor
- Monitor node distribution across data centers

## Related Pages

- [ScyllaDB DC Error](/tools/scylladb/scylladb-dc-error)
- [ScyllaDB Replication Error](/tools/scylladb/scylladb-replication-error)
- [ScyllaDB Network Topology Error](/tools/scylladb/scylladb-network-topology-error)
