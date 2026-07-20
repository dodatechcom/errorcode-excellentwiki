---
title: "[Solution] Redis Maxmemory Samples Configuration Error"
description: "How to fix Redis maxmemory-samples configuration for eviction policies"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- maxmemory-samples too low causing poor eviction decisions
- maxmemory-samples too high causing CPU overhead
- Invalid sample count

## Fix

Check current setting:

```bash
redis-cli CONFIG GET maxmemory-samples
```

Set appropriate sample count:

```bash
# Default: 5 (good balance)
redis-cli CONFIG SET maxmemory-samples 5

# Higher accuracy (more CPU)
redis-cli CONFIG SET maxmemory-samples 10
```

Check eviction efficiency:

```bash
redis-cli INFO stats | grep evicted_keys
```

## Examples

```bash
# Check maxmemory-samples
redis-cli CONFIG GET maxmemory-samples

# Set samples for better eviction
redis-cli CONFIG SET maxmemory-samples 7

# Monitor eviction rate
watch -n 5 'redis-cli INFO stats | grep evicted_keys'
```
