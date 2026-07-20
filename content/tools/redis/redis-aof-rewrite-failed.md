---
title: "[Solution] Redis AOF Rewrite Failed"
description: "How to fix Redis AOF rewrite failure during background AOF rewriting"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Insufficient disk space for new AOF file
- Fork operation failed due to memory pressure
- Rewrite buffer exceeded memory limit
- Child process terminated abnormally

## How to Fix

Check AOF rewrite status:

```bash
redis-cli INFO persistence | grep aof_rewrite_in_progress
```

Check disk space:

```bash
df -h /var/lib/redis/
```

Disable AOF rewrite temporarily:

```bash
redis-cli CONFIG SET auto-aof-rewrite-percentage 0
```

Check AOF file integrity:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
```

## Examples

```bash
# Trigger manual rewrite
redis-cli BGREWRITEAOF

# Monitor AOF rewrite
watch -n 1 'redis-cli INFO persistence | grep aof'

# Check AOF size
ls -lh /var/lib/redis/appendonly.aof
```
