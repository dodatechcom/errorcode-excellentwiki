---
title: "[Solution] Ubuntu Server: ubuntu-kernel-softlockup-error"
description: "Fix Ubuntu ubuntu-kernel-softlockup-error. Kernel soft lockup detected."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Soft Lockup Error

Kernel soft lockup is detected on a CPU.

## Common Causes
- Long-running code without yielding
- Driver bug causing spin loop
- Very high system load

## How to Fix
1. Check soft lockup messages
```bash
dmesg | grep -i "soft lockup"
```
2. Check watchdog
```bash
cat /proc/sys/kernel/watchdog
```
3. Increase soft lockup timeout
```bash
echo 120 | sudo tee /proc/sys/kernel/watchdog_thresh
```

## Examples
```bash
$ dmesg | grep -i "soft lockup"
[  123.456] watchdog: BUG: soft lockup - CPU#1 stuck for 23s!
```