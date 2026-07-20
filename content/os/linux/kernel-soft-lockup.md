---
title: "[Solution] Linux: kernel-soft-lockup — Kernel soft lockup detected"
description: "Fix Linux kernel-soft-lockup errors. Kernel soft lockup detected with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["kernel-error"]
weight: 13
---
# Linux: Kernel Soft Lockup

A soft lockup occurs when a task runs in kernel mode for longer than the watchdog threshold (default 20 seconds) without yielding the CPU.

## Common Causes

- Kernel thread spinning in a loop without sleeping
- File system operation stuck on a slow disk (NFS, FUSE)
- Infinite loop in a kernel driver
- High IRQ handling consuming all CPU
- Memory pressure causing long page reclaim cycles

## How to Fix

### 1. Check Lockup Messages

```bash
dmesg | grep -i "soft lockup\|BUG: soft" | tail -30
```

### 2. Identify the Stuck Task

```bash
# Look for the task name in lockup message
dmesg | grep -A5 "soft lockup"
```

### 3. Increase Watchdog Threshold

```bash
sudo sysctl -w kernel.watchdog_thresh=30
```

### 4. Check Disk I/O

```bash
iostat -x 1 5
iotop -o
```

### 5. Check NFS Mounts

```bash
mount | grep nfs
# If NFS is hanging, use soft mount option
sudo mount -o hard,intr,timeo=30 <server>:/export /mnt
```

## Examples

```bash
$ dmesg | grep "soft lockup"
[ 5678.901] watchdog: BUG: soft lockup - CPU#2 stuck for 23s! [kworker/2:1:4567]
[ 5678.901] Modules linked in: nfs lockd grace fscache
[ 5678.901] CPU: 2 PID: 4567 Comm: kworker/2:1 Tainted: P        W  O
[ 5678.901] RIP: 0010:nfs_file_read+0x12/0x30 [nfs]
```
