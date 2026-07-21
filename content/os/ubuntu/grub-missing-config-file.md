---
title: "[Solution] Ubuntu Server: grub-missing-config-file"
description: "Fix Ubuntu grub-missing-config-file. GRUB configuration file missing after upgrade or crash."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Missing Config File

The /boot/grub/grub.cfg or /etc/default/grub file is missing.

## Common Causes
- Accidental deletion during cleanup
- Filesystem corruption
- Disk partitioning change
- Failed GRUB upgrade

## How to Fix
1. Boot from live USB and check
```bash
ls /mnt/boot/grub/grub.cfg
ls /mnt/etc/default/grub
```
2. Rebuild grub.cfg
```bash
sudo chroot /mnt
update-grub
```
3. Recreate /etc/default/grub if missing
```bash
cat > /etc/default/grub << EOF
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
EOF
update-grub
```

## Examples
```bash
$ ls /etc/default/grub
ls: cannot access /etc/default/grub: No such file or directory
```
