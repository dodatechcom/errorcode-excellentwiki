---
title: "[Solution] Ubuntu Server: ubuntu-cgroup-memory-pressure-error"
description: "Fix Ubuntu ubuntu-cgroup-memory-pressure-error. cgroup memory pressure monitoring fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Cgroup Memory Pressure Error

cgroup memory pressure monitoring fails.

## Common Causes
- memory.pressure file not available
- PSI not enabled
- cgroup v1 vs v2 incompatibility

## How to Fix
1. Check PSI support
```bash
cat /proc/pressure/memory
```
2. Check cgroup memory pressure
```bash
cat /sys/fs/cgroup/memory/memory.pressure
```
3. Enable PSI if needed
```bash
grep PSI /boot/config-$(uname -r)
```

## Examples
```bash
$ cat /proc/pressure/memory
some avg10=0.00 avg60=0.00 avg300=0.00 total=0
full avg10=0.00 avg60=0.00 avg300=0.00 total=0
```