---
title: "[Solution] Cassandra Write Timeout — How to Fix"
description: "Fix Cassandra write timeout errors by reducing mutation size, tuning commit log settings, balancing replica load, and configuring appropriate consistency levels."
tools: ["cassandra"]
error-types: ["write-timeout"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra write timeout occurs when the coordinator does not receive acknowledgment from enough replicas within the write timeout window. The write may or may not have been persisted — Cassandra does not distinguish between ack-received and ack-lost scenarios at the coordinator level.

## Why It Happens

Write timeouts are particularly dangerous because Cassandra may have accepted the mutation on some replicas but the coordinator timed out before receiving confirmation. This can lead to silent data divergence if not handled correctly.

- The commit log is blocked by fsync delays or disk saturation on replica nodes
- Memtable flushes are stalling due to memory pressure or high write throughput
- The consistency level requires more replicas than are currently available
- Network partitions prevent the coordinator from reaching some replicas
- Compaction is consuming I/O bandwidth needed for flush operations
- Large mutations (e.g., counter updates or large batches) take longer to apply
- The hinted handoff queue is full and cannot accept new hints

## Common Error Messages

```text
WriteTimeoutException: Cassandra timeout during write query at consistency LOCAL_QUORUM (2 responses were required but only 1 completed)
```

The coordinator needed two replica acknowledgments but only received one. The write may exist on some replicas but not all.

```text
WriteTimeoutException: Timed out after 2000ms writing to /10.0.1.2 (keyspace.table)
```

A specific replica node did not respond in time. The node may be overloaded or the disk may be saturated.

```text
UnavailableException: Cannot achieve LOCAL_QUORUM at consistency LOCAL_QUORUM because only 1 of 3 replicas are alive
```

Too few replicas are alive to satisfy the consistency level. No write was attempted.

```text
WriteFailureException: Operation failed for table — received 0 responses from一致性 level LOCAL_QUORUM (timeout)
```

Zero replicas responded. This typically indicates a severe network issue or all replicas are down.

## How to Fix It

### 1. Reduce Mutation Size

```java
// Bad: Large batch with many mutations
BatchStatement batch = BatchStatement.builder(BatchType.UNLOGGED)
    .add("INSERT INTO events (id, data) VALUES (1, ?)", largePayload)
    .add("INSERT INTO events (id, data) VALUES (2, ?)", largePayload)
    .build();
session.execute(batch);

// Good: Individual writes with async
for (Event event : events) {
    CompletableFuture.supplyAsync(() ->
        session.executeAsync(
            SimpleStatement.builder("INSERT INTO events (id, data) VALUES (?, ?)")
                .addPositionalValue(event.getId())
                .addPositionalValue(event.getData())
                .build()
        )
    );
}
```

Large mutations take longer to apply on replicas. Break them into smaller writes and use async execution to improve throughput.

### 2. Tune Commit Log and Flush Settings

```yaml
# cassandra.yaml
commitlog_sync: periodic
commitlog_sync_period_in_ms: 10000
commitlog_segment_size_in_mb: 32
commitlog_total_space_in_mb: 8192

# Increase write timeout
write_request_timeout_in_ms: 10000
```

```bash
# Check commit log disk I/O
iostat -x 1 5

# Monitor pending flushes
nodetool tpstats | grep -A5 "MemtableFlush"
```

Ensure the commit log is on fast storage (SSD). Use `commitlog_sync: batch` for stronger durability at the cost of latency, or `periodic` for better performance.

### 3. Lower Consistency Level for Writes

```java
// Use LOCAL_ONE for non-critical writes
session.execute(
    SimpleStatement.builder("INSERT INTO metrics (id, value) VALUES (?, ?)")
        .addPositionalValue(metricId)
        .addPositionalValue(metricValue)
        .setConsistencyLevel(ConsistencyLevel.LOCAL_ONE)
        .build()
);
```

```cql
-- Temporary consistency reduction during cluster instability
CONSISTENCY LOCAL_ONE;
INSERT INTO metrics (id, value) VALUES ('cpu_1', 85.3);
```

LOCAL_ONE requires only one replica acknowledgment, significantly reducing timeout probability. Use this for high-volume metrics or logging tables where occasional data loss is acceptable.

### 4. Fix Replica Node Health

```bash
# Check for GC pauses on replicas
grep -i "gc" /var/log/cassandra/system.log | tail -20

# Check disk usage on each node
df -h /var/lib/cassandra

# Check pending compactions
nodetool compactionstats

# Restart a problematic node
nodetool drain
sudo systemctl restart cassandra
```

Ensure all replica nodes have sufficient disk space, memory, and I/O capacity. A single overloaded replica can cause write timeouts for the entire cluster.

## Common Scenarios

**Write timeouts after increasing replication factor.** Adding replicas means more nodes must acknowledge each write. Increase the write timeout proportionally and ensure all new replica nodes are fully up and streaming complete before relying on them.

**Timeouts only on specific tables.** Some tables may have large partitions or high write volume. Check partition size with `nodetool tablehistograms` and redesign the data model if partitions exceed 100MB.

**Timeouts during compaction.** STCS (Size-Tiered Compaction Strategy) can cause I/O spikes during compaction. Switch to LCS (Leveled Compaction Strategy) for write-heavy workloads to spread compaction more evenly.

## Prevent It

- Monitor write latency at the 99th percentile with JMX or Prometheus and alert before timeouts occur
- Use LOCAL_ONE for high-volume non-critical writes and reserve LOCAL_QUORUM for data that requires strong consistency
- Schedule regular disk I/O benchmarks with fio to ensure commit log and data directories have sufficient throughput headroom
