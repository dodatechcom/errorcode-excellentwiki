---
title: "[Solution] Linux: hung-task — hung task detected"
description: "Fix Linux hung-task errors. hung task detected with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 10
---

# Linux: Hung Task Detected

A hung task occurs when a process remains in uninterruptible sleep (D-state) for more than 120 seconds.

## Common Causes

- Blocked I/O on a failing disk
- NFS server unresponsive
- FUSE filesystem deadlock
- Kernel module or driver stuck
- LVM or MD RAID operation blocked

## How to Fix

### 1. Identify Hung Tasks

```bash
ps aux | grep " D"
cat /proc/<pid>/stack
cat /proc/<pid>/wchan
```

### 2. Check Kernel Messages

```bash
dmesg | grep -i "hung task\|blocked" | tail -20
```

### 3. Check I/O Status

```bash
iostat -x 1
sudo iotop -oP
```

### 4. Check Filesystem Status

```bash
mount | grep <affected_mount>
sudo lsof <affected_mount>
```

## Examples

```bash
$ ps aux | grep " D"
root     12345  0.0  0.0      0     0 ?     D    Jul20   0:00 [kworker/u:2]

$ cat /proc/12345/stack
[<ffffffff81234567>] __lock_page+0x123/0x456
[<ffffffff81234568>] filemap_fault+0x234/0x567
[<ffffffff81234569>] __do_fault+0x56/0x89

$ dmesg | tail -5
[12345.678] INFO: task kworker/u:2:12345 blocked for more than 120 seconds.
[12345.679] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
```
