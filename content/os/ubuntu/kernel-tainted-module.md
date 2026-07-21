---
title: "Kernel Tainted by Proprietary Module"
description: "Kernel marked as tainted after loading proprietary module"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Kernel Tainted by Proprietary Module

Kernel marked as tainted after loading proprietary module

## Common Causes

- NVIDIA proprietary driver loaded
- VirtualBox kernel modules loaded
- Other out-of-tree modules loaded
- Firmware loading from untrusted source

## How to Fix

1. Check taint status: `cat /proc/sys/kernel/tainted`
2. View loaded modules: `lsmod | grep -i nvidia`
3. Understand taint flags in kernel documentation
4. Consider using open-source alternatives (nouveau)

## Examples

```bash
# Check kernel taint status
cat /proc/sys/kernel/tainted

# View which modules are loaded
lsmod

# Check dmesg for taint warnings
dmesg | grep -i taint
```
