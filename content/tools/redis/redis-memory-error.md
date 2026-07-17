---
title: "Redis Out of Memory Error"
description: "Redis server runs out of memory and cannot allocate more."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Redis Out of Memory Error

A Redis OOM error occurs when the Redis server reaches its `maxmemory` limit and cannot allocate more memory for new operations. This affects write operations until memory is freed.

## Common Causes

- maxmemory limit set too low
- Too many keys stored
- Large values consuming excessive memory
- Memory fragmentation

## How to Fix

### Check Current Memory Usage

```bash
redis-cli INFO memory
```

### Increase maxmemory

```conf
# /etc/redis/redis.conf
maxmemory 2gb
```

### Set Eviction Policy

```conf
# /etc/redis/redis.conf
maxmemory-policy allkeys-lru
```

### Monitor Memory Usage

```bash
redis-cli INFO memory
redis-cli DBSIZE
redis-cli MEMORY USAGE key_name
```

### Clean Up Old Keys

```bash
# Delete expired keys
redis-cli SCAN 0 MATCH session:* COUNT 100

# Use TTL on keys
redis-cli SET key value EX 3600
```

### Check for Memory Leaks

```bash
redis-cli MEMORY DOCTOR
```

## Examples

```bash
redis-cli SET mykey myvalue
OOM command not allowed when used memory > 'maxmemory'.

# Fix: increase maxmemory or clean up keys
redis-cli CONFIG SET maxmemory 4gb
```

## Related Errors

- [Connection Error]({{< relref "/tools/redis/redis-connection-error" >}}) — connection failure
- [Timeout Error]({{< relref "/tools/redis/redis-timeout-error" >}}) — operation timeout
