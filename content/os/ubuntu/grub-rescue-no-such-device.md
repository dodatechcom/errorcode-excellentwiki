---
title: "[Solution] Ubuntu Server: grub-rescue-no-such-device"
description: "Fix Ubuntu grub-rescue-no-such-device. GRUB rescue mode cannot find specified boot device."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Rescue No Such Device

GRUB enters rescue mode because it cannot find the specified device.

## Common Causes
- Disk device naming changed
- USB drive removed that was part of boot chain
- Disk failure or disconnected
- GRUB referencing wrong disk

## How to Fix
1. List available devices
```bash
grub> ls
```
2. Find correct partition
```bash
grub> ls (hd0,gpt1)/boot
grub> set root=(hd0,gpt1)
```
3. Boot manually
```bash
grub> linux /boot/vmlinuz-5.15.0-25-generic root=/dev/sda2
grub> initrd /boot/initrd.img-5.15.0-25-generic
grub> boot
```

## Examples
```bash
grub> ls
(hd0) (hd0,gpt3) (hd0,gpt2) (hd0,gpt1)
grub> ls (hd0,gpt2)/boot
vmlinuz-5.15.0-25-generic  initrd.img-5.15.0-25-generic
```
