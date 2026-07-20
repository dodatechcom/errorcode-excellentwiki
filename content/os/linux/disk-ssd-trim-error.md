---
title: "[Solution] Linux: disk-ssd-trim-error — SSD TRIM error"
description: "Fix Linux disk-ssd-trim-error errors. SSD TRIM error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: SSD TRIM Error

TRIM errors occur when the kernel cannot issue discard commands to an SSD, preventing efficient garbage collection and degrading performance.

## Common Causes

- Filesystem mounted without discard support
- Kernel driver bug for the specific SSD controller
- SSD firmware does not support TRIM or has it disabled
- ATA pass-through issues with hardware RAID controllers
- Encrypted volumes not passing TRIM commands through (LUKS)

## How to Fix

### 1. Check TRIM Support

```bash
lsblk -D
# Check DISC-GRAN and DISC-MAX columns
```

### 2. Enable Periodic TRIM

```bash
sudo systemctl enable fstrim.timer
sudo systemctl start fstrim.timer
sudo fstrim -av
```

### 3. Enable Mount-Time Discard

```bash
# Add 'discard' to mount options in /etc/fstab
# /dev/sda1 / ext4 defaults,discard 0 1
```

### 4. Check Queue Limits

```bash
cat /sys/block/sdX/queue/discard_granularity
cat /sys/block/sdX/queue/discard_max_bytes
```

## Examples

```bash
$ lsblk -D
NAME   DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
sda           0      512B       2G         0
sda1          0      512B       2G         0

$ sudo fstrim -v /
/: 25.1 GiB were trimmed

$ sudo systemctl status fstrim.timer
● fstrim.timer - Discard unused blocks once a week
     Loaded: loaded
     Active: active (waiting)
```
