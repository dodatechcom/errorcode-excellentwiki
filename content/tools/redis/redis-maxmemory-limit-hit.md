---
title: "[Solution] Redis Maxmemory Limit Hit"
description: "How to handle Redis maxmemory limit being reached with proper eviction"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Data set growing beyond configured maxmemory
- Eviction policy not aggressive enough
- No key expiration (TTL) set on keys

## How to Fix

Check maxmemory and policy:

```bash
redis-cli CONFIG GET maxmemory
redis-cli CONFIG GET maxmemory-policy
```

Set appropriate eviction policy:

```bash
# For caching workload
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# For mixed workload
redis-cli CONFIG SET maxmemory-policy volatile-lru
```

Increase maxmemory if more RAM is available:

```bash
redis-cli CONFIG SET maxmemory 8gb
```

Find and remove unnecessary keys:

```bash
redis-cli --bigkeys
redis-cli --memkeys
```

## Examples

```bash
# Monitor eviction events
redis-cli INFO stats | grep evicted_keys

# Set TTL on keys
redis-cli EXPIRE mykey 3600

# Check memory usage of a key
redis-cli MEMORY USAGE mykey
```
