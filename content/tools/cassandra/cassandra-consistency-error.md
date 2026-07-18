---
title: "[Solution] Cassandra Consistency Error - Fix Consistency Level Not Met"
description: "Fix Cassandra consistency level not met errors. Resolve read and write consistency failures when replicas are unavailable."
tools: ["cassandra"]
error-types: ["consistency-error"]
severities: ["error"]
weight: 5
---

This error means Cassandra could not achieve the requested consistency level. Not enough replicas responded to satisfy the read or write consistency requirement.

## What This Error Means

When consistency level cannot be achieved, you see:

```
UnavailableException: Cannot achieve consistency level LOCAL_QUORUM
# or
WriteTimeoutException: Timed out achieving consistency level
# or
ReadTimeoutException: Timed out achieving consistency level ONE
```

Each consistency level requires a specific number of replicas to respond. When unavailable nodes reduce the replica count below the threshold, the operation fails.

## Why It Happens

- Too many nodes are down to satisfy the consistency level
- The replication factor is too low for the requested consistency
- Network partitions prevent the coordinator from reaching replicas
- The consistency level is set higher than the replication factor allows
- Data center awareness is not configured correctly

## How to Fix It

### Check replica count per consistency level

```bash
nodetool status
nodetool describe_cluster
```

Verify enough nodes are Up and Normal.

### Reduce consistency level for writes

```java
// Instead of LOCAL_QUORUM
session.execute(
    SimpleStatement.builder("INSERT INTO users (id, name) VALUES (?, ?)")
        .addPositionalValues(1, "Alice")
        .setConsistencyLevel(ConsistencyLevel.LOCAL_ONE)
        .build()
);
```

### Increase replication factor

```cql
ALTER KEYSPACE my_keyspace WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'dc1': 3,
  'dc2': 3
};
```

### Use LOCAL_QUORUM for multi-datacenter

```java
// LOCAL_QUORUM requires majority in local DC only
ConsistencyLevel.LOCAL_QUORUM
```

### Check for network partitions

```bash
nodetool tpstats | grep -i timeout
```

Timeouts may indicate network issues between nodes.

### Tune consistency for read vs write

```java
// Strong consistency: write with QUORUM, read with QUORUM
// Eventual consistency: write with ONE, read with ONE
```

### Use speculative retry for slow replicas

```yaml
# cassandra.yaml
speculative_retry: 99p
```

This retries on the next replica if the first does not respond.

### Verify data center configuration

```yaml
# cassandra-rackdc.properties
dc=dc1
rack=rack1
```

### Use tunable consistency per query

```java
// Different consistency for different operations
session.execute(writeStatement.setConsistencyLevel(ConsistencyLevel.QUORUM));
session.execute(readStatement.setConsistencyLevel(ConsistencyLevel.ONE));
```

## Common Mistakes

- Using QUORUM with a replication factor of 1
- Not accounting for node failures when choosing consistency levels
- Setting consistency too high for read-heavy workloads
- Forgetting that LOCAL_QUORUM is per-datacenter, not global
- Not monitoring consistency level failures as a cluster health indicator

## Related Pages

- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- replica unavailability
- [Cassandra Write Timeout]({{< relref "/tools/cassandra/cassandra-write-timeout" >}}) -- write timeouts
- [Cassandra Read Timeout]({{< relref "/tools/cassandra/cassandra-read-timeout" >}}) -- read timeouts
