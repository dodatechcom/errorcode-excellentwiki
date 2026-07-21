---
title: "[Solution] Ubuntu Server: kernel-snap-kernel-conflict"
description: "Fix Ubuntu kernel-snap-kernel-conflict. Snap kernel conflicts with system kernel packages."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Kernel Conflict

Snap-installed kernel conflicts with the system-installed kernel.

## Common Causes
- Both snap and apt kernels installed
- GRUB menu shows duplicate kernel entries
- snap kernel bypasses custom DKMS modules
- Kernel command-line arguments mismatch

## How to Fix
1. List installed kernels
```bash
dpkg -l | grep linux-image
snap list | grep kernel
```
2. Remove conflicting snap kernel
```bash
sudo snap remove ubuntu-kernel
```
3. Set default kernel in GRUB
```bash
sudo grub-set-default 0
sudo update-grub
```

## Examples
```bash
$ dpkg -l | grep linux-image
ii  linux-image-5.15.0-25-generic

$ snap list | grep kernel
kernel  5.15.0-25  1234 /stable/ canonical
```
