---
title: "[Solution] Cassandra GC Overhead Limit Exceeded - Fix JVM Memory"
description: "Fix Cassandra GC overhead limit exceeded by tuning JVM heap size to under 8GB, enabling the G1GC garbage collector, and reducing concurrent memory pressure"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra `GC overhead limit exceeded` error occurs when the JVM spends more than 98% of its time in garbage collection while reclaiming less than 2% of heap memory. This is a fatal condition that typically causes the node to stop responding.

## What This Error Means

When the JVM detects that garbage collection is consuming excessive CPU with minimal memory recovery, it throws `java.lang.OutOfMemoryError: GC overhead limit exceeded`. For Cassandra, this means the node is under extreme memory pressure and may become unresponsive to client requests, fail to respond to gossip, and eventually be marked down by other nodes.

This error is distinct from a heap space `OutOfMemoryError` because it specifically relates to GC efficiency rather than absolute memory exhaustion.

## Why It Happens

- JVM heap allocated too much memory (exceeding available physical RAM)
- Large partitions loaded into memory during reads
- Too many concurrent compactions or streaming operations
- Off-heap memory misconfigured (Bloom filters, key cache, row cache)
- Memory leak in custom UDFs or extensions
- Insufficient heap for the number of concurrent connections
- G1GC not configured for large heaps (staying with CMS)

## How to Fix It

### 1. Check Current JVM Settings

```bash
# Check what Cassandra is using
ps aux | grep cassandra | grep -o '\-Xm[sx][^ ]*'
```

### 2. Set Appropriate Heap Size

```bash
# conf/jvm-server.options or conf/cassandra-env.sh
# Rule of thumb: no more than 8GB for G1GC, no more than 50% of RAM
-Xms8G
-Xmx8G
```

### 3. Enable G1GC for Large Heaps

```bash
# conf/jvm-server.options
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:InitiatingHeapOccupancyPercent=70
-XX:G1RSetUpdatingPauseTimePercent=5
```

### 4. Monitor Heap Usage

```bash
nodetool info
nodetool tpstats
```

### 5. Reduce Off-Heap Usage

```yaml
# cassandra.yaml - reduce cache sizes
key_cache_size_in_mb: 512
row_cache_size_in_mb: 0
counter_cache_size_in_mb: 0
```

### 6. Limit Concurrent Operations

```yaml
# cassandra.yaml
concurrent_reads: 32
concurrent_writes: 32
concurrent_compactors: 2
```

## Common Mistakes

- Allocating 32GB heap on a 32GB machine, leaving nothing for the OS and page cache
- Not switching from CMS to G1GC when increasing heap beyond 8GB
- Ignoring off-heap memory usage when tuning the JVM
- Setting `-Xms` and `-Xmx` to different values causing heap resizing pauses

## Related Pages

- [Cassandra WriteTimeoutException](/tools/cassandra/cassandra-write-timeout)
- [Cassandra ReadTimeoutException](/tools/cassandra/cassandra-read-timeout)
- [Cassandra Compaction Error](/tools/cassandra/cassandra-compaction-error)
