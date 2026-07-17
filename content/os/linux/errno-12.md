---
title: "[Solution] Linux ENOMEM (errno 12) — Out of Memory Fix"
description: "Fix Linux ENOMEM (errno 12) Out of Memory error. Diagnose memory usage, configure swap, and fix OOM killer issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 40
---

# Linux ENOMEM (errno 12) — Out of Memory

ENOMEM (errno 12) means the kernel could not allocate memory for a requested operation. This can occur when the system has exhausted all available RAM and swap space, when a process tries to allocate more memory than its limit allows, or when the kernel itself runs out of memory for internal structures. On Linux, this error is closely tied to the OOM (Out of Memory) killer, which terminates processes to reclaim memory.

## Common Causes

- System RAM and swap are fully consumed
- A process has a memory leak consuming available resources
- Overcommit settings prevent large allocations
- ulimit memory limits are too low for the workload
- Too many processes competing for memory
- Kernel slab caches consuming excessive memory

## How to Fix ENOMEM

### 1. Check Current Memory Usage

Start by diagnosing how memory is being used:

```bash
# Show total, used, and free memory including swap
free -h
```

Example output:

```
              total        used        free      shared  buff/cache   available
Mem:           15Gi        14Gi       256Mi       512Mi       896Mi       345Mi
Swap:         2.0Gi       2.0Gi        12Mi
```

If `available` is very low and swap is full, the system is under memory pressure.

### 2. Find Processes Using the Most Memory

Identify which processes are consuming memory:

```bash
# Sort processes by memory usage (descending)
ps aux --sort=-%mem | head -20

# Or use top interactively
top

# Use htop for a more readable view
htop
```

To find a specific process's memory usage:

```bash
# Check a specific process
cat /proc/<PID>/status | grep VmRSS

# Or use pmap for detailed memory map
pmap <PID>
```

### 3. Check for Memory Leaks

Run the suspected program under a memory profiler:

```bash
# Using valgrind (slows execution significantly)
valgrind --leak-check=full --show-leak-kinds=all ./program

# Monitor a running process over time
# If RSS grows continuously, there is likely a leak
watch -n 5 'ps -p <PID> -o pid,rss,vsz,cmd'
```

### 4. Add or Expand Swap Space

If the system has little or no swap, adding swap provides a safety net:

```bash
# Check current swap
swapon --show

# Create a 4GB swap file
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make it permanent by adding to /etc/fstab
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Adjust swappiness to control how aggressively the kernel swaps:

```bash
# Check current swappiness
cat /proc/sys/vm/swappiness

# Lower value means less swapping (default is 60)
sudo sysctl vm.swappiness=10

# Make permanent
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
```

### 5. Adjust Overcommit Settings

Linux allows memory overcommit by default. You can tighten this:

```bash
# Check current overcommit mode
cat /proc/sys/vm/overcommit_memory

# Values: 0=heuristic, 1=always, 2=never overcommit
# Setting to 2 prevents overcommit and makes ENOMEM more predictable
sudo sysctl vm.overcommit_memory=2

# Adjust the overcommit ratio (percentage of RAM allowed to commit)
sudo sysctl vm.overcommit_ratio=80
```

### 6. Clear Caches and Buffers

Reclaim memory used by kernel caches without killing processes:

```bash
# Free page cache, dentries, and inodes
sudo sync && sudo sysctl -w vm.drop_caches=3

# Free only page cache
sudo sysctl -w vm.drop_caches=1

# Free dentries and inodes only
sudo sysctl -w vm.drop_caches=2
```

### 7. Adjust ulimit Settings

Per-process memory limits can trigger ENOMEM even when system RAM is available:

```bash
# Check current limits
ulimit -a

# Check address space limit
ulimit -v

# Increase virtual memory limit for the current session
ulimit -v unlimited

# For persistent changes, edit /etc/security/limits.conf
sudo nano /etc/security/limits.conf
```

Add:

```
* soft as unlimited
* hard as unlimited
```

### 8. Monitor OOM Killer Activity

Check if the OOM killer has been active:

```bash
# Check kernel logs for OOM killer events
dmesg | grep -i "oom\|out of memory\|killed process"

# Check system journal
journalctl -k | grep -i "oom\|killed process"
```

You can adjust which processes the OOM killer targets by modifying the oom_score_adj:

```bash
# Make a critical process less likely to be killed (-1000 to 1000)
echo -1000 | sudo tee /proc/<PID>/oom_score_adj

# Make a less important process more likely to be killed
echo 1000 | sudo tee /proc/<PID>/oom_score_adj
```

### 9. Check Kernel Slab Memory

Kernel objects (inodes, dentries, buffer caches) consume memory in the slab:

```bash
# View slab memory usage
slabtop

# Or check directly
cat /proc/meminfo | grep -i slab
```

## Prevention Tips

- Set up monitoring with tools like `htop`, `glances`, or `netdata`
- Configure swap as a safety net (at least 2-4 GB)
- Use cgroups to limit memory per service
- Profile memory usage regularly in production applications

## Related Error Codes

- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
