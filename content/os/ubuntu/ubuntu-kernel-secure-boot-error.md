---
title: "[Solution] Ubuntu Server: ubuntu-kernel-secure-boot-error"
description: "Fix Ubuntu ubuntu-kernel-secure-boot-error. Kernel module rejected by Secure Boot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Secure Boot Error

Kernel modules are rejected because of Secure Boot restrictions.

## Common Causes
- Unsigned third-party module
- DKMS module not signed
- MOK not enrolled

## How to Fix
1. Check Secure Boot status
```bash
mokutil --sb-state
```
2. Sign module with MOK
```bash
sudo mokutil --import /path/to/MOK.der
# Reboot and enroll in MOK manager
```
3. Disable Secure Boot temporarily in BIOS

## Examples
```bash
$ mokutil --sb-state
SecureBoot enabled

$ sudo modprobe nvidia
modprobe: ERROR: could not insert 'nvidia': Required key not available
```