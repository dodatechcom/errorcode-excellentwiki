---
title: "Ubuntu Hugepages Configuration Error"
description: "Application fails to allocate hugepages or they are not available"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Hugepages Configuration Error

Application fails to allocate hugepages or they are not available

## Common Causes

- Hugepages not enabled in kernel boot parameters
- Insufficient hugepages allocated for workload
- Hugepage size not matching application requirement
- Transparent hugepages (THP) interfering with explicit hugepages

## How to Fix

1. Check hugepages: `cat /proc/meminfo | grep Huge`
2. Allocate: `echo 1024 | sudo tee /proc/sys/vm/nr_hugepages`
3. Check THP: `cat /sys/kernel/mm/transparent_hugepage/enabled`
4. Disable THP: `echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled`

## Examples

```bash
# Check hugepages status
grep -i huge /proc/meminfo

# Allocate hugepages
echo 2048 | sudo tee /proc/sys/vm/nr_hugepages

# Disable transparent hugepages
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```
