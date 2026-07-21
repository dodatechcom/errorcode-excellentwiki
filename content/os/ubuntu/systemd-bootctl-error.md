---
title: "[Solution] Ubuntu Server: system-bootctl-error"
description: "Fix Ubuntu system-bootctl-error. bootctl fails to manage UEFI boot entries."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Bootctl Error

bootctl fails to create, delete, or list UEFI boot entries.

## Common Causes
- EFI variables not writable (Secure Boot)
- /sys/firmware/efi not mounted
- Boot entry already exists with same name
- Broken ESP filesystem

## How to Fix
1. Check EFI variable access
```bash
ls /sys/firmware/efi/
```
2. List boot entries
```bash
bootctl status
bootctl list
```
3. Create or fix boot entry
```bash
sudo bootctl install
sudo bootctl update
```

## Examples
```bash
$ bootctl status
System:
      Firmware: UEFI 2.70
  Secure Boot: enabled

$ sudo bootctl install
Failed to write variable: No such file or directory
```
