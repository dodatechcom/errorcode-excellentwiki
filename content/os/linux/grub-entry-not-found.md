---
title: "[Solution] Linux: grub-entry-not-found -- GRUB entry not found"
description: "Fix Linux GRUB entry not found errors. Boot entry missing in GRUB menu after update."
os: ["linux"]
error-types: ["boot-error"]
severities: ["error"]
---

# Linux: GRUB Entry Not Found

GRUB entry not found occurs when the bootloader cannot locate the kernel image.

## Common Causes

- Kernel image removed during cleanup
- New kernel installed but GRUB not regenerated
- Wrong root partition in GRUB config
- Filesystem UUID changed after reformatting
- Separate /boot partition not mounted

## How to Fix

### 1. Enter GRUB Rescue

```bash
ls (hd0,1)/boot/
ls (hd0,2)/boot/
set root=(hd0,2)
set prefix=(hd0,2)/boot/grub
insmod normal
normal
```

### 2. Regenerate GRUB Config

```bash
sudo mount /dev/sdXn /boot
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo update-grub
```

### 3. Install GRUB to Disk

```bash
sudo grub-install /dev/sda
sudo update-grub
```

## Examples

```bash
$ sudo grub-mkconfig -o /boot/grub/grub.cfg
Generating grub.cfg ...
Found linux image: /boot/vmlinuz-5.15.0-56-generic
Found initrd image: /boot/initrd.img-5.15.0-56-generic
```
