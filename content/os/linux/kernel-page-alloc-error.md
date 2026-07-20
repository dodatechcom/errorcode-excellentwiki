---
title: "[Solution] Linux: kernel-page-alloc-error — Page allocation failure in kernel"
description: "Fix Linux kernel-page-alloc-error errors. Page allocation failure in kernel with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["kernel-error"]
weight: 12
---
# Linux: Kernel Page Allocation Failure

Page allocation failures occur when the kernel cannot allocate physical memory pages, often indicating memory pressure.

## Common Causes

- System is out of memory (OOM condition approaching)
- Memory fragmentation preventing high-order allocations
- cgroup memory limit restricting the process
- Too many transparent hugepages consuming memory
- Kernel memory leak in a driver or filesystem

## How to Fix

### 1. Check Memory Status

```bash
free -h
cat /proc/buddyinfo
```

### 2. Check cgroup Limits

```bash
cat /sys/fs/cgroup/memory/memory.limit_in_bytes
cat /sys/fs/cgroup/memory/memory.usage_in_bytes
```

### 3. Reduce Memory Pressure

```bash
# Clear caches
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# Lower swappiness
sudo sysctl -w vm.swappiness=10

# Reduce page cache pressure
sudo sysctl -w vm.vfs_cache_pressure=200
```

### 4. Disable Transparent Hugepages

```bash
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```

## Examples

```bash
$ dmesg | grep "page allocation failure"
[12345.678] kworker/0:1: page allocation failure: order:2, mode:0xcc0(GFP_KERNEL)
[12345.678] CPU: 0 PID: 1234 Comm: kworker/0:1 Tainted: P        W  O

$ cat /proc/buddyinfo
Node 0, zone   Normal  12345 67890 234  0  0  0  0  0  0  0  0
# Low order-2 blocks indicate fragmentation
```
