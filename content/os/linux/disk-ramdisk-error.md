---
title: "[Solution] Linux: disk-ramdisk-error — ramdisk initialization error"
description: "Fix Linux disk-ramdisk-error errors. ramdisk initialization error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 4
---
# Linux: RAM Disk / tmpfs Error

RAM disk errors occur with tmpfs or ramfs filesystems (used for /tmp, /dev/shm, container overlays).

## Common Causes

- tmpfs size limit reached (defaults to 50% of physical RAM)
- /tmp or /dev/shm too small for application requirements
- Containers or processes exhausting shared memory
- Kernel parameter tmpfs-size set too low

## How to Fix

### 1. Check tmpfs Usage

```bash
df -h | grep tmpfs
```

### 2. Resize tmpfs

```bash
# Remount with larger size
sudo mount -o remount,size=4G /tmp
sudo mount -o remount,size=8G /dev/shm
```

### 3. Make Persistent in fstab

```bash
# Add to /etc/fstab:
# tmpfs /tmp tmpfs defaults,size=4G 0 0
```

## Examples

```bash
$ df -h | grep tmpfs
tmpfs           3.9G  3.9G     0 100% /dev/shm

$ sudo mount -o remount,size=8G /dev/shm
$ df -h /dev/shm
tmpfs           8.0G  3.9G  4.1G  49% /dev/shm
```
