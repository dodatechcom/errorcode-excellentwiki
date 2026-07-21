---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-nmi-error"
description: "Fix Ubuntu ubuntu-kernel-panic-nmi-error. NMI watchdog triggers kernel panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic NMI Error

NMI watchdog triggers kernel panic.

## Common Causes
- Hardware fault causing NMI
- Watchdog timeout exceeded
- Driver holding CPU too long

## How to Fix
1. Check NMI watchdog settings
```bash
cat /proc/sys/kernel/nmi_watchdog
```
2. Disable NMI watchdog temporarily
```bash
echo 0 | sudo tee /proc/sys/kernel/nmi_watchdog
```
3. Check kernel logs
```bash
dmesg | grep -i nmi
```

## Examples
```bash
$ cat /proc/sys/kernel/nmi_watchdog
1

$ dmesg | grep -i nmi
[  123.456] Uhhuh. NMI received for unknown reason 30 on CPU 0.
```