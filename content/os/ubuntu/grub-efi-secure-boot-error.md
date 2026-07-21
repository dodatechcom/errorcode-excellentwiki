---
title: "[Solution] Ubuntu Server: grub-efi-secure-boot-error"
description: "Fix Ubuntu grub-efi-secure-boot-error. GRUB EFI secure boot fails due to unsigned bootloader."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB EFI Secure Boot Error

System cannot boot in UEFI Secure Boot mode.

## Common Causes
- MOK not enrolled
- GRUB EFI binary not signed
- Shim bootloader not installed
- BIOS Secure Boot policy too restrictive

## How to Fix
1. Check Secure Boot status
```bash
mokutil --sb-state
```
2. Install signed GRUB and shim
```bash
sudo apt install grub-efi-amd64-signed shim-signed
```
3. Enroll MOK if needed
```bash
sudo mokutil --import /path/to/MOK.der
```

## Examples
```bash
$ mokutil --sb-state
SecureBoot enabled

$ sudo apt install grub-efi-amd64-signed shim-signed
```
