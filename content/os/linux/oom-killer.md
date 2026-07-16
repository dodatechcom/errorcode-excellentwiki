---
title: "[Solution] Linux Out of Memory (OOM Killer) — Fix Killed Process"
description: "Fix Linux 'Out of memory: Killed process' (OOM killer) errors. Diagnose memory usage, add swap, and prevent OOM kills with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["runtime-error"]
tags: ["oom-killer", "out-of-memory", "oom", "killed-process", "memory"]
weight: 5
---

# Linux: Out of Memory — OOM Killer

The `Out of memory: Killed process` message means the Linux kernel's OOM (Out of Memory) killer terminated a process because the system ran out of memory. When available RAM and swap are exhausted, the kernel selects the process with the highest memory usage (or "oom_score") and kills it to prevent a complete system freeze. This is a critical event because the killed process loses all its data.

## Common Causes

- Process memory leak consuming all available RAM
- Insufficient RAM or swap for the workload
- Too many memory-intensive processes running simultaneously
- Container or VM memory limits set too low
- Large database or application not properly tuned

## How to Fix

### 1. Check Current Memory Usage

Identify how much memory is in use and what's consuming it:

```bash
# Overall memory status
free -h

# Top memory consumers
ps aux --sort=-%mem | head -20

# Detailed per-process memory
top -o %MEM
```

### 2. Check OOM Killer Logs

Find which process was killed and why:

```bash
# Check kernel logs for OOM events
dmesg | grep -i "oom\|killed process"

# Or check system logs
journalctl -k | grep -i "oom\|killed process"
```

Example output:

```
[12345.678] Out of memory: Killed process 12345 (java) total-vm:2048000kB, anon-rss:1500000kB
```

### 3. Check OOM Scores

See which processes are most likely to be killed:

```bash
# View OOM score for all processes
for pid in $(ls /proc | grep -E '^[0-9]+$'); do
  echo "$(cat /proc/$pid/oom_score 2>/dev/null) $(cat /proc/$pid/comm 2>/dev/null)"
done | sort -rn | head -20

# Or check a specific process
cat /proc/$(pgrep -f "process-name")/oom_score
```

### 4. Add or Increase Swap Space

```bash
# Check current swap
sudo swapon --show

# Create a 4GB swap file
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make persistent in /etc/fstab
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Adjust swappiness (default is 60, lower means use swap less)
sudo sysctl vm.swappiness=10
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
```

### 5. Protect Important Processes from OOM Killer

```bash
# Make a process less likely to be killed (lower oom_score_adj)
echo -1000 | sudo tee /proc/$(pgrep -f "important-process")/oom_score_adj

# Make a process more likely to be killed (higher oom_score_adj)
echo 1000 | sudo tee /proc/$(pgrep -f "sacrificial-process")/oom_score_adj
```

### 6. Tune Memory Limits

For processes running under systemd:

```bash
# Edit the service unit file
sudo systemctl edit myservice.service

# Add memory limit
[Service]
MemoryMax=2G
MemoryHigh=1.5G
```

For containerized workloads, set appropriate memory limits in Docker:

```bash
docker run -m 2g myimage
```

### 7. Reduce Memory Usage

```bash
# Clear filesystem cache
sudo sync && sudo sysctl -w vm.drop_caches=3

# Kill memory-hungry processes
kill -9 $(ps aux --sort=-%mem | awk 'NR==2{print $2}')
```

## Examples

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi        14Gi       200Mi        50Mi        800Mi       500Mi
Swap:         2.0Gi       2.0Gi         0Bi

$ dmesg | grep "oom"
[  987.654] Out of memory: Killed process 1234 (mysqld) total-vm:8192000kB, anon-rss:7500000kB
```

## Related Errors

- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — malloc/mmap failure
- [Segmentation fault]({{< relref "/os/linux/segfault11" >}}) — Process crash from bad memory access
- [Too many open files]({{< relref "/os/linux/too-many-open-files" >}}) — File descriptor limit reached
