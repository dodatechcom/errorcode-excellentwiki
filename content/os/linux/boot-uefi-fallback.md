---
title: "[Solution] Linux: boot-uefi-fallback -- UEFI fallback to BIOS"
description: "Fix Linux UEFI boot fallback errors. System falling back to BIOS compatibility mode."
os: ["linux"]
error-types: ["boot-error"]
severities: ["error"]
---

# Linux: UEFI Boot Fallback Error

UEFI fallback occurs when the system cannot find a valid UEFI boot entry.

## Common Causes

- UEFI boot entry deleted from NVRAM
- CSM (Compatibility Support Module) enabled in BIOS
- shimx64.efi or grubx64.efi missing from ESP
- Secure Boot preventing unsigned bootloader
- Wrong architecture boot binary

## How to Fix

### 1. Check Boot Entries

```bash
efibootmgr -v
ls /boot/efi/EFI/
```

### 2. Create Boot Entry

```bash
sudo efibootmgr -c -d /dev/sda -p 1 -L "Linux" -l \\\\EFI\\\\ubuntu\\\\shimx64.efi
```

### 3. Disable CSM

```bash
# Enter BIOS setup and disable CSM/Legacy Boot
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --removable
```

## Examples

```bash
$ efibootmgr -v
BootCurrent: 0000
BootOrder: 0002,0001,0000
Boot0001* CD/DVD Drive  BIOS(3,PM,0x500)
Boot0002* Network       BIOS(3,PI,0x500)
# No Linux entry
```
