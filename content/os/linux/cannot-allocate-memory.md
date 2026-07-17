---
title: "[Solution] Linux 'Cannot allocate memory' — ENOMEM Fix"
description: "Fix Linux 'Cannot allocate memory' (ENOMEM) errors. Diagnose memory exhaustion, overcommit settings, and memory-hungry processes."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Cannot allocate memory (ENOMEM)

The `Cannot allocate memory` error (ENOMEM) occurs when a program's request for memory (via `malloc`, `mmap`, or similar) is denied by the kernel. This can happen because the system truly has no memory available, or because overcommit settings prevent the allocation. Unlike OOM killer events, this error is reported to the application directly.

## Common Causes

- System has exhausted all available RAM and swap
- Memory overcommit policy prevents large allocations
- Process is trying to allocate more memory than allowed by cgroup/ulimit limits
- Kernel memory fragmentation preventing large contiguous allocations
- Too many processes competing for limited memory

## How to Fix

### 1. Check Memory Status

```bash
# View total, used, and available memory
free -h

# Check overcommit settings
cat /proc/sys/vm/overcommit_memory
cat /proc/sys/vm/overcommit_ratio
```

The `available` column in `free -h` shows how much memory is actually available for new allocations.

### 2. Understand Overcommit Settings

| Value | Behavior |
|-------|----------|
| 0 | Heuristic overcommit (default) — kernel estimates if enough memory is available |
| 1 | Always overcommit — never refuses allocations |
| 2 | Strict — only allows allocations up to `swap + RAM * overcommit_ratio%` |

```bash
# Check current setting
cat /proc/sys/vm/overcommit_memory

# Set to heuristic (default)
sudo sysctl -w vm.overcommit_memory=0

# Set to always overcommit (can cause OOM kills)
sudo sysctl -w vm.overcommit_memory=1

# Set to strict mode (safer for critical systems)
sudo sysctl -w vm.overcommit_memory=2
sudo sysctl -w vm.overcommit_ratio=80
```

### 3. Check Per-Process Limits

```bash
# Check memory limits for the current session
ulimit -v

# Check limits for a specific process
cat /proc/$(pgrep -f "process-name")/limits | grep "Max address space"

# Increase virtual memory limit
ulimit -v unlimited
```

### 4. Add Swap Space

```bash
# Create a 4GB swap file
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make persistent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 5. Find Memory-Consuming Processes

```bash
# Top 10 memory consumers
ps aux --sort=-%mem | head -11

# Check a specific process's memory map
pmap -x $(pgrep -f "process-name")

# Total memory used by all processes
ps -eo rss,comm | awk '{sum+=$1} END {print sum/1024 " MB"}'
```

### 6. Reduce Memory Usage

```bash
# Clear page cache, dentries, and inodes
sudo sync && sudo sysctl -w vm.drop_caches=3

# Drop caches permanently for one run
echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### 7. Check for Memory Leaks

```bash
# Install valgrind
sudo apt install valgrind

# Check for leaks
valgrind --leak-check=full ./myprogram

# Monitor memory usage over time
watch -n 1 "ps -o pid,rss,vsz,comm -p $(pgrep -f myprogram)"
```

## Examples

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           16Gi        15Gi       100Mi        50Mi        800Mi       200Mi
Swap:         2.0Gi       2.0Gi         0Bi

$ python3 -c "x = bytearray(10**10)"
MemoryError: unable to allocate memory

# After adding swap and clearing cache:
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           16Gi        12Gi       2.0Gi        50Mi        800Mi       3.5Gi
Swap:         4.0Gi       500Mi       3.5Gi
```

## Related Errors

- [Out of memory / OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Process killed by OOM
- [Too many open files]({{< relref "/os/linux/too-many-open-files" >}}) — File descriptor exhaustion
- [Segmentation fault]({{< relref "/os/linux/segfault11" >}}) — Process crash from bad memory access
