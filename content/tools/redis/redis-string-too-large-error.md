---
title: "[Solution] Redis String Value Too Large Error"
description: "How to fix Redis string too large errors when storing values"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Value exceeds 512 MB maximum string size
- Client buffer limit exceeded
- Memory allocation failure for large values

## Fix

Check max value size:

```bash
redis-cli CONFIG GET maxmemory
```

Split large values into smaller chunks:

```bash
# Store as hash fields instead of one large string
redis-cli HSET bigdata chunk:0 "part1"
redis-cli HSET bigdata chunk:1 "part2"
```

Use client-side chunking:

```python
import redis
r = redis.Redis()
chunk_size = 1024 * 1024  # 1MB chunks
for i in range(0, len(data), chunk_size):
    r.SET(f"key:{i}", data[i:i+chunk_size])
```

## Examples

```bash
# Check string length
redis-cli STRLEN mykey

# Check max memory
redis-cli CONFIG GET maxmemory

# Use MEMORY USAGE to check size
redis-cli MEMORY USAGE mykey
```
