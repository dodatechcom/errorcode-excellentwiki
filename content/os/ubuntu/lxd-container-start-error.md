---
title: "LXD Container Failed to Start"
description: "LXD container fails to start with various error messages"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Container Failed to Start

LXD container fails to start with various error messages

## Common Causes

- Container rootfs missing or corrupted
- Required kernel modules not loaded
- Storage backend error preventing mount
- AppArmor profile preventing container launch

## How to Fix

1. Check container logs: `lxc info --show-log <container>`
2. Verify rootfs: `ls /var/snap/lxd/common/lxd/storage-pools/*/containers/<container>/rootfs/`
3. Try starting in debug mode: `lxc start <container> --debug`
4. Check AppArmor: `sudo aa-status | grep lxd`

## Examples

```bash
# Get container logs
lxc info --show-log mycontainer

# Check container status
lxc list

# Start with debug output
lxc start mycontainer --debug
```
