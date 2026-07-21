---
title: "Ubuntu Hibernation Swap Too Small Error"
description: "System cannot hibernate because swap partition smaller than RAM"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Hibernation Swap Too Small Error

System cannot hibernate because swap partition smaller than RAM

## Common Causes

- Swap size less than installed RAM
- Swap partition not used as hibernation target
- Hibernation not configured in GRUB
-  resume= parameter missing from kernel cmdline

## How to Fix

1. Check swap: `swapon --show`
2. Compare with RAM: `free -h`
3. Add resume parameter: `GRUB_CMDLINE_LINUX='resume=/dev/sda2'`
4. Update GRUB: `sudo update-grub`

## Examples

```bash
# Check swap and RAM sizes
swapon --show
free -h

# Configure hibernation
echo 'GRUB_CMDLINE_LINUX="resume=/dev/sda2"' | sudo tee /etc/default/grub.d/hibernate.cfg
sudo update-grub
```
