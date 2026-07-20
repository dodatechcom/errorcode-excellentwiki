---
title: "[Solution] Redis AOF File Corrupted"
description: "How to fix Redis AOF file corruption issues"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Server crashed during AOF write
- Power failure during persistence
- Disk I/O error
- Incomplete write due to disk full

## How to Fix

Check AOF file integrity:

```bash
redis-check-aof --fix /var/lib/redis/appendonly.aof
```

If the AOF is too corrupted, truncate and rebuild from RDB:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
# If truncated, fix it:
echo -n "" | sudo tee /var/lib/redis/appendonly.aof
```

Start Redis and let it rebuild:

```bash
sudo systemctl start redis
```

Prevent future corruption with AOF fsync:

```bash
redis-cli CONFIG SET appendfsync everysec
```

## Examples

```bash
# Check AOF integrity
redis-check-aof /var/lib/redis/appendonly.aof

# Fix corrupted AOF
redis-check-aof --fix /var/lib/redis/appendonly.aof

# Verify RDB backup
redis-check-rdb /var/lib/redis/dump.rdb
```
