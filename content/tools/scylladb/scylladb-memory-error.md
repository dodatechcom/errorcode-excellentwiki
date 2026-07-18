---
title: "[Solution] ScyllaDB Memory Error — How to Fix"
description: "Fix ScyllaDB memory errors by tuning heap settings, resolving OOM crashes, and optimizing memory allocation for cache and compaction"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Memory Error

ScyllaDB memory errors occur when the system runs out of available memory for operations like caching, compaction, and query processing. ScyllaDB uses memory-mapped I/O extensively.

## Why It Happens

- Heap memory is exhausted due to large partitions
- Cache memory is too large for available RAM
- Compaction uses excessive memory
- Too many concurrent connections consume memory
- Memory leak in ScyllaDB or extension
- Cgroups memory limit is too low in containerized deployments

## Common Error Messages

```
OutOfMemoryError: Failed to allocate memory
```

```
MemoryLimitExceeded: Memory limit exceeded for query
```

```
CacheMemoryLimit: Cache memory budget exceeded
```

```
LinuxOOMKiller: ScyllaDB killed by OOM killer
```

## How to Fix It

### 1. Monitor Memory Usage

```bash
# Check ScyllaDB memory usage
nodetool memory

# Check cache memory
nodetool info | grep -i memory

# Check OS memory
free -h
cat /proc/meminfo | grep -i "mem\|swap"

# Check for OOM kills
dmesg | grep -i oom
journalctl -k | grep -i oom
```

### 2. Configure Memory Limits

```yaml
# In scylla.yaml
# Limit per-core memory (for Scylla enterprise)
# Per-core memory for cache
# memory: 4G

# Reduce cache size if memory is tight
# default_cache_size_in_mb: 2048
```

```bash
# Set memory limit via scylla setup
sudo scylla_setup --memory 4G

# Or set via command line
scylla --memory 4G --smp 4
```

### 3. Reduce Memory Pressure

```bash
# Reduce concurrent requests
nodetool setstreamthroughput 100

# Compact more aggressively to free memory
nodetool compact mykeyspace mytable

# Clear caches (causes temporary performance drop)
nodetool invalidatecachecorruptkeys
```

```yaml
# In scylla.yaml - reduce cache memory
# cache_hit_rate: 0.95
# Increase compaction throughput to free memory faster
compaction_throughput_mb_per_sec: 64
```

### 4. Fix Container Memory Limits

```yaml
# Docker Compose
services:
  scylla:
    image: scylladb/scylla
    deploy:
      resources:
        limits:
          memory: 8G
    # Ensure ScyllaDB knows its memory limit
    command: --memory 4G --smp 4
```

```bash
# Check container memory limits
docker inspect scylla | grep -i memory

# Monitor inside container
docker exec scylla free -h
docker exec scylla nodetool info | grep -i memory
```

## Common Scenarios

- **OOM kill after large query**: Reduce partition size or increase `read_request_timeout_in_ms`.
- **Cache memory exceeds RAM**: Reduce `default_cache_size_in_mb` or increase physical memory.
- **Container OOM restart**: Set explicit memory limits and inform ScyllaDB via `--memory` flag.

## Prevent It

- Reserve at least 2GB RAM per ScyllaDB core for OS overhead
- Monitor memory usage with `nodetool memory` regularly
- Set up OOM killer prevention with cgroups

## Related Pages

- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
