---
title: "[Solution] Linux: kernel-hard-lockup — Kernel hard lockup detected"
description: "Fix Linux kernel-hard-lockup errors. Kernel hard lockup detected with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["kernel-error"]
weight: 15
---
# Linux: Kernel Hard Lockup

A hard lockup occurs when a CPU stops responding to interrupts for a prolonged period (usually >60 seconds). The kernel watchdog detects this and reports it.

## Common Causes

- CPU stuck in an infinite loop with interrupts disabled
- Hardware failure (CPU, motherboard, power supply)
- Buggy kernel driver holding a spinlock too long
- Firmware/BIOS issue causing CPU to hang
- Overheating causing CPU to halt

## How to Fix

### 1. Check Watchdog Messages

```bash
dmesg | grep -i "watchdog\|lockup\|hung_task" | tail -30
journalctl -k | grep -i "lockup"
```

### 2. Disable Watchdog Temporarily

```bash
# For testing
echo 0 | sudo tee /proc/sys/kernel/watchdog
echo 0 | sudo tee /proc/sys/kernel/nmi_watchdog
```

### 3. Check CPU Temperature

```bash
sudo sensors
cat /sys/class/thermal/thermal_zone*/temp
```

### 4. Update BIOS/Firmware

Check vendor website for updates.

### 5. Check for Faulty Hardware

```bash
# Stress test the CPU
sudo apt install stress
stress --cpu 8 --timeout 60
```

## Examples

```bash
$ dmesg | grep -i lockup
[ 1234.567] watchdog: BUG: hard lockup on CPU#1, swapper/1, irq event stamp: 12345
[ 1234.567] Watchdog: CPU 1 Hard LOCKUP
[ 1234.567] Modules linked in: nvidia drm etc...
```
