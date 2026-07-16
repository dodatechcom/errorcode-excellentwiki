---
title: "OOM command not allowed"
description: "Redis refuses a command because it would exceed the configured maxmemory limit"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oom", "memory", "maxmemory", "eviction"]
weight: 5
---

This error occurs when Redis rejects a write command because the configured `maxmemory` limit has been reached and there are no keys eligible for eviction under the current policy.

## Common Causes

- Application stores more data than the Redis instance is configured to hold
- maxmemory is set too low for the workload
- Eviction policy is set to `noeviction`
- Large key or batch write pushes memory over the limit

## How to Fix

1. Check current memory usage and maxmemory:

```bash
redis-cli INFO memory | grep -E "used_memory_human|maxmemory_human"
```

2. Increase the maxmemory limit:

```bash
redis-cli CONFIG SET maxmemory 1gb
```

3. Set an appropriate eviction policy:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

4. Find large keys and clean them up:

```bash
redis-cli --bigkeys
```

## Examples

```bash
redis-cli SET session:abc "data"
# (error) OOM command not allowed when used memory > 'maxmemory'.
```

## Related Errors

- [WRONGTYPE Operation against a key](/tools/redis/wrong-type)
