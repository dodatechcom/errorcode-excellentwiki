---
title: "[Solution] Ubuntu Server: kernel-uuid-mismatch-boot"
description: "Fix Ubuntu kernel-uuid-mismatch-boot. Root filesystem UUID does not match GRUB configuration."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel UUID Mismatch Boot

The root filesystem UUID referenced by GRUB does not match the actual UUID.

## Common Causes
- Partition was cloned or resized
- Filesystem was recreated
- GRUB not regenerated after partition change
- /etc/fstab uses outdated UUID

## How to Fix
1. Find current UUIDs
```bash
sudo blkid
```
2. Update GRUB configuration
```bash
sudo nano /etc/default/grub
sudo update-grub
```
3. Update /etc/fstab
```bash
sudo nano /etc/fstab
```

## Examples
```bash
$ sudo blkid
/dev/sda1: UUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890" TYPE="ext4"
/dev/sda2: UUID="12345678-abcd-1234-abcd-123456789abc" TYPE="ext4"
```
