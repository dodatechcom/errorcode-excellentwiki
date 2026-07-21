---
title: "[Solution] Ubuntu Server: grub-mkconfig-loop"
description: "Fix Ubuntu grub-mkconfig-loop. grub-mkconfig enters infinite loop during update-grub."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Grub Mkconfig Loop

update-grub hangs indefinitely because grub-mkconfig enters an infinite loop.

## Common Causes
- /etc/grub.d script contains infinite loop
- Circular symlink in /boot/grub
- Recursive call in custom grub script
- Broken os-prober detection

## How to Fix
1. Check which script hangs
```bash
sudo update-grub 2>&1 | head -5
```
2. Disable custom scripts temporarily
```bash
sudo chmod -x /etc/grub.d/40_custom
sudo update-grub
sudo chmod +x /etc/grub.d/40_custom
```
3. Check for circular symlinks
```bash
find /boot/grub -type l
```

## Examples
```bash
$ sudo update-grub
Sourcing file /etc/grub.d/40_custom
# Hangs here...

$ sudo chmod -x /etc/grub.d/41_custom
$ sudo update-grub
Generating grub configuration file ... done
```
