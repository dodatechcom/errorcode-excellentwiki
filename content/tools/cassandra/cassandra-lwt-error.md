---
title: "[Solution] Cassandra Lightweight Transaction Failed - Fix LWT Errors"
description: "Fix Cassandra lightweight transaction failures by tuning Paxos timeouts, reducing hot partition key contention, using LOCAL_QUORUM, and implementing retries"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra lightweight transaction (LWT) error occurs when an `IF NOT EXISTS` or `IF EXISTS` condition fails or the underlying Paxos protocol cannot commit within the timeout. The error surfaces as `WriteTimeoutException` with `write_type: CAS` or `LWT_FAILURE`.

## What This Error Means

Lightweight transactions in Cassandra use the Paxos consensus protocol to provide compare-and-set semantics. When you execute `INSERT ... IF NOT EXISTS` or `UPDATE ... IF EXISTS`, Cassandra must:

1. Run a prepare phase across the quorum of replicas
2. Run a commit phase
3. Return the result (applied or not)

If this multi-round-trip process times out, the driver throws a `WriteTimeoutException` with the write type `CAS`. Unlike a normal write timeout, the actual write may or may not have been applied, leading to ambiguity.

## Why It Happens

- Paxos consensus requires 4 round trips instead of 1, making LWTs inherently slower
- High contention on the same partition key (multiple concurrent LWTs on the same row)
- Paxos timeout is too low for the network latency between replicas
- Replicas are overloaded and slow to respond during the prepare/commit phases
- Consistency level is set to `ALL` instead of `QUORUM` or `LOCAL_QUORUM`
- Using LWTs for high-throughput operations (LWTs are not designed for high contention)

## How to Fix It

### 1. Use LOCAL_QUORUM for LWTs

```java
// Always use LOCAL_QUORUM for lightweight transactions
ResultSet rs = session.execute(
    QueryBuilder.insertInto("my_table")
        .value("id", UUID.randomUUID())
        .value("data", "value")
        .ifNotExists()
        .consistencyLevel(ConsistencyLevel.LOCAL_QUORUM)
);
```

### 2. Increase Paxos Timeout

```yaml
# cassandra.yaml
cas_timeout_in_ms: 5000
```

### 3. Reduce Contention

```java
// Instead of LWT on a hot partition, use a separate contention key
String uniqueKey = UUID.randomUUID().toString();
ResultSet rs = session.execute(
    QueryBuilder.insertInto("my_table")
        .value("id", uniqueKey)
        .value("data", "value")
        .ifNotExists()
);
```

### 4. Avoid LWTs for High-Throughput Workloads

```java
// Use a regular insert if duplicate detection is handled at the application level
ResultSet rs = session.execute(
    QueryBuilder.insertInto("my_table")
        .value("id", uuid)
        .value("data", "value")
        .consistencyLevel(ConsistencyLevel.LOCAL_ONE)
);
```

### 5. Monitor Paxos Latency

```bash
nodetool proxyhistograms
# Look for cas_read and cas_write latency
```

### 6. Check for Contention in Application Logs

```java
// Log the result of IF NOT EXISTS to monitor contention
ResultSet rs = session.execute(insertStatement);
Row row = rs.one();
boolean applied = rs.wasApplied();
if (!applied) {
    // Handle contention - the insert was not applied
    log.warn("LWT contention detected for key: {}", uniqueKey);
}
```

## Common Mistakes

- Using LWTs on a high-contention partition key (e.g., a counter or queue)
- Not checking `wasApplied()` after an LWT, leading to silent data overwrites
- Setting the consistency level to `ALL` for LWTs, which increases latency dramatically
- Assuming LWT failures are always safe retries when they may have partially applied

## Related Pages

- [Cassandra WriteTimeoutException](/tools/cassandra/cassandra-write-timeout)
- [Cassandra ReadTimeoutException](/tools/cassandra/cassandra-read-timeout)
- [Cassandra Compaction Error](/tools/cassandra/cassandra-compaction-error)
