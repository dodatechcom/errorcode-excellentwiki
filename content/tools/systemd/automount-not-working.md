---
title: "[Solution] systemd automount not working"
description: "Fix systemd automount not working. Resolve automount units that do not trigger on access."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd automount not working

## Error Description

mnt-data.automount: Automount not triggered when accessing /mnt/data.

The automount unit is not mounting on demand.

## Common Causes

Common Causes:
- Automount unit is not enabled
- The associated mount unit has errors
- Directory access is happening through a cached path
- The automount unit file is not properly configured

## How to Fix

How to Fix:
```bash
# Check automount status
systemctl status mnt-data.automount

# Enable and start
sudo systemctl enable mnt-data.automount
sudo systemctl start mnt-data.automount

# Test by accessing the mount point
ls /mnt/data
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