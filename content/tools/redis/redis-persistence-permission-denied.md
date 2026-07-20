---
title: "[Solution] Redis Persistence Permission Denied"
description: "How to fix Redis file permission errors during persistence operations"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Redis process does not own the data directory
- SELinux or AppArmor blocking access
- Read-only filesystem

## Fix

Check ownership:

```bash
ls -la /var/lib/redis/
sudo chown -R redis:redis /var/lib/redis/
```

Check SELinux:

```bash
sudo getenforce
sudo ausearch -m avc -ts recent | grep redis
```

Set correct SELinux context:

```bash
sudo semanage fcontext -a -t redis_var_lib_t "/var/lib/redis(/.*)?"
sudo restorecon -Rv /var/lib/redis/
```

## Examples

```bash
# Check file system permissions
namei -l /var/lib/redis/dump.rdb

# Check process user
ps aux | grep redis

# Verify writable directory
sudo -u redis touch /var/lib/redis/test_file && rm /var/lib/redis/test_file
```
