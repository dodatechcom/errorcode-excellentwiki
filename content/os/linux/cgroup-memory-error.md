---
title: "[Solution] Linux: cgroup-memory-error -- cgroup memory limit OOM"
description: "Fix Linux cgroup memory limit errors. Cgroup memory limit exceeded causing OOM kill."
os: ["linux"]
error-types: ["cgroup-error"]
severities: ["error"]
---

# Linux: Cgroup Memory Limit Error

Cgroup memory limit errors occur when processes hit allocated memory limits.

## Common Causes

- Memory limit too low for application workload
- Memory leak in cgroup child process
- swap accounting limit hit before main memory
- Kernel memory not accounted in cgroup limit
- OOM score adjustment protecting wrong processes

## How to Fix

### 1. Check Memory Usage

```bash
cat /sys/fs/cgroup/memory/memory.usage_in_bytes
cat /sys/fs/cgroup/memory/memory.limit_in_bytes
cat /sys/fs/cgroup/memory/memory.max
```

### 2. Increase Memory Limit

```bash
echo 4G | sudo tee /sys/fs/cgroup/memory/memory.limit_in_bytes
sudo systemctl set-property <service> MemoryMax=4G
```

### 3. Debug OOM

```bash
dmesg | grep -i "oom\|killed"
sudo journalctl -k | grep -i oom
cat /sys/fs/cgroup/memory/memory.oom_control
```

## Examples

```bash
$ cat /sys/fs/cgroup/memory/memory.usage_in_bytes
2147483648
$ cat /sys/fs/cgroup/memory/memory.limit_in_bytes
2147483648
# Usage at limit
$ dmesg | grep oom
[12345.678] Memory cgroup out of memory: Killed process 1234 (myapp)
```
