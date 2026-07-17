---
title: "[Solution] Linux Out of Memory — Kill Process at Fault Fix"
description: "Fix Linux 'Out of memory: Kill process' errors. Diagnose OOM killer triggers, identify memory hogs, and prevent critical process termination."
platforms: ["linux"]
severities: ["critical"]
error-types: ["runtime-error"]
tags: ["oom-killer", "kill-process", "out-of-memory", "memory-pressure", "swap"]
weight: 5
---

# Linux: Out of memory — Kill process

The `Out of memory: Kill process <PID> (<name>)` message means the kernel's OOM killer has terminated a process to free memory. This occurs when the system has exhausted all available RAM and swap, and the kernel must sacrifice a process to prevent a complete system freeze. The killed process loses all unsaved data.

## Common Causes

- Memory leak in an application consuming RAM over time
- Insufficient physical RAM for active workload
- Swap space exhausted or misconfigured
- Container/VM memory limits too restrictive
- Too many concurrent processes or threads
- Database or JVM heap size misconfiguration

## How to Fix

### 1. Identify the OOM Event

```bash
# Check kernel logs for OOM killer activity
dmesg | grep -A 20 "oom-killer"
sudo journalctl -k | grep -i "oom"

# Look for the killed process and its memory usage
# Example output:
# [12345.678] oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0-1,task=mysqld,pid=1234,uid=0
```

### 2. Check Memory Usage

```bash
# Overall memory status
free -h

# Show memory in megabytes
free -m

# Top memory-consuming processes
ps aux --sort=-%mem | head -15

# Detailed per-process memory
smem -t -p | head -20

# Check swap usage
swapon --show
```

### 3. Add or Increase Swap

```bash
# Check current swap
sudo swapon --show

# Create a swap file (e.g., 8GB)
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Adjust swappiness (lower = less aggressive swapping)
sudo sysctl vm.swappiness=10
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
```

### 4. Adjust OOM Killer Behavior

```bash
# Protect a critical process from OOM killer
sudo systemctl set-property myservice.service OOMScoreAdjust=-1000

# For non-systemd processes
sudo echo -1000 > /proc/<PID>/oom_score_adj

# Allow a process to be killed first (sacrificial)
sudo echo 1000 > /proc/<PID>/oom_score_adj

# Disable OOM killer entirely (not recommended)
sudo sysctl vm.oom-kill=0
```

### 5. Configure Memory Limits

For systemd services:

```ini
[Service]
MemoryMax=2G
MemoryHigh=1.5G
MemorySwapMax=500M
```

Apply via:

```bash
sudo systemctl edit myservice.service
sudo systemctl restart myservice.service
```

For Docker containers:

```bash
docker run -m 2g --memory-swap 3g myimage
docker update --memory 2g --memory-swap 3g container_name
```

### 6. Diagnose Memory Leaks

```bash
# Monitor memory growth over time
watch -n 5 'ps aux --sort=-%mem | head -10'

# Use valgrind for detailed leak analysis
valgrind --leak-check=full ./myapp

# Use top in batch mode
top -b -d 10 -n 6 | grep myapp
```

### 7. Tune Kernel Memory Parameters

```bash
# Reduce overcommit (more conservative memory allocation)
sudo sysctl vm.overcommit_memory=2
sudo sysctl vm.overcommit_ratio=80

# Reduce dirty page cache
sudo sysctl vm.dirty_ratio=10
sudo sysctl vm.dirty_background_ratio=5

# Set min_free_kbytes to reserve more memory
sudo sysctl vm.min_free_kbytes=65536
```

## Examples

```bash
$ dmesg | grep "Kill process"
[12345.678] Out of memory: Kill process 12345 (java) score 950 or sacrifice child
[12345.678] Killed process 12345 (java) total-vm:8192000kB, anon-rss:7500000kB, file-rss:0kB

$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi        14Gi       200Mi       200Mi       600Mi       300Mi
Swap:         2.0Gi       2.0Gi         0Bi
```

## Related Errors

- [OOM killer]({{< relref "/os/linux/oom-killer" >}}) — General OOM killer overview
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — Memory allocation failures
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk space exhaustion
