---
title: "[Solution] Redis Maxmemory Policy Invalid Error"
description: "How to fix Redis invalid maxmemory-policy configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Policy name misspelled
- Using volatile-* policy with no keys having TTL
- Policy not compatible with Redis version

## Fix

Check valid policies:

```bash
redis-cli CONFIG GET maxmemory-policy
```

Valid values:

```bash
noeviction       # return errors when memory limit reached
allkeys-lru      # evict any key using LRU
volatile-lru     # evict keys with TTL using LRU
allkeys-random   # evict random keys
volatile-random  # evict random keys with TTL
volatile-ttl     # evict keys with shortest TTL
allkeys-lfu      # evict least frequently used keys (Redis 4.0+)
volatile-lfu     # evict least frequently used keys with TTL (Redis 4.0+)
```

Set valid policy:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

## Examples

```bash
# Check current policy
redis-cli CONFIG GET maxmemory-policy

# Set appropriate policy
redis-cli CONFIG SET maxmemory-policy volatile-lru

# Set TTL on keys for volatile policies
redis-cli EXPIRE mykey 3600
```
