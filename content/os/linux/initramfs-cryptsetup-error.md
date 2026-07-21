---
title: "[Solution] Linux: initramfs-cryptsetup-error -- LUKS unlock failure"
description: "Fix Linux initramfs cryptsetup errors. LUKS encrypted volume unlock failure during boot."
os: ["linux"]
error-types: ["boot-error"]
severities: ["error"]
---

# Linux: Initramfs Cryptsetup Error

Initramfs cryptsetup errors prevent LUKS volumes from being unlocked during boot.

## Common Causes

- LUKS header corruption
- Incorrect passphrase or keyfile
- initramfs not including cryptsetup binary
- Kernel missing dm-crypt module
- UUID in crypttab does not match partition

## How to Fix

### 1. Boot from Live Media and Unlock

```bash
sudo cryptsetup luksOpen /dev/sdXn encrypted_vol
sudo vgchange -ay
ls /dev/mapper/
```

### 2. Check LUKS Status

```bash
sudo cryptsetup luksDump /dev/sdXn
sudo cryptsetup luksOpen --test-passphrase < /dev/sdXn
```

### 3. Rebuild initramfs

```bash
sudo mount /dev/mapper/root /mnt
sudo mount /dev/sdX1 /mnt/boot 2>/dev/null
sudo chroot /mnt
update-initramfs -u -k all
```

## Examples

```bash
$ sudo cryptsetup luksOpen /dev/sda3 encrypted_vol
Enter passphrase for /dev/sda3:
No key available with this passphrase.
$ sudo cryptsetup luksDump /dev/sda3 | grep -i slot
Key Slot 0: ENABLED
Key Slot 1: DISABLED
```
