---
title: "[Solution] systemd D-Bus connection failed"
description: "Fix systemd D-Bus connection failed. Resolve communication failures between services and systemd."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd D-Bus connection failed

## Error Description

Failed to connect to D-Bus system bus: Connection refused

The service cannot communicate with systemd via D-Bus.

## Common Causes

Common Causes:
- D-Bus daemon is not running
- D-Bus socket is not accessible
- Service does not have D-Bus permissions
- D-Bus policy file is misconfigured

## How to Fix

How to Fix:
```bash
# Check D-Bus status
systemctl status dbus

# Restart D-Bus
sudo systemctl restart dbus

# Check D-Bus socket
ls -la /run/dbus/system_bus_socket

# Verify D-Bus configuration
ls /etc/dbus-1/system.d/
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