---
title: "[Solution] Linux: btrfs-scrub-error — Btrfs scrub error"
description: "Fix Linux btrfs-scrub-error errors. Btrfs scrub error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["filesystem-error"]
weight: 10
---

# Linux: Btrfs Scrub Error Error

Btrfs scrub error errors occur when the B-tree filesystem encounters issues with scrub error operations.

## Common Causes

- Filesystem metadata or data corruption
- Device failure in multi-device filesystem
- Transaction commit failures due to power loss
- Subvolume or snapshot operation conflicts
- Insufficient free space for COW operations

## How to Fix

### 1. Check Btrfs Status

```bash
sudo btrfs filesystem show
sudo btrfs filesystem usage /mount/point
sudo btrfs device stats /mount/point
```

### 2. Check for Errors

```bash
sudo dmesg | grep -i btrfs | tail -20
sudo btrfs scrub start -B /mount/point
```

### 3. Repair Filesystem

```bash
sudo btrfs check /dev/sda1
sudo btrfs check --repair /dev/sda1
```

## Examples

```bash
$ sudo btrfs filesystem show
Label: none  uuid: xxxx
Total devices 1 FS bytes used 100.00GiB
devid    1 size 250.00GiB used 120.00GiB path /dev/sda1

$ sudo dmesg | grep -i btrfs | tail -3
[12345.678] Btrfs loaded, crc32c=crc32c-generic
[12345.679] BTRFS info (device sda1): disk space caching is enabled
```
