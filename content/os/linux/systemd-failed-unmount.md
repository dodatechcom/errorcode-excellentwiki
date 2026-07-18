---
title: "[Solution] Linux: systemd-failed-unmount — Failed unmounting during shutdown"
description: "Fix Linux systemd-failed-unmount errors. Failed unmounting during shutdown with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["boot-error"]
weight: 10
---

# Linux: systemd-failed-unmount — Failed unmounting during shutdown

Fix Linux systemd-failed-unmount errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Filesystem busy
- Stale NFS mounts
- Improper fstab entries
- Hardware failure

## How to Fix

### 1. Check Failed Mounts
```bash
systemctl --failed | grep umount
journalctl -b -u 'umount*'
```

### 2. Force Unmount
```bash
sudo umount -l /path/to/mount
sudo umount -f /path/to/mount
```

### 3. Fix fstab
```bash
sudo nano /etc/fstab
# Add 'nofail' option
```

### 4. Disable Problematic Units
```bash
sudo systemctl mask mount-<path>.mount
```

## Common Scenarios

- Shutdown hangs for minutes
- Failed unmount in boot logs
- Network mounts cause delay

## Prevent It

- Use 'nofail' for non-essential mounts
- Set timeouts for network mounts
- Release file handles before shutdown
