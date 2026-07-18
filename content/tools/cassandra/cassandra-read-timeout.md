---
title: "[Solution] Cassandra Read Timeout — How to Fix"
description: "Fix Cassandra read timeout errors by tuning consistency levels, optimizing query patterns, increasing timeouts, and rebalancing replica placement."
tools: ["cassandra"]
error-types: ["read-timeout"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra read timeout occurs when the coordinator node does not receive enough replica responses within the configured timeout window. The data may exist on the cluster, but the coordinator gave up waiting before all required replicas replied.

## Why It Happens

Read timeouts are often symptoms of underlying cluster stress rather than a simple configuration issue. The coordinator must collect responses from a quorum of replicas, and any delay on those replicas can trigger the timeout.

- Replicas are overloaded with compaction, streaming, or repair work
- The consistency level requires more responses than are available (e.g., LOCAL_QUORUM with only one replica up)
- GC pauses on replica nodes prevent timely response to the coordinator
- Network latency between the coordinator and replicas exceeds the read timeout
- The query is scanning too many rows or returning a large result set
- SSTable counts are high due to excessive compaction pressure
- The read repair mechanism is adding overhead to reads under LOCAL_QUORUM

## Common Error Messages

```text
ReadTimeoutException: Cassandra timeout during read query at consistency LOCAL_QUORUM (2 responses were required but only 1 completed)
```

The coordinator needed two replica responses but only received one. This is the most common read timeout pattern.

```text
ReadTimeoutException: Timed out after 2000ms while reading from [/10.0.1.1, /10.0.1.2] (keyspace.table)
```

The coordinator timed out entirely. Replicas may be unreachable or severely overloaded.

```text
UnavailableException: Not enough live replicas to achieve LOCAL_QUORUM at consistency LOCAL_QUORUM
```

Not enough replicas are alive to satisfy the consistency requirement. This is distinct from a timeout—the coordinator knows immediately that it cannot satisfy the request.

```text
OverloadedException: Too many in-flight requests (1024) on node /10.0.1.2
```

A replica node has hit its pending request limit and is refusing new work.

## How to Fix It

### 1. Lower the Consistency Level Temporarily

```java
// Instead of LOCAL_QUORUM, use LOCAL_ONE for latency-sensitive reads
ResultSet rs = session.execute(
    SimpleStatement.builder("SELECT * FROM users WHERE id = ?")
        .addPositionalValue(userId)
        .setConsistencyLevel(ConsistencyLevel.LOCAL_ONE)
        .build()
);
```

```cql
-- Lower consistency at the CQL level
CONSISTENCY LOCAL_ONE;
SELECT * FROM users WHERE id = 12345;
```

This sacrifices read-your-writes consistency but prevents timeouts during cluster instability. Revert to LOCAL_QUORUM once the cluster is healthy.

### 2. Increase Read Timeout Settings

```yaml
# cassandra.yaml on each node
read_request_timeout_in_ms: 10000
range_request_timeout_in_ms: 20000
```

```java
// Driver-side timeout
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.1", 9042))
    .withLocalDatacenter("datacenter1")
    .withConfigLoader(DriverConfigLoader.fromString(
        "basic.request.timeout = 15s\n"))
    .build();
```

Increase both the server-side timeout in cassandra.yaml and the driver-side timeout. Ensure the driver timeout is longer than the server timeout to avoid premature client-side aborts.

### 3. Optimize the Query Pattern

```cql
-- Bad: Full table scan
SELECT * FROM events WHERE event_type = 'login';

-- Good: Partition-scoped query with limit
SELECT * FROM events WHERE partition_key = 'user_12345' LIMIT 100;
```

```java
// Bad: Fetching all columns
ResultSet rs = session.execute("SELECT * FROM large_table WHERE id = ?");

// Good: Select only needed columns
ResultSet rs = session.execute(
    "SELECT id, name, email FROM large_table WHERE id = ?");
```

Avoid ALLOW FILTERING, wide partition reads, and queries that return thousands of rows. Use pagination with `fetchSize()` to control result set size.

### 4. Repair Nodes and Rebalance Load

```bash
# Run anti-entropy repair to fix replica inconsistencies
nodetool repair -pr keyspace_name table_name

# Check for hot spots
nodetool tablestats keyspace_name.table_name

# Verify replica placement
nodetool ring
```

Run repair regularly (at least once per GC grace seconds period) to ensure replicas stay in sync. Uneven token ranges cause some nodes to receive disproportionate read traffic.

## Common Scenarios

**Timeouts spike after deploying new code.** New queries may introduce full table scans or large partition reads. Enable query tracing with `tracing ON` in cqlsh to identify slow queries, and review the `cassandra.yaml` trace sampling settings.

**Reads fail only during peak hours.** The cluster may not have enough capacity for peak read throughput. Add read replicas with `ALTER KEYSPACE` to increase replication factor, or scale horizontally with additional nodes to distribute load.

**One datacenter reads fine but another times out.** Cross-datacenter reads add latency. Verify the driver is routing reads to the local datacenter and not accidentally sending requests to a remote DC through incorrect `localDatacenter` configuration.

## Prevent It

- Set up continuous repair with Medusa or Reaper to run weekly and keep replicas synchronized across the cluster
- Monitor read latency p99 with the Cassandra metrics exporter and alert when p99 exceeds 500ms
- Profile all queries in staging with `nodetool tablehistograms` to catch expensive reads before production deployment
