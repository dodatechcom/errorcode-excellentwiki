---
title: "Redis - OOM command not allowed"
description: "Redis rejects write commands because memory usage has reached the configured maxmemory limit"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

An OOM (Out of Memory) command not allowed error occurs when Redis memory usage reaches the `maxmemory` limit and the server refuses to execute commands that would require additional memory. This is a protective mechanism to prevent Redis from consuming all system memory.

## Common Causes

- `maxmemory` set too low for the workload
- Memory-heavy data structures (large hashes, lists, sets)
- No eviction policy configured or eviction cannot free enough memory
- Memory fragmentation causing actual usage to exceed limits
- Temporary spike in data volume

## How to Fix

1. Check current memory usage:

```bash
redis-cli INFO memory
redis-cli MEMORY USAGE key_name
```

2. Increase maxmemory in redis.conf:

```conf
# redis.conf
maxmemory 2gb
```

3. Set an appropriate eviction policy:

```conf
# redis.conf
maxmemory-policy allkeys-lru
# Options: volatile-lru, allkeys-lru, volatile-ttl, allkeys-random, noeviction
```

4. Set maxmemory at runtime:

```bash
redis-cli CONFIG SET maxmemory 4gb
```

5. Identify memory-heavy keys:

```bash
redis-cli --bigkeys
redis-cli MEMORY USAGE key_name
```

6. Clean up expired or unused keys:

```bash
redis-cli SCAN 0 MATCH temp:* COUNT 100
redis-cli DEL key1 key2 key3
```

## Examples

```bash
# Error: OOM command not allowed when used memory > 'maxmemory'
redis-cli SET large_key "very large value"
# OOM command not allowed when used memory ('1073741825') is greater than maxmemory ('1073741824')

# Fix: increase maxmemory
redis-cli CONFIG SET maxmemory 2gb
# Or clean up memory
redis-cli --bigkeys
```

## Related Errors

- [Memory error]({{< relref "/tools/redis/redis-memory-error" >}})
- [Persistence error]({{< relref "/tools/redis/redis-persistence-error" >}})
