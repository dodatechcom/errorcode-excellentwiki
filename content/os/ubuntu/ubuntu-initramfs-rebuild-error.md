---
title: "Ubuntu Initramfs Rebuild Error"
description: "update-initramfs fails during kernel update or manual rebuild"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Initramfs Rebuild Error

update-initramfs fails during kernel update or manual rebuild

## Common Causes

- Missing kernel modules required by initramfs
- Disk space full in /boot partition
- Broken symlinks in /lib/modules/
- Hook script in /etc/initramfs-tools/ has errors

## How to Fix

1. Check boot space: `df -h /boot`
2. Free space: remove old kernels: `sudo apt-get autoremove`
3. Rebuild: `sudo update-initramfs -u -k all`
4. Check hooks: `ls /etc/initramfs-tools/hooks/`

## Examples

```bash
# Check /boot space
df -h /boot

# Rebuild initramfs for all kernels
sudo update-initramfs -u -k all

# Remove old kernels to free space
sudo apt-get autoremove
```
