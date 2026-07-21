---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-hung-task"
description: "Fix Ubuntu ubuntu-kernel-panic-hung-task. Hung task causes kernel panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic Hung Task

Hung task detector triggers kernel panic.

## Common Causes
- Task blocked for too long (120s default)
- Disk I/O completely stuck
- Filesystem deadlock

## How to Fix
1. Check hung task settings
```bash
cat /proc/sys/kernel/hung_task_timeout_secs
```
2. Disable panic on hung task
```bash
echo 0 | sudo tee /proc/sys/kernel/hung_task_panic
```
3. Check for stuck tasks
```bash
echo w > /proc/sysrq-trigger
```

## Examples
```bash
$ dmesg | grep -i "hung task"
[  123.456] INFO: task kworker/0:1:1234 blocked for more than 120 seconds.
```