---
title: "Redis - RDB save failed"
description: "Redis fails to save data to disk during RDB persistence, potentially losing data on restart"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

An RDB save failed error occurs when Redis cannot complete a background save to create an RDB snapshot. This can result in data loss if the server restarts before a successful save completes.

## Common Causes

- Disk space exhaustion on the data volume
- Disk I/O latency or failure
- fork() failure due to insufficient memory for background save
- RDB file path not writable
- Large dataset causing save to take too long

## How to Fix

1. Check disk space:

```bash
df -h /var/lib/redis
du -sh /var/lib/redis/dump.rdb
```

2. Free up disk space:

```bash
# Remove old RDB files
rm -f /var/lib/redis/dump.rdb.bak

# Check Redis log for save errors
tail -100 /var/log/redis/redis.log
```

3. Check RDB configuration:

```conf
# redis.conf
save 900 1      # save after 900 seconds if at least 1 key changed
save 300 10     # save after 300 seconds if at least 10 keys changed
save 60 10000   # save after 60 seconds if at least 10000 keys changed

dir /var/lib/redis
dbfilename dump.rdb
```

4. Trigger manual save for testing:

```bash
redis-cli BGSAVE
# Check status
redis-cli LASTSAVE
redis-cli INFO persistence
```

5. Ensure sufficient memory for fork:

```bash
# Redis needs ~2x memory during fork for RDB
# Check available memory
free -h

# If low memory, reduce dataset or increase RAM
```

6. Switch to AOF for more reliable persistence:

```conf
# redis.conf
appendonly yes
appendfsync everysec
```

## Examples

```bash
# Error: Failed opening the RDB dump file for saving: No space left on device
$ redis-cli BGSAVE
Background save failed: No space left on device

# Fix: free disk space and retry
$ rm -f /var/log/redis/*.gz
$ redis-cli BGSAVE
OK
```

## Related Errors

- [Memory error]({{< relref "/tools/redis/redis-memory-error" >}})
- [Cluster error]({{< relref "/tools/redis/redis-cluster-error" >}})
