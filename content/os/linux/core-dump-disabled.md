---
title: "[Solution] Linux: core-dump-disabled — core dump disabled"
description: "Fix Linux core-dump-disabled errors. core dump disabled with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 4
---
# Linux: Core Dump Disabled

Core dumps are disabled when the system prevents saving crash information for debugging. This makes debugging process crashes more difficult.

## Common Causes

- Core dump size limit set to 0 (ulimit -c 0)
- core_pattern set to disable core dumps (|/bin/false)
- Apport or systemd-coredump not properly configured
- Filesystem full preventing core dumps from being written
- Directory for core dumps has wrong permissions

## How to Fix

### 1. Check Current Core Dump Settings

```bash
ulimit -c
cat /proc/sys/kernel/core_pattern
cat /proc/sys/kernel/core_uses_pid
```

### 2. Enable Core Dumps Temporarily

```bash
ulimit -c unlimited
```

### 3. Enable Core Dumps System-Wide

```bash
# Set core file pattern
echo "core.%p" | sudo tee /proc/sys/kernel/core_pattern

# Make permanent
echo "kernel.core_pattern=core.%p" | sudo tee -a /etc/sysctl.conf
echo "* soft core unlimited" | sudo tee -a /etc/security/limits.conf
```

### 4. Use systemd-coredump

```bash
sudo systemctl enable systemd-coredump.socket
sudo systemctl start systemd-coredump.socket
# Then use coredumpctl to access
coredumpctl list
coredumpctl info <PID>
```

## Examples

```bash
$ ulimit -c
0

$ ulimit -c unlimited
$ ./myprogram
Segmentation fault (core dumped)

$ ls -la core*
-rw------- 1 user user 12345678 Jul 20 14:30 core.12345

$ coredumpctl list
TIME                            PID   UID   GID SIG COREFILE EXE
Mon 2026-07-20 14:30:45 UTC   12345  1000  1000  11 present /home/user/myprogram
```
