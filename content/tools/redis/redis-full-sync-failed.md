---
title: "[Solution] Redis Full Resync Failed Error"
description: "How to fix Redis full synchronization failure during initial replica setup"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Master cannot fork process for RDB save
- Network timeout during large dataset transfer
- Disk full on replica for RDB storage
- Master overloaded

## Fix

Check disk space on replica:

```bash
df -h /var/lib/redis/
```

Check master fork capability:

```bash
sysctl vm.overcommit_memory
```

Monitor sync progress:

```bash
redis-cli INFO replication | grep master_sync_in_progress
```

Increase timeout for large datasets:

```bash
redis-cli CONFIG SET repl-timeout 600
```

## Examples

```bash
# Check sync status
redis-cli INFO replication | grep -E "master_sync|master_repl"

# Monitor disk usage during sync
watch -n 2 'df -h /var/lib/redis/'

# Check master CPU during sync
top -p $(pidof redis-server)
```
