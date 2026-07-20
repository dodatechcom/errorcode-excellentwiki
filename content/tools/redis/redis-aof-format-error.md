---
title: "[Solution] Redis AOF Format Error"
description: "How to fix Redis AOF format parsing errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- AOF file contains invalid Redis protocol
- Partial write during crash
- Manual editing of AOF file
- Version incompatibility

## Fix

Check AOF integrity:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
```

Fix the AOF:

```bash
redis-check-aof --fix /var/lib/redis/appendonly.aof
```

Start with RDB only:

```bash
sudo mv /var/lib/redis/appendonly.aof /var/lib/redis/appendonly.aof.bak
sudo systemctl start redis
# Re-enable AOF
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Check AOF format
redis-check-aof /var/lib/redis/appendonly.aof

# View AOF tail
tail -20 /var/lib/redis/appendonly.aof

# Restart with AOF disabled
redis-server /etc/redis/redis.conf --appendonly no
```
