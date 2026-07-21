---
title: "[Solution] TiDB Coprocessor Cache Error — How to Fix"
description: "Fix TiDB coprocessor cache errors when the coprocessor request cache exceeds memory limits or returns stale data"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Coprocessor Cache Error

Coprocessor cache errors occur when the TiDB coprocessor request cache encounters memory limits, stale data, or configuration issues that prevent efficient query processing.

## Why It Happens

- Coprocessor cache size exceeds the configured memory limit
- Cache contains stale data after region merges or splits
- TiKV node is overloaded and cannot process cached requests
- Cache eviction policy is not suitable for the workload
- Memory pressure causes cache thrashing

## Common Error Messages

```
ERROR: coprocessor cache exceeded memory limit
```

```
WARN: coprocessor cache is full, evicting old entries
```

```
error: coprocessor request failed: region not found
```

## How to Fix It

### 1. Adjust Cache Size

```toml
# In tikv.toml
[readpool.coprocessor]
# Increase max memory for coprocessor cache
```

### 2. Monitor Cache Hit Rate

```bash
curl -s http://tikv:20180/metrics | grep tikv_coprocessor_cache_hit_rate
```

### 3. Configure Cache Eviction

```toml
# In tidb.toml
[tikv-client]
coprocessor-cache-capacity = 1073741824
```

### 4. Balance Coprocessor Load

```bash
# Check coprocessor distribution across TiKV nodes
curl -s http://tidb:10080/api/v1/tikv/regions | jq '.regions | length'
```

## Examples

```
$ curl -s http://tikv:20180/metrics | grep coprocessor_cache
tikv_coprocessor_cache_hit_total 1500000
tikv_coprocessor_cache_miss_total 500000
```

## Prevent It

- Monitor cache hit rate and adjust size accordingly
- Use appropriate cache eviction policies
- Balance coprocessor load across TiKV nodes

## Related Pages

- [TiDB Coprocessor Error](/tools/tidb/tidb-coprocessor-error)
- [TiDB Tikv Coprocessor Error](/tools/tidb/tidb-tikv-coprocessor-error)
- [TiDB Query Error](/tools/tidb/tidb-query-error)
