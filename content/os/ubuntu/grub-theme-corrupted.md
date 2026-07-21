---
title: "GRUB Theme Image Corrupted"
description: "GRUB boot menu displays incorrectly due to corrupted theme images"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# GRUB Theme Image Corrupted

GRUB boot menu displays incorrectly due to corrupted theme images

## Common Causes

- Theme PNG/JPG files corrupted during GRUB install
- Unsupported image format in GRUB theme
- Insufficient memory to load theme graphics
- Theme path incorrect in grub.cfg

## How to Fix

1. Reset theme: remove custom theme and use default
2. Check theme path in /boot/grub/themes/
3. Use PNG format with RGB color space
4. Update GRUB: `sudo update-grub`

## Examples

```bash
# Check GRUB theme directory
ls -la /boot/grub/themes/

# Reset to default theme
sudo rm -rf /boot/grub/themes/custom
sudo update-grub
```
