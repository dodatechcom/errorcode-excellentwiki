---
title: "[Solution] Redis Memory Fragmentation Error"
description: "How to fix Redis memory fragmentation ratio issues"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Fragmentation ratio > 1.5 indicates external fragmentation
- Frequent updates to keys of different sizes
- jemalloc allocator not optimizing properly
- Large key operations creating fragmentation

## How to Fix

Check fragmentation ratio:

```bash
redis-cli INFO memory | grep mem_fragmentation_ratio
```

Trigger memory defragmentation:

```bash
redis-cli MEMORY PURGE
```

Restart Redis to defragment (if persistent storage is safe):

```bash
sudo systemctl restart redis
```

Use active defragmentation (Redis 4.0+):

```bash
redis-cli CONFIG SET activedefrag yes
redis-cli CONFIG SET active-defrag-enabled yes
```

Analyze key sizes:

```bash
redis-cli --bigkeys
redis-cli --memkeys
```

## Examples

```bash
# Monitor fragmentation
watch -n 5 'redis-cli INFO memory | grep -E "used_memory_rss_human|mem_fragmentation_ratio"'

# Check allocator
redis-cli INFO memory | grep mem_allocator

# Manual defrag
redis-cli MEMORY PURGE
```
