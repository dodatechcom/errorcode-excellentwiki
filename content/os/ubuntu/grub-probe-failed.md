---
title: "GRUB Probe Failed Error"
description: "grub-probe cannot determine device for boot partition"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# GRUB Probe Failed Error

grub-probe cannot determine device for boot partition

## Common Causes

- /boot on separate partition not detected by GRUB
- Device map file corrupted or missing
- UUID changes after disk re-partitioning
- LVM or RAID configuration not recognized

## How to Fix

1. Reinstall GRUB: `sudo grub-install /dev/sda`
2. Update device map: `sudo grub-mkdevicemap`
3. Check /boot is mounted: `mount | grep /boot`
4. Verify UUID in /etc/fstab matches actual partition UUID

## Examples

```bash
# Check current device map
cat /boot/grub/device.map

# Regenerate device map
sudo grub-mkdevicemap

# Reinstall GRUB
sudo grub-install /dev/sda
```
