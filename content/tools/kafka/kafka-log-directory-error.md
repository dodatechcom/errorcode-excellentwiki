---
title: "[Solution] Kafka Log Directory Error"
description: "Fix Kafka log directory errors. Resolve issues with broker failing to access or create log directories."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Log Directory Error

Kafka log directory errors occur when the broker cannot read, write, or create files in the configured log directory due to permissions, disk, or filesystem issues.

## Common Causes

- Log directory does not exist on the broker filesystem
- Filesystem permissions not set for the kafka user
- Disk is full or mounted read-only
- Symbolic link in log.dirs pointing to a missing mount

## How to Fix

1. Create the log directory with correct ownership:

```bash
sudo mkdir -p /data/kafka-logs
sudo chown -R kafka:kafka /data/kafka-logs
```

2. Check disk space:

```bash
df -h /data/kafka-logs
```

3. Verify the log.dirs configuration:

```bash
grep 'log.dirs' /etc/kafka/server.properties
```

4. Check for filesystem errors:

```bash
dmesg | grep -i "error\|readonly"
mount | grep /data
```

## Examples

```bash
# Monitor disk usage on log directories
du -sh /data/kafka-logs/* | sort -rh | head -10

# Check inode availability
df -i /data/kafka-logs
```
