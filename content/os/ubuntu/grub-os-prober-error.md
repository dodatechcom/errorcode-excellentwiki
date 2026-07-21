---
title: "[Solution] Ubuntu Server: grub-os-prober-error"
description: "Fix Ubuntu grub-os-prober-error. GRUB os-prober fails to detect other operating systems."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Os Prober Error

GRUB os-prober fails to detect other operating systems.

## Common Causes
- os-prober package not installed
- NTFS driver missing for Windows partition
- Other OS partition not accessible
- os-prober disabled in GRUB

## How to Fix
1. Install os-prober
```bash
sudo apt install os-prober ntfs-3g
```
2. Enable os-prober
```bash
echo GRUB_DISABLE_OS_PROBER=false | sudo tee -a /etc/default/grub
sudo update-grub
```
3. Check detected systems
```bash
sudo os-prober
```

## Examples
```bash
$ sudo os-prober
/dev/sda3@/EFI/Microsoft/Boot/bootmgfw.efi:Windows Boot Manager:Windows:efi
```
