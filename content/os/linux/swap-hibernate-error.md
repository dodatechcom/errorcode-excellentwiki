---
title: "[Solution] Linux: swap-hibernate-error -- hibernation resume failure"
description: "Fix Linux swap hibernation errors. Swap hibernation resume failure after suspend to disk."
os: ["linux"]
error-types: ["swap-error"]
severities: ["error"]
---

# Linux: Swap Hibernate Error

Hibernate resume errors occur when the system cannot resume from hibernation.

## Common Causes

- Swap partition too small for hibernation image
- resume= parameter missing from kernel command line
- UUID changed after reformatting
- Secure Boot blocking hibernation resume
- Kernel not compiled with suspend/resume support

## How to Fix

### 1. Check Resume Configuration

```bash
cat /proc/cmdline | tr ' ' '\\n' | grep resume
cat /etc/initramfs-tools/conf.d/resume 2>/dev/null
lsblk -o NAME,UUID,SIZE | grep swap
```

### 2. Set Resume Device

```bash
UUID=$(sudo blkid -s UUID -o value /dev/sdb1)
echo "RESUME=$UUID" | sudo tee /etc/initramfs-tools/conf.d/resume
sudo update-initramfs -u
```

### 3. Add Kernel Parameter

```bash
sudo vim /etc/default/grub
GRUB_CMDLINE_LINUX="resume=UUID=$UUID"
sudo update-grub
```

## Examples

```bash
$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz root=/dev/sda2 ro
# No resume= parameter
$ free -h | grep Swap
Swap: 8.0G
# Swap larger than RAM - OK for hibernation
```
