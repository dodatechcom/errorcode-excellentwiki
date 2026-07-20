---
title: "[Solution] Redis Log File Permission Error"
description: "How to fix Redis log file permission and access errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Log file directory not writable by redis user
- Log file owned by wrong user
- Disk full preventing log writes

## Fix

Check log file permissions:

```bash
ls -la /var/log/redis/
sudo chown redis:redis /var/log/redis/redis-server.log
sudo chmod 644 /var/log/redis/redis-server.log
```

Check disk space:

```bash
df -h /var/log/
```

Update log configuration:

```bash
redis-cli CONFIG SET logfile /var/log/redis/redis-server.log
redis-cli CONFIG SET loglevel verbose
```

## Examples

```bash
# Check log file
ls -la /var/log/redis/

# View Redis logs
sudo tail -50 /var/log/redis/redis-server.log

# Set log level
redis-cli CONFIG SET loglevel verbose
```
