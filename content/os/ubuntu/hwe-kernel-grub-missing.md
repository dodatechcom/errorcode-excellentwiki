---
title: "HWE Kernel Not Listed in GRUB Menu"
description: "HWE kernel installed but not appearing in GRUB boot menu"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# HWE Kernel Not Listed in GRUB Menu

HWE kernel installed but not appearing in GRUB boot menu

## Common Causes

- GRUB not updated after HWE kernel installation
- GRUB timeout too short to show menu
- grub.cfg not regenerated
- Wrong GRUB_DEFAULT set

## How to Fix

1. Update GRUB: `sudo update-grub`
2. Check GRUB config: `grep menuentry /boot/grub/grub.cfg`
3. Set GRUB timeout: `GRUB_TIMEOUT=5` in /etc/default/grub
4. Reinstall GRUB if needed

## Examples

```bash
# Update GRUB to include new kernel
sudo update-grub

# Check available menu entries
grep menuentry /boot/grub/grub.cfg

# Set GRUB to show menu
sudo sed -i 's/GRUB_TIMEOUT=.*/GRUB_TIMEOUT=5/' /etc/default/grub
sudo update-grub
```
