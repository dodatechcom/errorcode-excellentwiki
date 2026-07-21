---
title: "Swap Priority Configuration Error"
description: "Multiple swap devices with conflicting priorities or wrong priority order"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Swap Priority Configuration Error

Multiple swap devices with conflicting priorities or wrong priority order

## Common Causes

- Two swap devices with same priority value
- Swap priority not set causing random usage order
- Higher priority swap on slower device
- Swap on SSD and HDD with same priority

## How to Fix

1. Check swap priority: `swapon --show`
2. Set priority: `swapon -p <priority> /dev/sdX`
3. Update /etc/fstab with priority option
4. Disable lower-priority swap: `swapoff /dev/sdX`

## Examples

```bash
# Check current swap devices and priorities
swapon --show

# Set swap priority
sudo swapoff /dev/sdb2
sudo mkswap /dev/sdb2
sudo swapon -p 10 /dev/sdb2
# Update /etc/fstab
# /dev/sdb2 none swap sw,pri=10 0 0
```
