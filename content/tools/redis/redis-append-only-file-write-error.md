---
title: "[Solution] Redis AOF Write Error"
description: "How to fix Redis append-only file write errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Disk full
- I/O error on the storage device
- AOF file permissions changed

## Fix

Check disk space:

```bash
df -h /var/lib/redis/
```

Check disk health:

```bash
sudo smartctl -a /dev/sda
```

Verify file permissions:

```bash
ls -la /var/lib/redis/appendonly.aof
sudo chown redis:redis /var/lib/redis/appendonly.aof
```

Check AOF configuration:

```bash
redis-cli CONFIG GET appendfsync
redis-cli CONFIG GET appendonly
```

## Examples

```bash
# Check I/O errors
dmesg | grep -i error

# Test disk write
dd if=/dev/zero of=/var/lib/redis/test_write bs=1M count=100
rm /var/lib/redis/test_write

# Monitor AOF size
watch -n 5 'ls -lh /var/lib/redis/appendonly.aof'
```
