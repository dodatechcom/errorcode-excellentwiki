---
title: "LXD Storage Pool Creation Error"
description: "Failed to create storage pool for LXD containers"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Storage Pool Creation Error

Failed to create storage pool for LXD containers

## Common Causes

- Storage backend (zfs, lvm, btrfs) not available
- Disk device not found or not accessible
- Insufficient disk space for storage pool
- ZFS module not loaded in kernel

## How to Fix

1. Check available storage backends: `lxd init --dump`
2. Verify ZFS: `modprobe zfs && zpool list`
3. Check disk space: `df -h /dev/sdX`
4. Create pool manually: `lxc storage create mypool zfs`

## Examples

```bash
# Check available storage drivers
lxc storage info

# Create ZFS storage pool
sudo lxc storage create mypool zfs volume.size=10GB

# List storage pools
lxc storage list
```
