---
title: "[Solution] systemd local-fs.target failed"
description: "Fix systemd local-fs.target failed. Resolve boot failures when local filesystem mounts fail."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd local-fs.target failed

## Error Description

local-fs.target: Failed to start. Local filesystems not mounted.

One or more local filesystem mounts failed during boot.

## Common Causes

Common Causes:
- /etc/fstab contains invalid entries
- Device specified in fstab does not exist
- Filesystem corruption requires fsck
- Mount point directory missing

## How to Fix

How to Fix:
```bash
# Check mount failures
systemctl --failed | grep mount

# Verify fstab
cat /etc/fstab
sudo systemd-analyze verify local-fs.target

# Boot to rescue mode and fix
sudo systemctl isolate rescue.target

# Run fsck
fsck /dev/sda1
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```