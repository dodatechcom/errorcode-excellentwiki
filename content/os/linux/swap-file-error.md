---
title: "[Solution] Linux: swap-file-error -- swap file creation error"
description: "Fix Linux swap file errors. Swap file creation or activation failure on filesystem."
os: ["linux"]
error-types: ["swap-error"]
severities: ["error"]
---

# Linux: Swap File Error

Swap file errors occur when creating or activating swap files fails.

## Common Causes

- Btrfs does not support traditional swap files
- Swap file missing permissions (0600)
- fstab entry pointing to wrong file
- Filesystem mounted with noexec
- Swap file on unsupported filesystem

## How to Fix

### 1. Check Swap File

```bash
ls -la /swapfile
file /swapfile
swapon --show
```

### 2. Create Proper Swap File

```bash
sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 3. Fix Btrfs Swap

```bash
sudo btrfs subvolume create /swap
sudo chattr +C /swap
sudo dd if=/dev/zero of=/swap/swapfile bs=1M count=4096
sudo mkswap /swap/swapfile
```

## Examples

```bash
$ sudo swapon /swapfile
swapon: /swapfile: read swap header failed
$ file /swapfile
/swapfile: ASCII text
# Not properly created - use dd
$ sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
Setting up swapspace version 1, size = 4 GiB
```
