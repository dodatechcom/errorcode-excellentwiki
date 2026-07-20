---
title: "[Solution] systemd mount unit failed"
description: "Fix systemd mount unit failed errors. Resolve mount unit failures during system startup or manual mounting."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd mount unit failed

## Error Description

mnt-data.mount: Mount process exited, code=exited, status=32/FAILURE

The mount operation failed with exit code 32.

## Common Causes

Common Causes:
- The device specified in What= does not exist
- Filesystem type in Type= is not supported
- Mount point directory does not exist
- Device is busy or already mounted

## How to Fix

How to Fix:
```bash
# Check mount unit status
systemctl status mnt-data.mount

# Check the device
lsblk

# Create mount point if missing
sudo mkdir -p /mnt/data

# Test mount manually
sudo mount /dev/sdb1 /mnt/data
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