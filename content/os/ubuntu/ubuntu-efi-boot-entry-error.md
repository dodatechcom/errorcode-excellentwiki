---
title: "Ubuntu EFI Boot Entry Error"
description: "UEFI boot entries incorrect or missing preventing Ubuntu from booting"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu EFI Boot Entry Error

UEFI boot entries incorrect or missing preventing Ubuntu from booting

## Common Causes

- EFI boot entry points to wrong partition
- Multiple Ubuntu EFI entries causing confusion
- BIOS/UEFI reset cleared boot entries
- Secure Boot blocking unsigned Ubuntu bootloader

## How to Fix

1. Check entries: `efibootmgr -v`
2. Add entry: `sudo efibootmgr --create --disk /dev/sda --part 1 --loader /EFI/ubuntu/grubx64.efi --label Ubuntu --verbose`
3. Delete wrong entry: `sudo efibootmgr -b XXXX -B`
4. Set boot order: `sudo efibootmgr -o XXXX,YYYY`

## Examples

```bash
# Check current EFI boot entries
efibootmgr -v

# Create new boot entry
sudo efibootmgr --create --disk /dev/sda --part 1 --loader /EFI/ubuntu/grubx64.efi --label Ubuntu

# Set boot order
sudo efibootmgr -o 0001,0002
```
