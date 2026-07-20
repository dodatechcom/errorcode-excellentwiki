---
title: "[Solution] Redis OOM Command Not Allowed"
description: "How to fix Redis OOM error when used memory exceeds maxmemory limit"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- `maxmemory` limit reached and no eviction policy configured
- Eviction policy set to `noeviction`
- Large number of keys being written rapidly
- Memory fragmentation causing higher usage than expected

## How to Fix

Check current memory usage:

```bash
redis-cli INFO memory | grep used_memory_human
```

Check maxmemory setting:

```bash
redis-cli CONFIG GET maxmemory
```

Set an eviction policy:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

Increase maxmemory:

```bash
redis-cli CONFIG SET maxmemory 4gb
```

Analyze memory usage:

```bash
redis-cli MEMORY USAGE mykey
redis-cli MEMORY DOCTOR
```

## Examples

```bash
# Check memory breakdown
redis-cli INFO memory

# Find keys using most memory
redis-cli --bigkeys

# Force memory defragmentation
redis-cli MEMORY PURGE
```
