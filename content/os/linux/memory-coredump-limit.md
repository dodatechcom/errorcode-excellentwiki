---
title: "[Solution] Linux: memory-coredump-limit -- core dump size limit"
description: "Fix Linux coredump limit errors. Core dump size limit preventing full crash dump."
os: ["linux"]
error-types: ["memory-error"]
severities: ["warning"]
---

# Linux: Core Dump Size Limit

Core dump size limits prevent complete crash dumps for debugging.

## Common Causes

- ulimit -c set to 0 or too small
- /proc/sys/kernel/core_pattern misconfigured
- Disk space insufficient for core dump
- systemd-coredump limiting core size
- Resource limits in systemd service unit

## How to Fix

### 1. Check Core Dump Settings

```bash
ulimit -c
cat /proc/sys/kernel/core_pattern
```

### 2. Enable Core Dumps

```bash
ulimit -c unlimited
echo "/var/crash/core.%e.%p.%t" | sudo tee /proc/sys/kernel/core_pattern
```

### 3. Configure Systemd Coredump

```bash
cat /etc/systemd/coredump.conf
# Edit: [Coredump] MaxUse=10G
sudo systemctl restart systemd-coredump
```

## Examples

```bash
$ ulimit -c
0
$ ulimit -c unlimited
$ ulimit -c
unlimited
```
