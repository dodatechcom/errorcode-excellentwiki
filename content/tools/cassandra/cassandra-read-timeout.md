---
title: "[Solution] Cassandra ReadTimeoutException - Fix Read Latency"
description: "Resolve Cassandra ReadTimeoutException by optimizing partition design to stay under 100MB, tuning consistency levels, and balancing replica load across nodes"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra `ReadTimeoutException` occurs when a read query does not receive enough replica responses within the configured timeout window. The coordinator knows the replicas are alive but the data could not be retrieved in time.

## What This Error Means

Unlike a `UnavailableException` (where replicas are unreachable), a `ReadTimeoutException` means the replicas are responding but are too slow. The coordinator received some responses but not enough to satisfy the requested consistency level before the timeout expired.

The exception details include the data size returned, the consistency level, and whether `data_present` is true (meaning some data was received but not enough).

## Why It Happens

- Large partitions causing slow reads from SSTables
- Insufficient memory for the key cache or row cache
- Compaction running concurrently and consuming I/O
- Replica nodes overloaded with too many concurrent reads
- Read consistency level too high for the cluster topology
- `read_request_timeout_in_ms` in `cassandra.yaml` is too low
- Using ALLOW FILTERING or secondary index scans that force full table scans

## How to Fix It

### 1. Increase the Read Timeout

```yaml
# cassandra.yaml
read_request_timeout_in_ms: 10000
range_request_timeout_in_ms: 15000
```

### 2. Use LOCAL_ONE or LOCAL_QUORUM for Reads

```java
ResultSet rs = session.execute(
    QueryBuilder.select().all().from("my_table")
        .whereColumn("id").isEqualTo(bindMarker())
        .consistencyLevel(ConsistencyLevel.LOCAL_QUORUM)
);
```

### 3. Optimize Partition Size

```sql
-- Avoid large partitions by redesigning the data model
-- Keep partitions under 100MB
SELECT * FROM my_table WHERE user_id = ? AND event_date = ?;
```

### 4. Tune Caches

```yaml
# cassandra.yaml
key_cache_size_in_mb: 2048
row_cache_size_in_mb: 0
```

### 5. Monitor Read Latency

```bash
nodetool proxyhistograms
nodetool tablestats my_keyspace.my_table
```

### 6. Avoid ALLOW FILTERING

```sql
-- Bad: full scan
SELECT * FROM my_table WHERE status = 'active' ALLOW FILTERING;

-- Good: query by partition key
SELECT * FROM my_table WHERE user_id = ? AND status = 'active';
```

## Common Mistakes

- Designing wide rows that grow unbounded, leading to multi-second reads
- Ignoring compaction pressure during peak read hours
- Using `ALL` consistency for read-heavy workloads
- Not setting up read repair or speculative retry properly in the driver configuration

## Related Pages

- [Cassandra WriteTimeoutException](/tools/cassandra/cassandra-write-timeout)
- [Cassandra Unavailable Exception](/tools/cassandra/cassandra-unavailable)
- [Cassandra Connection Error](/tools/cassandra/cassandra-connection-error)
- [Cassandra Compaction Error](/tools/cassandra/cassandra-compaction-error)
