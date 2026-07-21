---
title: "[Solution] ScyllaDB Cache Warming Error — How to Fix"
description: "Fix ScyllaDB cache warming errors when the key or row cache fails to populate correctly after restart"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Cache Warming Error

Cache warming errors occur when ScyllaDB fails to properly warm the key cache or row cache after a restart, causing performance degradation during the warming period.

## Why It Happens

- Cache size is too small for the working dataset
- Key cache persistence file is corrupted
- Memory pressure prevents cache population
- Too many tables are configured for cache warming
- Cache warming I/O competes with normal read traffic

## Common Error Messages

```
WARN: Failed to load key cache from disk
```

```
error: row cache size exceeds available memory
```

```
cache_warming: unable to warm cache for table mykeyspace.users
```

## How to Fix It

### 1. Increase Cache Size

```yaml
# In scylla.yaml
key_cache_size_in_mb: 1024
row_cache_size_in_mb: 2048
```

### 2. Clear and Rebuild Cache

```bash
nodetool invalidatekeycache
nodetool invalidaterowcache
nodetool drain
sudo systemctl restart scylla-server
```

### 3. Configure Cache Persistence

```yaml
# In scylla.yaml
key_cache_save_period: 14400
row_cache_save_period: 0
key_cache_keys_to_save: 100000
```

### 4. Limit Cache-Warmed Tables

```cql
ALTER TABLE mykeyspace.large_table WITH caching = {'keys': 'NONE', 'rows_per_partition': 'NONE'};
```

## Examples

```
INFO  [main] Key cache was successfully warmed. Loaded 1500000 entries
WARN  [main] Row cache warming skipped: insufficient memory (need 4GB, have 1GB free)
```

## Prevent It

- Size caches appropriately for working set
- Monitor cache hit rates after restarts
- Warm caches during off-peak hours

## Related Pages

- [ScyllaDB Cache Error](/tools/scylladb/scylladb-cache-error)
- [ScyllaDB Memory Error](/tools/scylladb/scylladb-memory-error)
- [ScyllaDB Node Down](/tools/scylladb/scylladb-node-down)
