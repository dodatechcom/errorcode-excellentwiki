---
title: "[Solution] Redis Disk Quota Exceeded Error"
description: "How to fix Redis disk quota exceeded when the filesystem runs out of space"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Redis data files growing too large
- AOF file continuously growing
- System logs consuming disk space
- Insufficient partition size

## Fix

Check disk usage:

```bash
du -sh /var/lib/redis/
df -h /var/lib/redis/
```

Trim the AOF:

```bash
redis-cli BGREWRITEAOF
```

Find large keys:

```bash
redis-cli --bigkeys
```

Clean up old data:

```bash
redis-cli FLUSHDB
```

Add disk space or relocate data:

```bash
redis-cli CONFIG SET dir /data/redis/
```

## Examples

```bash
# Check disk usage by file type
find /var/lib/redis/ -type f -exec ls -lh {} \;

# Monitor disk usage
watch -n 10 'df -h /var/lib/redis/'

# Check inode usage
df -i /var/lib/redis/
```
