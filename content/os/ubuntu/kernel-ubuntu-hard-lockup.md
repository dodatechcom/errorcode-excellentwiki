---
title: "[Solution] Ubuntu Server: kernel-ubuntu-hard-lockup"
description: "Fix Ubuntu kernel-ubuntu-hard-lockup. Kernel hard lockup detected on Ubuntu server."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu Hard Lockup

A hard lockup occurs when a CPU stops responding to interrupts for a prolonged period.

## Common Causes
- CPU stuck in an infinite loop with interrupts disabled
- Hardware failure (CPU, motherboard, power supply)
- Buggy kernel driver holding a spinlock too long
- Overheating causing CPU to halt

## How to Fix
1. Check watchdog messages
```bash
dmesg | grep -i "watchdog\|lockup\|hung_task"
journalctl -k | grep -i "lockup"
```
2. Check CPU temperature
```bash
sensors
cat /sys/class/thermal/thermal_zone*/temp
```
3. Disable watchdog temporarily
```bash
echo 0 | sudo tee /proc/sys/kernel/watchdog
```

## Examples
```bash
$ dmesg | grep -i lockup
[ 1234.567] watchdog: BUG: hard lockup on CPU#1, swapper/1
[ 1234.567] Watchdog: CPU 1 Hard LOCKUP
```
