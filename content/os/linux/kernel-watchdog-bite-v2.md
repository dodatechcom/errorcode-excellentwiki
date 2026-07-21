---
title: "[Solution] Linux: kernel-watchdog-bite-v2 -- kernel watchdog bite timeout"
description: "Fix Linux kernel watchdog bite errors. Hardware watchdog timer firing and resetting system."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Watchdog Bite

A kernel watchdog bite occurs when the hardware watchdog fires because kernel did not reset it.

## Common Causes

- Kernel soft lockup preventing watchdog reset
- High system load starving the watchdog kthread
- Faulty watchdog hardware or driver bug
- CPU stuck in uninterruptible sleep (D state)
- NMI watchdog configured incorrectly

## How to Fix

### 1. Check Watchdog Logs

```bash
sudo dmesg | grep -i watchdog
sudo journalctl -k | grep -i watchdog
```

### 2. Monitor Soft Lockups

```bash
sudo sysctl kernel.softlockup_panic=1
sudo sysctl kernel.nmi_watchdog=1
cat /proc/sys/kernel/watchdog
```

### 3. Adjust Watchdog Timeout

```bash
echo 1 | sudo tee /proc/sys/kernel/watchdog
sudo sysctl -w kernel.watchdog_thresh=10
```

## Examples

```bash
$ sudo dmesg | grep watchdog
[12345.678] watchdog: BUG: soft lockup - CPU#3 stuck for 22s!
[12345.679] watchdog: hardware watchdog timeout
$ cat /proc/sys/kernel/watchdog
1
```
