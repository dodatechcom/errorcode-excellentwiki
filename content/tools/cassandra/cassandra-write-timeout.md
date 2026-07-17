---
title: "[Solution] Cassandra WriteTimeoutException - Fix Consistency Level"
description: "Fix Cassandra WriteTimeoutException by tuning consistency levels like QUORUM and LOCAL_QUORUM, increasing replication factor, and monitoring cluster health"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra `WriteTimeoutException` occurs when a write operation does not complete within the specified timeout period. The coordinator node received the write request but could not confirm that the required number of replicas acknowledged the write.

## What This Error Means

Cassandra uses a tunable consistency model. When you issue a write with a given consistency level (e.g., `QUORUM`, `ALL`), the coordinator must wait for that many replicas to respond. If they do not respond within the configured timeout, the driver throws a `WriteTimeoutException`.

The exception message typically includes the write type (e.g., `SIMPLE`, `BATCH`, `COUNTER`, `UNLOGGED_BATCH`), the consistency level requested, and the number of replicas that responded versus what was needed.

## Why It Happens

- Replica nodes are overloaded or experiencing disk I/O bottlenecks
- Network latency between the coordinator and replica nodes
- Consistency level is set too high for the current replication factor
- The `write_request_timeout_in_ms` in `cassandra.yaml` is too low
- Node failure or network partition reducing available replicas
- Commit log sync is slowing writes (e.g., `commitlog_sync: periodic` with long interval)
- Large batch statements overwhelming replicas

## How to Fix It

### 1. Lower the Consistency Level

```java
// Instead of ALL or QUORUM, use LOCAL_QUORUM or ONE for non-critical writes
ResultSet rs = session.execute(
    QueryBuilder.insertInto("my_table")
        .value("id", UUID.randomUUID())
        .value("data", "hello")
        .consistencyLevel(ConsistencyLevel.LOCAL_QUORUM)
);
```

### 2. Increase the Timeout

```yaml
# cassandra.yaml
write_request_timeout_in_ms: 5000
```

### 3. Increase Replication Factor

```sql
ALTER KEYSPACE my_keyspace
  WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'datacenter1': 3
  };
```

### 4. Monitor Node Health

```bash
nodetool status
nodetool tpstats
```

### 5. Reduce Batch Size

```java
// Use unlogged batches for unrelated inserts
BatchStatement batch = new BatchStatement(BatchStatement.Type.UNLOGGED);
for (MyEntity entity : entities) {
    batch.add(insertStatement.bind(entity));
}
session.execute(batch);
```

## Common Mistakes

- Using `ConsistencyLevel.ALL` with a replication factor of 3 in a multi-node cluster without accounting for failover
- Forgetting that `LOCAL_QUORUM` requires a quorum within the local datacenter only
- Not monitoring `nodetool tpstats` for pending writes or dropped messages
- Setting timeouts too low without checking disk and network baselines first

## Related Pages

- [Cassandra ReadTimeoutException](/tools/cassandra/cassandra-read-timeout)
- [Cassandra Unavailable Exception](/tools/cassandra/cassandra-unavailable)
- [Cassandra Lightweight Transaction Error](/tools/cassandra/cassandra-lwt-error)
- [Cassandra Compaction Error](/tools/cassandra/cassandra-compaction-error)
