---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-init-not-found"
description: "Fix Ubuntu ubuntu-kernel-panic-init-not-found. Kernel cannot find init."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic Init Not Found

Kernel panics because it cannot find the init process.

## Common Causes
- root= parameter incorrect in GRUB
- initramfs missing init binary
- Root filesystem not mounted

## How to Fix
1. Boot from recovery
```bash
# At GRUB, edit boot entry and fix root=
```
2. Rebuild initramfs
```bash
sudo update-initramfs -u
```
3. Check root device
```bash
cat /proc/cmdline
sudo blkid
```

## Examples
```bash
$ dmesg | tail -5
[    1.234] Kernel panic - not syncing: No working init found.
```