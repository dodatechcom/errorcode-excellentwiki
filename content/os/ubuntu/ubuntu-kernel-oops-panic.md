---
title: "[Solution] Ubuntu Server: ubuntu-kernel-oops-panic"
description: "Fix Ubuntu ubuntu-kernel-oops-panic. Kernel oops escalates to full panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Oops Panic

Kernel oops escalates to full kernel panic.

## Common Causes
- Oops in critical kernel path
- panic_on_oops=1 enabled
- Watchdog triggered after oops

## How to Fix
1. Check panic_on_oops setting
```bash
cat /proc/sys/kernel/panic_on_oops
```
2. Disable panic on oops
```bash
echo 0 | sudo tee /proc/sys/kernel/panic_on_oops
echo 'kernel.panic_on_oops = 0' | sudo tee -a /etc/sysctl.conf
```
3. Check kernel logs
```bash
journalctl -b -1 | grep -i oops
```

## Examples
```bash
$ cat /proc/sys/kernel/panic_on_oops
1
```