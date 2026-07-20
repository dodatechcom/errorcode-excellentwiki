---
title: "[Solution] Redis Busy Loading Error"
description: "How to fix Redis busy loading error when the server is still loading data from disk"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Large RDB dump file taking long to load
- Server just started and data not yet loaded
- AOF rewrite in progress
- Insufficient I/O bandwidth for loading
- Dataset too large for available memory during load

## How to Fix

Wait for loading to complete:

```bash
# Check loading status
redis-cli INFO persistence | grep loading
```

Check RDB file size:

```bash
ls -lh /var/lib/redis/dump.rdb
```

Switch to AOF for faster startup:

```bash
redis-cli CONFIG SET appendonly yes
```

Increase loading speed with better hardware or by reducing dataset size:

```bash
# Monitor loading progress
redis-cli INFO persistence | grep rdb_last_bgsave_status
```

## Examples

```bash
# Check if Redis is still loading
redis-cli PING
# If loading: LOADING Redis is loading the dataset in memory

# Wait and retry
while [ "$(redis-cli PING)" != "PONG" ]; do sleep 1; done
echo "Redis is ready"
```
