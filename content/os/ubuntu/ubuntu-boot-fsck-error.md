---
title: "Ubuntu Filesystem Check (fsck) Boot Error"
description: "System drops to fsck during boot to repair filesystem errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Filesystem Check (fsck) Boot Error

System drops to fsck during boot to repair filesystem errors

## Common Causes

- Filesystem corruption from unclean shutdown
- Disk bad sectors causing read/write errors
- Ext4 journal corruption
- Improper shutdown (power loss, forced reboot)

## How to Fix

1. Allow fsck to complete if prompted
2. Boot from live USB and run fsck manually
3. Check disk health: `sudo smartctl -a /dev/sda`
4. Mount and check: `sudo fsck -y /dev/sda1`

## Examples

```bash
# From live USB, check filesystem
sudo fsck -y /dev/sda1

# Check disk health
sudo smartctl -a /dev/sda

# Mount filesystem after repair
sudo mount /dev/sda1 /mnt
```
