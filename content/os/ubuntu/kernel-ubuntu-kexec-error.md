---
title: "[Solution] Ubuntu Server: kernel-ubuntu-kexec-error"
description: "Fix Ubuntu kernel-ubuntu-kexec-error. kexec fails to load or boot a new kernel."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu Kexec Error

kexec fails to load a new kernel into memory for fast reboot.

## Common Causes
- New kernel image too large for reserved memory
- initrd not found at specified path
- Kernel architecture mismatch
- Memory fragmentation preventing allocation

## How to Fix
1. Check kexec status
```bash
cat /sys/kernel/kexec_loaded
```
2. Load kernel with kexec
```bash
sudo kexec -l /boot/vmlinuz-<version> --initrd=/boot/initrd.img-<version> --command-line="$(cat /proc/cmdline)"
```
3. Execute kexec
```bash
sudo kexec -e
```

## Examples
```bash
$ sudo kexec -l /boot/vmlinuz-5.15.0-25-generic --initrd=/boot/initrd.img-5.15.0-25-generic
$ sudo kexec -e
```
