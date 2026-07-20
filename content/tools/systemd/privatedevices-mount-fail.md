---
title: "[Solution] systemd PrivateDevices mount fail"
description: "Fix systemd PrivateDevices mount fail. Resolve service failures when /dev is private and causes mount issues."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd PrivateDevices mount fail

## Error Description

myapp.service: Failed to create private /dev. Mount failed.

The service cannot create its private /dev namespace.

## Common Causes

Common Causes:
- PrivateDevices=yes requires root
- /devtmpfs is not available
- Container environment prevents mount namespace
- Insufficient kernel support

## How to Fix

How to Fix:
```bash
# Check if the service runs as root
sudo systemctl edit myapp

# If root is required, ensure correct settings
```

```ini
[Service]
PrivateDevices=yes
# Or disable if not needed:
# PrivateDevices=no
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