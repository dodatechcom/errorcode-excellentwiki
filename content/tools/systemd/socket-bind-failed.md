---
title: "[Solution] systemd socket bind failed"
description: "Fix systemd socket bind failed errors. Resolve socket binding failures during activation."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd socket bind failed

## Error Description

myapp.socket: Failed to bind to [::]:80: Permission denied

systemd cannot bind the socket to the specified address.

## Common Causes

Common Causes:
- Binding to privileged port without root
- SELinux blocking the bind
- IPv6 not available or disabled
- Address format is invalid

## How to Fix

How to Fix:
```bash
# For privileged ports, ensure the socket has appropriate capabilities
sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenStream=8080
# Or use capabilities
# AmbientCapabilities=CAP_NET_BIND_SERVICE

# Check SELinux
sudo ausearch -m avc -ts recent
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