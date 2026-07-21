---
title: "Swap File Creation Error"
description: "Failed to create or enable swap file on filesystem"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Swap File Creation Error

Failed to create or enable swap file on filesystem

## Common Causes

- Filesystem does not support swap files (e.g., Btrfs without special flags)
- File already exists at swap location
- Insufficient disk space for swap file
- fallocate not supported on filesystem

## How to Fix

1. Use `dd` instead of `fallocate` for incompatible filesystems
2. Check filesystem type: `df -Th /swapfile`
3. Ensure swapfile does not exist: `ls -la /swapfile`
4. For Btrfs: use `btrfs filesystem mkswapfile` instead

## Examples

```bash
# Create swap file with dd (works on all filesystems)
sudo dd if=/dev/zero of=/swapfile bs=1M count=4096 status=progress
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```
