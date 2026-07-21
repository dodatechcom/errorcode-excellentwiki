---
title: "[Solution] Ubuntu Server: grub-theme-loading-error"
description: "Fix Ubuntu grub-theme-loading-error. GRUB theme fails to load causing display issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Theme Loading Error

GRUB fails to load its graphical theme.

## Common Causes
- Theme files corrupted or missing
- Font files not found
- Graphics mode not supported by GPU
- Theme references missing images

## How to Fix
1. Check theme location
```bash
ls /boot/grub/themes/
```
2. Disable graphical theme temporarily
```bash
sudo nano /etc/default/grub
# Comment out GRUB_THEME line
sudo update-grub
```
3. Reinstall GRUB theme
```bash
sudo apt install --reinstall grub2-common
```

## Examples
```bash
$ sudo update-grub
Found theme: /boot/grub/themes/mytheme/theme.txt
grub-probe: error: cannot find GRUB drive for /dev/sda1
```
