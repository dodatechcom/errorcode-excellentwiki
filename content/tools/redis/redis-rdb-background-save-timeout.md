---
title: "[Solution] Redis RDB Background Save Timeout"
description: "How to fix Redis RDB background save timeout when BGSAVE takes too long"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Large dataset requiring extended save time
- Slow disk I/O
- CPU contention from client operations
- Network storage (NFS) causing slow writes

## Fix

Check save progress:

```bash
redis-cli INFO persistence | grep rdb_bgsave_in_progress
```

Check disk performance:

```bash
iostat -x 1 5
```

Move to local SSD if using network storage:

```bash
redis-cli CONFIG SET dir /mnt/ssd/redis/
```

Monitor save duration:

```bash
redis-cli INFO stats | grep latest_fork_usec
```

## Examples

```bash
# Check BGSAVE status
redis-cli LASTSAVE
redis-cli INFO persistence | grep rdb_last_bgsave_time_sec

# Check disk I/O
iotop -p $(pidof redis-server)

# Benchmark disk write speed
dd if=/dev/zero of=/var/lib/redis/test bs=1M count=1024 oflag=direct
rm /var/lib/redis/test
```
