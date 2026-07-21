---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-cpu-stuck"
description: "Fix Ubuntu ubuntu-kernel-panic-cpu-stuck. CPU stuck error causes kernel panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic CPU Stuck

CPU stuck error leads to kernel panic.

## Common Causes
- CPU hardware issue
- Microcode bug
- Overheating causing CPU throttle

## How to Fix
1. Check CPU microcode
```bash
dmesg | grep -i microcode
```
2. Update microcode
```bash
sudo apt install intel-microcode
sudo apt install amd64-microcode
```
3. Check CPU temperature
```bash
sensors
```

## Examples
```bash
$ sensors
coretemp-isa-0000
Core 0: +75.0C  (high = +80.0C, crit = +100.0C)
```