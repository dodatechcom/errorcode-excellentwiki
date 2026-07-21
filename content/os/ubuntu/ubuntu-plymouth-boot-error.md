---
title: "Ubuntu Plymouth Boot Splash Error"
description: "Plymouth boot splash screen fails to display or crashes"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Plymouth Boot Splash Error

Plymouth boot splash screen fails to display or crashes

## Common Causes

- Plymouth theme not found or corrupted
- GPU driver not compatible with Plymouth
- Framebuffer device not available
- Plymouth service disabled

## How to Fix

1. Check theme: `ls /usr/share/plymouth/themes/`
2. Set theme: `sudo plymouth-set-default-theme ubuntu-text`
3. Disable: add `plymouth.enable=0` to kernel params
4. Check logs: `journalctl -b | grep plymouth`

## Examples

```bash
# Check available Plymouth themes
ls /usr/share/plymouth/themes/

# Set default theme
sudo plymouth-set-default-theme ubuntu-text

# Disable Plymouth boot splash
echo 'GRUB_CMDLINE_LINUX="plymouth.enable=0"' | sudo tee /etc/default/grub.d/plymouth.cfg
sudo update-grub
```
