---
title: "[Solution] Ubuntu Server: ubuntu-kernel-cpu-hotplug-error"
description: "Fix Ubuntu ubuntu-kernel-cpu-hotplug-error. CPU hotplug fails or causes instability."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel CPU Hotplug Error

CPU hotplug fails or causes issues.

## Common Causes
- CPU hotplug not supported by firmware
- Driver not handling CPU offline
- ACPI issue preventing hotplug

## How to Fix
1. Check CPU status
```bash
cat /sys/devices/system/cpu/online
cat /sys/devices/system/cpu/offline
```
2. Offline CPU
```bash
echo 0 | sudo tee /sys/devices/system/cpu/cpu3/online
```
3. Online CPU
```bash
echo 1 | sudo tee /sys/devices/system/cpu/cpu3/online
```

## Examples
```bash
$ cat /sys/devices/system/cpu/online
0-7
```