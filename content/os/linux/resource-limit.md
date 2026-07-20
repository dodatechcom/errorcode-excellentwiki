---
title: "[Solution] Linux: resource-limit — resource limit exceeded"
description: "Fix Linux resource-limit errors. resource limit exceeded with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: Resource Limit Exceeded

Resource limit errors occur when a process exceeds system or user-configured resource limits.

## Common Causes

- File descriptor limit (ulimit -n) too low
- Process/thread limit (ulimit -u) reached
- Memory limit (ulimit -m) exceeded
- Core file size limit (ulimit -c) restricting dumps
- Stack size limit (ulimit -s) too small

## How to Fix

### 1. Check Current Limits

```bash
ulimit -a
cat /proc/<pid>/limits
```

### 2. Check System-Wide Limits

```bash
cat /proc/sys/fs/file-max
cat /proc/sys/kernel/pid_max
cat /proc/sys/kernel/threads-max
```

### 3. Increase Limits

```bash
# For current session
ulimit -n 65536
# Permanently
echo "* soft nofile 65536" >> /etc/security/limits.conf
echo "* hard nofile 65536" >> /etc/security/limits.conf
```

### 4. Adjust systemd Limits

```bash
# In service file:
# [Service]
# LimitNOFILE=65536
sudo systemctl daemon-reload
```

## Examples

```bash
$ ulimit -n
1024
$ cat /proc/12345/limits | grep "open files"
Max open files            1024    4096    files
$ ls /proc/12345/fd | wc -l
1022
# Process about to hit file descriptor limit
$ ulimit -n 65536
$ # Restart application with higher limit
```
