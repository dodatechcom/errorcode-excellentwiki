---
title: "[Solution] ScyllaDB Seastar Memory Allocation Error — How to Fix"
description: "Fix ScyllaDB Seastar memory allocation errors when the reactor cannot allocate memory for request processing"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Seastar Memory Allocation Error

Seastar memory allocation errors occur when the ScyllaDB reactor thread cannot allocate memory from its per-core memory pool, causing request failures or node crashes.

## Why It Happens

- Memory is over-provisioned relative to available RAM
- Large partition reads consume excessive per-core memory
- Per-core memory pools are fragmented
- Compaction requires more memory than available
- Memory is leaked by long-running operations

## Common Error Messages

```
seastar: failed to allocate memory (size=4096)
```

```
ERROR: reactor stalled for 1000ms: memory allocation failed
```

```
seastar: Cannot allocate memory for buffer
```

## How to Fix It

### 1. Check Memory Allocation

```bash
nodetool memory
free -g
```

### 2. Reduce Memory-Intensive Operations

```bash
# Limit concurrent compactions
nodetool setcompactionthroughput -t 64
```

### 3. Adjust Memory Pool Size

```bash
# Start Scylla with specific memory allocation
scylla --memory 4G --smp 2
```

### 4. Monitor Memory Usage Per Core

```bash
curl -s http://localhost:9180/metrics | grep seastar_memory
```

## Examples

```
seastar: shard 3 failed to allocate 65536 bytes
seastar: reactor stalled for 2500ms while allocating memory
```

## Prevent It

- Allocate only 80% of RAM to ScyllaDB
- Monitor per-core memory usage with Scylla Monitoring
- Avoid running other memory-intensive processes on the same host

## Related Pages

- [ScyllaDB Memory Error](/tools/scylladb/scylladb-memory-error)
- [ScyllaDB Seastar Reactor Stall](/tools/scylladb/scylladb-seastar-reactor-stall)
- [ScyllaDB Seastar Reactor Stall Error](/tools/scylladb/scylladb-seastar-reactor-stall-error)
